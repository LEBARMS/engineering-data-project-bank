# Skills Evidence Map

| Skill | Evidence and where to start |
| --- | --- |
| Signal processing and physical modeling | iPrint isolates a piezoelectric ring-down and fits a damped sinusoid with six interpretable parameters. [Fit excerpt](../projects/01-iprint-predictive-maintenance/code/ringdown_fit.py) |
| Python, NumPy and SciPy | iPrint fits and summarizes windows with NumPy/SciPy. Football uses SciPy for feature-level drift. [iPrint](../projects/01-iprint-predictive-maintenance/README.md) · [Drift excerpt](../projects/03-football-mlops/code/drift_monitor.py) |
| pandas and scikit-learn | iPrint builds supervised feature tables and evaluates histogram gradient boosting. The thesis uses scikit-learn clustering baselines. [iPrint](../projects/01-iprint-predictive-maintenance/README.md) · [Thesis](../projects/02-llm-optimization-thesis/README.md) |
| Classification, regression and robustness | iPrint separates nozzle-state detection, pressure regression and onset prediction, with a nozzle-grouped holdout and sweep transfer tests. [Results](../projects/01-iprint-predictive-maintenance/README.md#results-across-operating-sequences) |
| Operations research, TSP and heuristic optimization | The thesis varies TSP information regimes and evaluates solution feasibility, objective gaps and runtime. [TSP evaluator](../projects/02-llm-optimization-thesis/code/tsp_evaluation.py) |
| LLM-guided code generation and experimentation | The thesis ties candidate generation to executable interfaces, benchmark feedback and parent selection. [Experimental system](../projects/02-llm-optimization-thesis/README.md#experimental-system) |
| Clustering | The thesis implements SSE, p-median and radius-volume objectives. The accident project applies Spark MLlib KMeans and silhouette. [Objective code](../projects/02-llm-optimization-thesis/code/clustering_objectives.py) · [Spark code](../projects/04-us-accidents-spark/code/spark_clustering.py) |
| Apache Spark, Spark SQL/DataFrames, Scala and PySpark | The accident project computes grouped weather statistics, builds Parquet features and benchmarks distributed workloads on Google Cloud. [Scala excerpt](../projects/04-us-accidents-spark/code/weather_by_severity.scala) · [Case study](../projects/04-us-accidents-spark/README.md) |
| DVC, MLflow and Cloud Storage | Football versions artifacts and records experiments. Its drift workflow selects and reproduces stages conditionally. [Model lifecycle](../projects/03-football-mlops/README.md#model-lifecycle-and-deployment) |
| FastAPI, Docker, GitHub Actions, Artifact Registry and Cloud Run | Football integrates inference endpoints, a local container smoke test, image publication and managed deployment. [Deployment excerpt](../projects/03-football-mlops/code/deploy-excerpt.yml) |

