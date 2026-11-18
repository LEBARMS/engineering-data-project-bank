# Technical Provenance

This page records where the selected code excerpts and figures in the portfolio come from. Source paths are relative to the linked original repositories.

## Football MLOps

**Source repository:** [TSM-MachLedata/MLOps](https://github.com/TSM-MachLedata/MLOps)

| Portfolio artifact | Original source |
| --- | --- |
| [Feature-level drift detection](../projects/01-football-mlops/code/drift_monitor.py) | `src/monitor_drift.py` |
| [Conditional retraining](../projects/01-football-mlops/code/conditional_retraining.py) | `src/retrain_if_drift.py` |
| [Champion-model selection](../projects/01-football-mlops/code/champion_selection.py) | `src/select_champion.py` |
| [Deployment workflow excerpt](../projects/01-football-mlops/code/deploy-excerpt.yml) | `.github/workflows/deploy.yml` |
| [MLOps / CI/CD pipeline diagram](../projects/01-football-mlops/assets/training-and-serving.png) | Redrawn from `.github/workflows/retrain.yml`, `.github/workflows/deploy.yml`, `dvc.yaml`, `.dvc/config`, `src/retrain_if_drift.py`, `src/select_champion.py`, the Dockerfile and FastAPI application. |

## US Accidents / Spark

**Source repository:** [MSE-202502-BDA/project-p_roth_ottiger_atallah_jouclard](https://github.com/MSE-202502-BDA/project-p_roth_ottiger_atallah_jouclard)

| Portfolio artifact | Original source |
| --- | --- |
| [Weather and severity aggregation](../projects/02-us-accidents-spark/code/weather_by_severity.scala) | `notebooks/phase3/03_statistical_analysis_3_4.scala` |
| [Spark MLlib clustering](../projects/02-us-accidents-spark/code/spark_clustering.py) | `notebooks/phase4/4_5_Clustering_Spark_MLlib.ipynb` |
| [Spark workload benchmark](../projects/02-us-accidents-spark/assets/spark-benchmark.png) | `benchmark_plot.png`; workload labels verified against the project README and final presentation. |
| [Big Data pipeline diagram](../projects/02-us-accidents-spark/assets/analysis-pipeline.png) | Redrawn from the CSV-to-Parquet workflow, Spark DataFrame processing, feature-engineering notebooks, MLlib workflow and cloud benchmark material. |

## LLM Optimization Thesis

**Source repositories:** [TSP heuristics](https://github.com/TM-HESSO-202526/llm-tsp-heuristics) · [Clustering heuristics](https://github.com/TM-HESSO-202526/llm-clustering-heuristics)

| Portfolio artifact | Original source |
| --- | --- |
| [TSP validation and benchmark scoring](../projects/03-llm-optimization-thesis/code/tsp_evaluation.py) | `server_eval/run_selected_tsp_eval.py` |
| [Parent-selection logic](../projects/03-llm-optimization-thesis/code/parent_selection.py) | `src/llm_tsp/llamea_loop.py` |
| [Clustering objectives](../projects/03-llm-optimization-thesis/code/clustering_objectives.py) | `src/llm_clustering/objectives.py` |
| [P3 p-median heuristic](../projects/03-llm-optimization-thesis/code/pmedian_candidate_p3.py) | `experiments/selected_clustering_heuristics_final_by_objective/P_MEDIAN_data_point_centers/P3_heuristic.py` |
| [Heuristic-generation loop](../projects/03-llm-optimization-thesis/assets/generation-loop.png) | Redrawn from the generation-loop implementations and the final thesis methodology. |
| [Generated-vs-baseline comparison](../projects/03-llm-optimization-thesis/assets/refinement-tradeoffs.png) | Redrawn from the final thesis benchmark tables using the recorded evaluation results. |

## iPrint Predictive Maintenance

**Source repository:** [PA-iPrint-anomaly-detection/PA](https://github.com/PA-iPrint-anomaly-detection/PA)

| Portfolio artifact | Original source |
| --- | --- |
| [Damped-sinusoid fitting](../projects/04-iprint-anomaly-detection/code/ringdown_fit.py) | `fitting_loop_merge_labels.ipynb` |
| [Early-warning performance](../projects/04-iprint-anomaly-detection/assets/f1-by-lead-time.png) | `steps_before_failure.ipynb` |
| [Non-jetting classification results](../projects/04-iprint-anomaly-detection/assets/non-jetting-confusion.png) | Final project report, Figure 5.1. |
| [Anomaly-detection pipeline diagram](../projects/04-iprint-anomaly-detection/assets/signal-pipeline.png) | Redrawn from `preprocessing.ipynb`, `extract_ringdown.ipynb`, `fitting_loop_merge_labels.ipynb`, `binary_classification.ipynb` and `steps_before_failure.ipynb`. |