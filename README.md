# Applied Data Science & Engineering Portfolio

Selected technical projects covering **MLOps and CI/CD**, **Big Data and distributed computing**, **LLM-guided optimization**, and **physics-informed anomaly detection**.

Each case study focuses on a different engineering question: how predictive models can be operated and deployed reliably, how multi-million-record datasets can be processed with distributed systems, how LLMs can participate in iterative algorithm design, and how physical self-sensing signals can reveal abnormal behavior in an industrial system.

| Project | Main question | Core technologies |
| --- | --- | --- |
| [Football Prediction MLOps & CI/CD](projects/01-football-mlops/README.md) | How can predictive models be operated through an automated MLOps and CI/CD pipeline that monitors data drift, triggers retraining when needed, validates containerized services, and deploys them to Google Cloud? | Python, DVC, MLflow, FastAPI, Docker, GitHub Actions, Google Cloud Storage, Artifact Registry, Cloud Run |
| [Large-Scale US Accidents Analytics with Apache Spark](projects/02-us-accidents-spark/README.md) | How can conventional analytical and machine-learning workloads be expressed and evaluated in a Big Data / distributed-computing environment? | Apache Spark, Spark SQL/DataFrames, Spark MLlib, Scala, PySpark, Parquet, Google Cloud |
| [LLM-Guided Automatic Heuristic Design](projects/03-llm-optimization-thesis/README.md) | Can an LLM accelerate the traditionally manual process of generating, evaluating and iteratively improving optimization heuristics? | Python, LLM-guided code generation, TSP, clustering, automated evaluation, benchmarking |
| [iPrint Printhead Anomaly Detection & Early Warning](projects/04-iprint-anomaly-detection/README.md) | Can acoustic self-sensing identify abnormal nozzle behavior and reveal signs of failure before non-jetting occurs? | Python, SciPy, scikit-learn, signal modelling, physical feature extraction, classification |

The projects are intentionally complementary:

- **Football MLOps** focuses on an automated model lifecycle: scheduled drift monitoring, drift-triggered retraining, model selection, container validation, and CI/CD deployment to Google Cloud Run.
- **US Accidents** focuses on Big Data processing, distributed transformations and Spark-based analytics.
- **LLM Heuristics** focuses on optimization research and automated algorithm design.
- **iPrint** focuses on physics-informed anomaly detection and early warning from acoustic self-sensing measurements in an industrial printhead.

[Skills evidence map](docs/skills-evidence-map.md) · [Technical evidence register](docs/evidence-register.md)
