# Source repository: TSM-MachLedata/MLOps
# Source path: github_portfolio/TSM-MachLedata__MLOps/src/monitor_drift.py
# Selection: run_ks_drift
# Purpose: Compute per-feature two-sample KS results and aggregate drift rate.
# Omissions: Imports, reference storage, windowing, reporting and orchestration.

def run_ks_drift(
    ref_df: pd.DataFrame,
    cur_df: pd.DataFrame,
    features: List[str],
    min_samples: int = 20,
) -> Tuple[float, pd.DataFrame]:
    """Run KS drift on a list of features and return drift_rate + report df."""
    results = []

    for col in features:
        if col not in ref_df.columns or col not in cur_df.columns:
            continue

        ref = ref_df[col].dropna()
        cur = cur_df[col].dropna()

        if len(ref) < min_samples or len(cur) < min_samples:
            continue

        stat, p_value = ks_2samp(ref, cur)
        drift = p_value < 0.05

        results.append({
            "feature": col,
            "ks_statistic": round(stat, 4),
            "p_value": round(float(p_value), 6),
            "drift_detected": bool(drift),
        })

    report_df = pd.DataFrame(results)

    if report_df.empty:
        return 0.0, report_df

    drift_rate = float(report_df["drift_detected"].mean())
    return drift_rate, report_df
