# Skills Evidence Map

| Technical area | Portfolio evidence |
| --- | --- |
| MLOps and model lifecycle | Football project: DVC artifact versioning, MLflow tracking, drift monitoring, conditional retraining and champion selection. [Case study](../projects/01-football-mlops/README.md) |
| CI/CD and cloud deployment | Football project: Docker build, container smoke test, Artifact Registry publication and Cloud Run deployment through GitHub Actions. [Deployment excerpt](../projects/01-football-mlops/code/deploy-excerpt.yml) |
| FastAPI and model serving | Football project: containerized prediction service deployed to managed Google Cloud infrastructure. [Case study](../projects/01-football-mlops/README.md) |
| Apache Spark and distributed analytics | US Accidents project: Spark DataFrame transformations and actions, reusable Parquet datasets and cloud benchmarking across a 7.7M-record dataset. [Case study](../projects/02-us-accidents-spark/README.md) |
| Scala and PySpark | US Accidents project: grouped weather/severity aggregation in Scala and Spark MLlib clustering in PySpark. [Scala excerpt](../projects/02-us-accidents-spark/code/weather_by_severity.scala) · [PySpark excerpt](../projects/02-us-accidents-spark/code/spark_clustering.py) |
| Spark MLlib and clustering | US Accidents project: distributed feature assembly, KMeans fitting and silhouette evaluation. [Clustering excerpt](../projects/02-us-accidents-spark/code/spark_clustering.py) |
| Operations research and heuristic optimization | Thesis: constructive heuristics, local refinement, p-median, TSP, algorithm evaluation and controlled benchmark protocols. [Case study](../projects/03-llm-optimization-thesis/README.md) |
| LLM-guided algorithm generation | Thesis: iterative candidate generation, feasibility validation, benchmark feedback, parent selection and diversity-control prompting. [Case study](../projects/03-llm-optimization-thesis/README.md) |
| Experimental design and algorithm evaluation | Thesis: quality/runtime trade-offs, stochastic variability, empirical scaling, multiple information regimes and mechanism verification. [TSP evaluator](../projects/03-llm-optimization-thesis/code/tsp_evaluation.py) |
| Physical signal modelling | iPrint project: piezoelectric self-sensing waveforms represented through robust damped-sinusoid fitting. [Fit excerpt](../projects/04-iprint-anomaly-detection/code/ringdown_fit.py) |
| Predictive modelling and robustness analysis | iPrint project: nozzle-state classification, separate pressure-sweep evaluation, early-warning horizons and exploratory pressure regression. [Case study](../projects/04-iprint-anomaly-detection/README.md) |
| Python scientific stack | NumPy, SciPy, pandas and scikit-learn are used across the iPrint, thesis and Football projects for numerical modelling, optimization experiments and monitoring. |
| Google Cloud | Football demonstrates containerized service deployment through Cloud Storage, Artifact Registry and Cloud Run. US Accidents demonstrates distributed Spark execution and cloud-based workload benchmarking. |
