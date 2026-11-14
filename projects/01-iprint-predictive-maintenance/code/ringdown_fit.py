# Source repository: PA-iPrint-anomaly-detection/PA @ a53dc5b
# Source path: github_portfolio/PA-iPrint-anomaly-detection__PA/fitting_loop_merge_labels.ipynb
# Selection: Cell 4; damped_sine_baseline_gamma, fit_sliding_windows, summarize_windows
# Purpose: Define the physical response, overlapping-window fit and parameter summary.
# Omissions: Imports, initializer and optimizer helpers, data loading and notebook orchestration.

def damped_sine_baseline_gamma(t, A, gamma, f, phi, C, D):
    return C + D*t + A*np.exp(-gamma*t)*np.sin(2*np.pi*f*t + phi)


def fit_sliding_windows(t, y, dt, cycles=6, overlap=0.5,
                        robust=True,
                        local_ratio=None,
                        use_weight='tukey'):
    """
    Windowed fitting with overlap-add.
    Returns:
        yhat_oa : overlap-add reconstruction over full t
        params  : array (nwin, 6) of [A, tau, f, phi, C, D] per window
        nrmse   : array (nwin,) window nrmse
        idxs    : list of slice objects for each window on original t
        meta    : dict with L, H, f0
    """
    y = np.asarray(y, float)
    t = np.asarray(t, float)

    # coarse frequency to set window length ~ cycles/f0
    f0 = _coarse_freq(y, dt)
    L = int(max(64, np.round((cycles / max(f0, 1.0)) / dt)))  # samples per window
    H = int(max(1, np.round(L * (1 - overlap))))              # hop
    if L > len(y):  # degenerate case
        L = len(y)
        H = max(1, L // 2)

    # --- analysis/synthesis windows ---
    # Interior frames: tapered; first/last: rectangular to avoid edge collapse
    if use_weight == 'tukey':
        w_core = tukey(L, 0.25)
    else:
        w_core = np.hanning(L)
    w_edge = np.ones(L)

    yhat_oa = np.zeros_like(y, float)
    wsum    = np.zeros_like(y, float)

    params_list = []
    nrmse_list  = []
    idxs        = []

    prev = None
    base_bounds = (
        [0.0, 1e4, 5e3, -np.pi, -1e9, -1e12],   # A, gamma, f, phi, C, D
        [1e9, 1e7, 3e5,  np.pi,  1e9,  1e12],
    )

    # default "slow drift" local constraints
    if local_ratio is None:
        local_ratio = dict(A=0.5, tau=0.5, f=0.2, phi=np.pi/3, C=5e4, D=1e10)

    for wi, start in enumerate(range(0, len(y) - L + 1, H)):
        sl = slice(start, start + L)
        idxs.append(sl)
        t_win = t[sl]; y_win = y[sl]

        # build local bounds around previous params if available
        if prev is not None and np.all(np.isfinite(prev)):
            bounds_local = _make_local_bounds(prev, local_ratio, base_bounds)
        else:
            bounds_local = base_bounds

        popt, yhat_win, rmse, nrm = fit_one(t_win, y_win, dt,
                                            bounds=bounds_local,
                                            robust=robust)

        params_list.append(popt)
        nrmse_list.append(nrm)

        # --- edge-safe overlap-add ---
        is_last = (start + L >= len(y))
        w_use = w_edge if (wi == 0 or is_last) else w_core
        yhat_oa[sl] += w_use * yhat_win
        wsum[sl]    += w_use

        prev = popt

    # avoid division by tiny numbers at very edges
    wsum_safe = np.where(wsum > 1e-9, wsum, 1.0)
    yhat_oa /= wsum_safe

    params_arr = np.vstack(params_list)
    nrmse_arr  = np.array(nrmse_list)

    meta = dict(L=L, H=H, f0=f0, cycles=cycles, overlap=overlap)
    return yhat_oa, params_arr, nrmse_arr, idxs, meta


def summarize_windows(params_arr, nrmse_arr, mode='nrmse'):
    """
    Weighted summary of window parameters.
    Returns a 6-vector [A, tau, f, phi, C, D] (phi left as circular mean).
    """
    A, tau, f, phi, C, D = params_arr.T
    gamma = 1/np.clip(tau, 1e-12, None)

    if mode == 'nrmse':
        w = 1/np.clip(nrmse_arr, 1e-6, None)**2
    elif mode == 'amplitude':
        w = np.clip(A, 1e-12, None)**2
    else:
        w = np.ones_like(A)

    def wmean(x): return float(np.sum(w*x)/np.sum(w))
    Abar = wmean(A)
    gbar = wmean(gamma); taubar = 1.0/max(gbar, 1e-12)
    fbar = wmean(f)
    Cbar = wmean(C); Dbar = wmean(D)

    # circular mean for phase (optional; often refit is better)
    sinp = wmean(np.sin(phi)); cosp = wmean(np.cos(phi))
    phibar = float(np.arctan2(sinp, cosp))
    return np.array([Abar, taubar, fbar, phibar, Cbar, Dbar], float)
