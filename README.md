# Applied Data Science & Engineering Portfolio

Selected technical projects covering **MLOps and CI/CD**, **Big Data and distributed computing**, **LLM-guided optimization**, and **physics-informed anomaly detection**.

Each case study focuses on a different question: how predictive models can be operated and deployed reliably, how multi-million-record datasets can be processed with distributed systems, how LLMs can participate in iterative algorithm design, and how physical signals can reveal abnormal behavior in an industrial system.

| Project | Main question | Core technologies |
| --- | --- | --- |
| [Football Prediction MLOps & CI/CD](projects/01-football-mlops/README.md) | How can predictive models be operated through an automated MLOps and CI/CD pipeline that monitors data drift, triggers retraining when needed, validates containerized services, and deploys them to Google Cloud? | Python, DVC, MLflow, FastAPI, Docker, GitHub Actions, Google Cloud Storage, Artifact Registry, Cloud Run |
| [Large-Scale US Accidents Analytics with Apache Spark](projects/02-us-accidents-spark/README.md) | How can conventional analytical and machine-learning workloads be expressed and evaluated in a distributed-computing environment? | Apache Spark, Spark SQL/DataFrames, Spark MLlib, Scala, PySpark, Parquet, Google Cloud |
| [LLM-Guided Automatic Heuristic Design](projects/03-llm-optimization-thesis/README.md) | Can an LLM accelerate the traditionally manual process of generating, evaluating and iteratively improving optimization heuristics? | Python, LLM-guided code generation, TSP, clustering, automated evaluation, benchmarking |
| [iPrint Printhead Anomaly Detection & Early Warning](projects/04-iprint-anomaly-detection/README.md) | Can piezoelectric self-sensing signals from the printhead reveal abnormal nozzle behavior and provide early warning before non-jetting occurs? | Python, SciPy, scikit-learn, signal modelling, physical feature extraction, classification |

[Technical evidence register](docs/provenance.md)
