# Source repository: TM-HESSO-202526/llm-tsp-heuristics
# Source path: github_portfolio/TM-HESSO-202526__llm-tsp-heuristics/server_eval/run_selected_tsp_eval.py
# Selection: normalize_tour and run_one
# Purpose: Validate a tour and record score, runtime and failure status.
# Omissions: Imports, data definitions, evaluator helpers, aggregation and CLI.

def normalize_tour(raw_tour: Any, n: int) -> np.ndarray:
    arr = np.asarray(raw_tour, dtype=np.int64).reshape(-1)
    validate_tour(arr, n)
    return arr


def run_one(
    h: HeuristicSpec,
    inst: TSPInstance,
    problem: SparseTSPProblem,
    rep: int,
    seed: int,
    timeout_s: float,
) -> dict[str, Any]:
    start = time.perf_counter()
    stdout_tail = ""
    try:
        mod_name = f"tsp_selected_{abs(hash((h.signal_category, h.heuristic_id, rep, inst.name))) % 10**12}"
        mod = module_from_path(h.code_path, mod_name)
        capture = io.StringIO()
        with contextlib.redirect_stdout(capture):
            raw = call_heuristic_from_module(mod, problem, np.random.default_rng(seed), timeout_s, seed)
        out = capture.getvalue()
        stdout_tail = out[-1000:] if out else ""

        tour = normalize_tour(raw, problem.n)
        objective_value = tour_cost_from_matrix(tour, problem.distance_matrix_for_evaluator())
        gap = 100.0 * (objective_value - inst.optimum) / inst.optimum if inst.optimum > 0 else np.nan
        candidate_edge_count, total_edges = problem.tour_candidate_edge_count(tour)
        uses_only_candidates = None
        candidate_edge_share = None
        if candidate_edge_count is not None and total_edges is not None:
            uses_only_candidates = bool(total_edges and candidate_edge_count == total_edges)
            candidate_edge_share = float(candidate_edge_count) / float(total_edges) if total_edges else None

        return {
            "signal_category": h.signal_category,
            "heuristic_id": h.heuristic_id,
            "heuristic_label": h.heuristic_label,
            "code_path": str(h.code_path.relative_to(REPO_ROOT) if h.code_path.is_relative_to(REPO_ROOT) else h.code_path),
            "instance_name": inst.name,
            "split": inst.split,
            "n": inst.n,
            "rep": rep,
            "seed": seed,
            "objective_value": objective_value,
            "reference_value": inst.optimum,
            "gap_ref_pct": gap,
            "runtime_s": time.perf_counter() - start,
            "status": "ok",
            "error_type": "",
            "error_message": "",
            "uses_only_candidates": uses_only_candidates,
            "candidate_edge_count": candidate_edge_count,
            "total_edges": total_edges,
            "candidate_edge_share": candidate_edge_share,
            "stdout_tail": stdout_tail,
            "hostname": socket.gethostname(),
        }
    except CandidateTimeoutError as e:
        return error_row(h, inst, rep, seed, start, "timeout", type(e).__name__, str(e), stdout_tail)
    except Exception as e:
        return error_row(h, inst, rep, seed, start, "error", type(e).__name__, str(e), stdout_tail, traceback.format_exc(limit=8))
