# Source repository: PA-iPrint-anomaly-detection/PA @ a53dc5b
# Source path: github_portfolio/PA-iPrint-anomaly-detection__PA/steps_before_failure.ipynb
# Selection: Cell 3; _row_singleK_delta
# Purpose: Build the acoustic deltas and previous-step flag for one onset-relative sample.
# Omissions: Imports, dataset builders, splitting, training and evaluation.

def _row_singleK_delta(nozzle_id: int, y: int, step_pos: int, seq_sweep: np.ndarray,
                      pressures: np.ndarray, idx_sweep: np.ndarray, K: int) -> dict:
    """
    seq_sweep is already in sweep order (P,6).
    Features: d0..d5 + has_prev. (No K/step_pos in features)
    """
    step_pos = int(step_pos)
    x = seq_sweep[step_pos].astype(float)

    has_prev = 1 if step_pos - 1 >= 0 else 0
    if has_prev:
        x_prev = seq_sweep[step_pos - 1].astype(float)
        d = x - x_prev
    else:
        d = np.zeros_like(x)

    p = float(pressures[int(idx_sweep[step_pos])])

    row = {
        "nozzle": int(nozzle_id),
        "y": int(y),
        "K": int(K),                  # metadata only
        "step_pos": int(step_pos),    # metadata only
        "pressure": p,                # metadata only
        "has_prev": int(has_prev),
    }
    for j in range(d.shape[0]):
        row[f"d{j}"] = float(d[j]) if np.isfinite(d[j]) else np.nan
    return row
