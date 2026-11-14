# Technical Evidence Register

Source paths are relative to the named source repository unless a workspace path is shown. Commit references identify the versions used. Each excerpt lists its selection and omissions in the header.

## iPrint Predictive Maintenance

Repository `PA-iPrint-anomaly-detection/PA` at `a53dc5b`. Final PA report by Anthony Atallah, dated February 2026.

| Portfolio evidence | Original source |
| --- | --- |
| [Ring-down fitting](../projects/01-iprint-predictive-maintenance/code/ringdown_fit.py) | `github_portfolio/PA-iPrint-anomaly-detection__PA/fitting_loop_merge_labels.ipynb`, cell 4, waveform model, windowed fit and summary functions. |
| [Lead-time feature construction](../projects/01-iprint-predictive-maintenance/code/lead_time_features.py) | `github_portfolio/PA-iPrint-anomaly-detection__PA/steps_before_failure.ipynb`, cell 3, `_row_singleK_delta`. |
| [Lead-time F1 plot](../projects/01-iprint-predictive-maintenance/assets/f1-by-lead-time.png) | Original embedded PNG in `github_portfolio/PA-iPrint-anomaly-detection__PA/steps_before_failure.ipynb`, cell 5, output 1. |
| [Non-jetting confusion matrices](../projects/01-iprint-predictive-maintenance/assets/non-jetting-confusion.png) | Redrawn from Figure 5.1, PDF p. 28 in `github_portfolio/PA-iPrint-anomaly-detection__PA/AtallahAnthony_rapport_MSE_PA_SA25.pdf`. Non-jetting F1 is computed from the reported counts as 2TP / (2TP + FP + FN). |
| [Signal pipeline](../projects/01-iprint-predictive-maintenance/assets/signal-pipeline.png) | New diagram from `github_portfolio/PA-iPrint-anomaly-detection__PA/preprocessing.ipynb` cell 10, `github_portfolio/PA-iPrint-anomaly-detection__PA/extract_ringdown.ipynb` cell 4, `github_portfolio/PA-iPrint-anomaly-detection__PA/fitting_loop_merge_labels.ipynb` cells 4, 6, 8, 12 and 14, `github_portfolio/PA-iPrint-anomaly-detection__PA/binary_classification.ipynb` cell 3, and `github_portfolio/PA-iPrint-anomaly-detection__PA/steps_before_failure.ipynb` cell 3. |

Shape and acquisition scope come from the PA report, §§3.1–3.2. The report’s Figure 5.1 and the classification notebook provide classification counts. Early-warning F1 at K=1–3 is recorded in the lead-time notebook cell 3. Pressure-regression metrics are in `github_portfolio/PA-iPrint-anomaly-detection__PA/predict_pressure.ipynb`, cells 6 and 8.

## LLM Optimization Thesis

Repositories `TM-HESSO-202526/llm-tsp-heuristics` at `862bb0c` and `TM-HESSO-202526/llm-clustering-heuristics` at `1c810e0`. Primary results and protocol source: Anthony Atallah, *Development of Optimization Heuristics with AI*, HES-SO MSE, June 2026, `github_portfolio/AtallahAnthony_rapport_MSE_TM_SP26.pdf`.

| Portfolio evidence | Original source |
| --- | --- |
| [TSP scoring excerpt](../projects/02-llm-optimization-thesis/code/tsp_evaluation.py) | `github_portfolio/TM-HESSO-202526__llm-tsp-heuristics/server_eval/run_selected_tsp_eval.py`, `normalize_tour` and `run_one`. |
| [Parent selection](../projects/02-llm-optimization-thesis/code/parent_selection.py) | `github_portfolio/TM-HESSO-202526__llm-tsp-heuristics/src/llm_tsp/llamea_loop.py`, `select_parent` and `parent_selection_reason`. |
| [Clustering objective module](../projects/02-llm-optimization-thesis/code/clustering_objectives.py) | `github_portfolio/TM-HESSO-202526__llm-clustering-heuristics/src/llm_clustering/objectives.py`, complete small module. |
| [C1a generated candidate](../projects/02-llm-optimization-thesis/code/tsp_candidate_c1a.py) | `github_portfolio/TM-HESSO-202526__llm-tsp-heuristics/experiments/selected_tsp_heuristics_final_by_signal/candidate_list/C1a_heuristic.py`. LLM-generated, curated and selected for evaluation. |
| [Generation loop](../projects/02-llm-optimization-thesis/assets/generation-loop.png) | New diagram adapted from final report Figure 3.1 (PDF p. 16), Tables 3.1–3.3 and §3.3.3. Implementations in `github_portfolio/TM-HESSO-202526__llm-tsp-heuristics/src/llm_tsp/llamea_loop.py` and `github_portfolio/TM-HESSO-202526__llm-clustering-heuristics/scripts/run_unified_pipeline.py`. |
| [Refinement trade-offs](../projects/02-llm-optimization-thesis/assets/refinement-tradeoffs.png) | Redrawn from final report Tables 5.1 and 6.1 (PDF pp. 36 and 43). Within-problem medians for D1/D1a and S1/SB1. |

Benchmark coverage is in final report Tables 3.2–3.3. Candidate-list and edge-prior results come from Tables 5.5 and 5.7 (PDF pp. 39 and 41), with separate instance coverage. P-median and radius-volume results come from Tables 6.3 and 6.5 (PDF pp. 46 and 50). §3.6 defines references, variability and empirical scaling. Chapters 7–9 cover attribution and interpretation.

## Football MLOps

Canonical repository `TSM-MachLedata/MLOps` at `b81fff3`. The team project records a Cloud Run deployment in its README and implements the release in GitHub Actions.

| Portfolio evidence | Original source |
| --- | --- |
| [Feature drift](../projects/03-football-mlops/code/drift_monitor.py) | `github_portfolio/TSM-MachLedata__MLOps/src/monitor_drift.py`, `run_ks_drift`. |
| [Conditional retraining](../projects/03-football-mlops/code/conditional_retraining.py) | `github_portfolio/TSM-MachLedata__MLOps/src/retrain_if_drift.py`, `retrain_models` and `main`. |
| [Champion selection](../projects/03-football-mlops/code/champion_selection.py) | `github_portfolio/TSM-MachLedata__MLOps/src/select_champion.py`, `main`. |
| [Deployment excerpt](../projects/03-football-mlops/code/deploy-excerpt.yml) | `github_portfolio/TSM-MachLedata__MLOps/.github/workflows/deploy.yml`, from `Smoke test container in CI` through `Deploy to Cloud Run`. |
| [Training and serving](../projects/03-football-mlops/assets/training-and-serving.png) | New diagram from `github_portfolio/TSM-MachLedata__MLOps/.github/workflows/retrain.yml`, `github_portfolio/TSM-MachLedata__MLOps/src/retrain_if_drift.py`, `github_portfolio/TSM-MachLedata__MLOps/dvc.yaml`, `github_portfolio/TSM-MachLedata__MLOps/.dvc/config`, `github_portfolio/TSM-MachLedata__MLOps/src/train_model2.py`, `github_portfolio/TSM-MachLedata__MLOps/.github/workflows/deploy.yml`, `github_portfolio/TSM-MachLedata__MLOps/Dockerfile` and `github_portfolio/TSM-MachLedata__MLOps/app/main.py`. |

The 30% trigger is a threshold in the workflow and retraining logic, measured as a share of tested numeric features.

## US Accidents / Spark

MA-BDA US Accidents academic team repository at `1d55298`.

| Portfolio evidence | Original source |
| --- | --- |
| [Scala weather summaries](../projects/04-us-accidents-spark/code/weather_by_severity.scala) | `notebooks/phase3/03_statistical_analysis_3_4.scala`, aggregation/export block in `SeverityWeatherAnalysis.main`. |
| [Spark MLlib clustering](../projects/04-us-accidents-spark/code/spark_clustering.py) | `notebooks/phase4/4_5_Clustering_Spark_MLlib.ipynb`, cells 6, 8 and 10. |
| [UMAP figure](../projects/04-us-accidents-spark/assets/cluster-umap.png) | Original embedded plot in `notebooks/phase4/03_statistical_analysis_3_5.ipynb` at `c9157ee`, cell 11, output 2. The team presentation includes the same plot on p. 9. |
| [Benchmark figure](../projects/04-us-accidents-spark/assets/spark-benchmark.png) | Original team image `benchmark_plot.png`. |
| [Spark pipeline](../projects/04-us-accidents-spark/assets/analysis-pipeline.png) | New diagram from `scripts/download_dataset.sh`, `notebooks/phase3/01_load_clean_exploration.ipynb`, `notebooks/phase4/4_1_feature_builder.ipynb`, `notebooks/phase4/4_4_Anthony.ipynb`, and the MLlib notebook above. The GCS benchmark annotation comes from §3.5 of the source `README.md` in that checkout and the cloud context from `docs/presentation_roth_ottiger_atallah_jouclard.pdf`, pp. 20–22. |

The saved Phase 3 load output supplies the row count. The team presentation reports 3.06 GB (p. 4) and 68.54% exploratory cluster-to-severity correspondence (p. 10). The benchmark plot records runs up to 7 million rows.
