# Source repository: TM-HESSO-202526/llm-tsp-heuristics
# Source path: github_portfolio/TM-HESSO-202526__llm-tsp-heuristics/src/llm_tsp/llamea_loop.py
# Selection: select_parent and parent_selection_reason
# Purpose: Select a search parent from measured candidate records.
# Omissions: Imports, record definitions, strategy normalization, prompt building and iteration orchestration.

def select_parent(records: list[CandidateRecord], strategy: str) -> CandidateRecord | None:
    if not records:
        return None
    strategy = normalized_selection_strategy(strategy)
    if strategy == "1,1":
        # Sequential mutation chain: always mutate the most recent generated candidate,
        # whether or not it is the best-so-far.
        return records[-1]
    if strategy == "1+1":
        # Elitist 1+1: mutate the best full-valid candidate so far; if none exists,
        # fall back to the best partial candidate by penalized score, then latest candidate.
        full_valid = [r for r in records if r.full_valid and r.selection_score is not None]
        if full_valid:
            return min(full_valid, key=lambda r: (float(r.selection_score), r.attempt))
        partial = [r for r in records if r.valid_instances > 0 and r.selection_score is not None]
        if partial:
            return min(partial, key=lambda r: (float(r.selection_score), r.attempt))
        return records[-1]
    raise ValueError(f"Unknown selection_strategy {strategy!r}; expected '1+1' or '1,1'.")


def parent_selection_reason(records: list[CandidateRecord], strategy: str, parent: CandidateRecord | None) -> str:
    if parent is None:
        return "no_parent_initial_generation"
    strategy = normalized_selection_strategy(strategy)
    if strategy == "1,1":
        return "latest_candidate_1comma1"
    full_valid = [r for r in records if r.full_valid and r.selection_score is not None]
    if full_valid and parent.attempt == min(full_valid, key=lambda r: (float(r.selection_score), r.attempt)).attempt:
        return "best_full_valid_1plus1"
    partial = [r for r in records if r.valid_instances > 0 and r.selection_score is not None]
    if partial and parent.attempt == min(partial, key=lambda r: (float(r.selection_score), r.attempt)).attempt:
        return "best_partial_penalized_1plus1"
    return "latest_no_valid_or_partial_1plus1"
