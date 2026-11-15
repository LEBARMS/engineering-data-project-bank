# Technical Evidence Register

This document records the origin of the focused code excerpts and visuals used in the public portfolio. Source paths refer to the original project repositories or final reports. The portfolio contains selected technical evidence rather than copies of the complete source projects.

## Football Prediction MLOps & CI/CD

Canonical repository: `TSM-MachLedata/MLOps`

| Portfolio evidence | Original source |
| --- | --- |
| [Feature-level drift detection](../projects/01-football-mlops/code/drift_monitor.py) | `src/monitor_drift.py`, `run_ks_drift`. |
| [Conditional retraining](../projects/01-football-mlops/code/conditional_retraining.py) | `src/retrain_if_drift.py`, retraining and threshold logic. |
| [Champion-model selection](../projects/01-football-mlops/code/champion_selection.py) | `src/select_champion.py`, champion selection logic. |
| [Deployment workflow excerpt](../projects/01-football-mlops/code/deploy-excerpt.yml) | `.github/workflows/deploy.yml`, container smoke test through Cloud Run deployment. |
| [Model lifecycle diagram](../projects/01-football-mlops/assets/training-and-serving.png) | Redrawn from `.github/workflows/retrain.yml`, `.github/workflows/deploy.yml`, `src/retrain_if_drift.py`, `src/select_champion.py`, `dvc.yaml`, `.dvc/config`, `src/train_model2.py`, `Dockerfile` and `app/main.py`. |

## Large-Scale US Accidents Analytics with Apache Spark

Source repository: US Accidents academic project

| Portfolio evidence | Original source |
| --- | --- |
| [Scala weather/severity aggregation](../projects/02-us-accidents-spark/code/weather_by_severity.scala) | `notebooks/phase3/03_statistical_analysis_3_4.scala`, grouped numerical weather summaries and weather-condition counts. |
| [Spark MLlib clustering](../projects/02-us-accidents-spark/code/spark_clustering.py) | `notebooks/phase4/4_5_Clustering_Spark_MLlib.ipynb`, feature assembly, KMeans and silhouette evaluation. |
| [Spark benchmark](../projects/02-us-accidents-spark/assets/spark-benchmark.png) | Recorded benchmark figure `benchmark_plot.png`. The portfolio legend uses the workload names verified in the source `README.md` §4.11 and final presentation slide 21. Plot values are preserved. |
| [Distributed analytics pipeline](../projects/02-us-accidents-spark/assets/analysis-pipeline.png) | Redrawn from `scripts/download_dataset.sh`, `notebooks/phase3/01_load_clean_exploration.ipynb`, `notebooks/phase4/4_1_feature_builder.ipynb`, `notebooks/phase4/4_4_Anthony.ipynb`, the MLlib notebook above, `README.md` §3.5 and `docs/presentation_roth_ottiger_atallah_jouclard.pdf`, pp. 20–22. |

## LLM-Guided Automatic Heuristic Design

TSP repository: `TM-HESSO-202526/llm-tsp-heuristics`

Clustering repository: `TM-HESSO-202526/llm-clustering-heuristics`

Clustering source revision used for the portfolio: `1c810e0`

Primary methodology and result source: Anthony Atallah, *Development of Optimization Heuristics with AI — LLM-Guided Generation and Evaluation of Heuristics for TSP and Clustering*, HES-SO MSE master thesis, June 2026. Local source `github_portfolio/AtallahAnthony_rapport_MSE_TM_SP26.pdf`.

| Portfolio evidence | Original source |
| --- | --- |
| [TSP feasibility and benchmark scoring](../projects/03-llm-optimization-thesis/code/tsp_evaluation.py) | `server_eval/run_selected_tsp_eval.py`, selected validation and scoring functions. |
| [Parent selection](../projects/03-llm-optimization-thesis/code/parent_selection.py) | `src/llm_tsp/llamea_loop.py`, parent-selection logic. |
| [Clustering objectives](../projects/03-llm-optimization-thesis/code/clustering_objectives.py) | `src/llm_clustering/objectives.py`. |
| [P3 p-median candidate](../projects/03-llm-optimization-thesis/code/pmedian_candidate_p3.py) | `experiments/selected_clustering_heuristics_final_by_objective/P_MEDIAN_data_point_centers/P3_heuristic.py`. LLM-generated, curated candidate selected for final evaluation. |
| [Generation-loop diagram](../projects/03-llm-optimization-thesis/assets/generation-loop.png) | Redrawn from final thesis Figure 3.1 (PDF p. 16), the TSP loop in `src/llm_tsp/llamea_loop.py` and clustering pipeline in `scripts/run_unified_pipeline.py`. |
| [Generated-vs-baseline comparison](../projects/03-llm-optimization-thesis/assets/refinement-tradeoffs.png) | Redrawn from final thesis Tables 6.1 and 6.3 (PDF pp. 43 and 46) using recorded final values only. |

## iPrint Printhead Anomaly Detection & Early Warning

Repository: `PA-iPrint-anomaly-detection/PA`

Primary report: final HEIA-FR PA report, February 2026, `AtallahAnthony_rapport_MSE_PA_SA25.pdf`.

| Portfolio evidence | Original source |
| --- | --- |
| [Damped-sinusoid fitting](../projects/04-iprint-anomaly-detection/code/ringdown_fit.py) | `fitting_loop_merge_labels.ipynb`, cell 4, waveform model, robust windowed fitting and feature summarization. |
| [Early-warning F1 plot](../projects/04-iprint-anomaly-detection/assets/f1-by-lead-time.png) | Original embedded output from `steps_before_failure.ipynb`, cell 5, output 1. |
| [Non-jetting confusion matrices](../projects/04-iprint-anomaly-detection/assets/non-jetting-confusion.png) | Redrawn from the final report classification counts, Figure 5.1 (PDF p. 28), using the intended non-jetting class interpretation. |
| [Signal-processing pipeline](../projects/04-iprint-anomaly-detection/assets/signal-pipeline.png) | Redrawn from `preprocessing.ipynb` cell 10, `extract_ringdown.ipynb` cell 4, `fitting_loop_merge_labels.ipynb` cells 4, 6, 8, 12 and 14, `binary_classification.ipynb` cell 3, and `steps_before_failure.ipynb` cell 3. |
