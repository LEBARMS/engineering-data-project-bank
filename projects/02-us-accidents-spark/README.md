# Large-Scale US Accidents Analytics with Apache Spark

This project explored **Big Data processing and distributed analytics** using a dataset of **7,728,394 US traffic-incident records** from 2016–2023, representing approximately **3.06 GB** of raw data.

The objective was not simply to train models on an accident dataset. The project was designed to work with the tools and computational patterns used when analytical workflows move from conventional single-machine processing toward **distributed execution** across a cluster.

Apache Spark provided the central distributed-computing framework, while Parquet was used to create analytical datasets for downstream transformations, statistical analysis and machine-learning workloads.

## Big Data workflow

The original accident data was distributed as CSV.

The workflow progressively transformed this raw source into data structures better suited to repeated analytical processing:

1. Ingest the raw CSV dataset and convert it to Parquet.
2. Clean, cast and filter the required fields using Spark DataFrame transformations.
3. Engineer temporal, weather and geographical features using distributed Spark operations.
4. Run analytical workloads with Spark SQL/DataFrames, including grouped aggregations and statistical summaries.
5. Build machine-learning workflows with Spark MLlib, including feature-vector assembly, model fitting and evaluation.
6. Execute and benchmark selected Spark workloads on Google Cloud across increasing input sizes.

![Big Data workflow from the raw accident dataset through Spark transformations, Parquet storage, analytical workloads and cloud execution](assets/analysis-pipeline.png)

## Why Spark?

Spark allowed the project to express data preparation and modelling as operations over distributed DataFrames rather than as a single local dataframe held entirely by one Python process.

Representative Spark transformations included:

- filtering invalid or missing values;
- selecting and transforming columns;
- grouping records by analytical categories;
- computing grouped aggregations;
- constructing temporal and weather features;
- assembling numerical feature vectors for machine learning;
- applying fitted models.

## Why Parquet?

Parquet is a columnar binary storage format: unlike CSV, it stores typed columns in an encoded representation rather than plain text. This makes it more efficient for repeated Spark reads.

## Analytical workloads

The project covered several types of distributed analysis, including:

- weather and severity statistics;
- temporal and geographical feature engineering;
- Spark MLlib clustering;
- predictive modelling;
- execution-time and memory benchmarking across increasing input sizes.

This made it possible to compare not only analytical outputs but also the computational behavior of different Spark workloads.

## Cloud execution and benchmark

The objective of this experiment was to observe **scaling behavior and resource use in a distributed analytics setting**, rather than to report a single model-performance score.

Selected Spark workloads were executed and benchmarked on **Google Cloud**, with Google Cloud Storage used as part of the distributed workflow.

The recorded benchmark increased the amount of processed data up to approximately **7 million rows** and measured execution time and memory behavior for several analytical questions.

![Execution time and memory behavior for selected Spark workloads as the processed sample size increases](assets/spark-benchmark.png)

- **Q3 — Accident duration prediction** using random forest regression.
- **Q5 — Spatial clustering** using Spark MLlib KMeans.
- **Q6 — Hourly accident count prediction** using random forest regression.

The workloads exhibit a broadly similar increase in execution time as data volume grows, but at different absolute cost levels and with different configured memory requirements.

## Technical evidence

- [Grouped weather and severity statistics in Scala](code/weather_by_severity.scala)
- [Spark MLlib feature assembly, KMeans and silhouette evaluation in PySpark](code/spark_clustering.py)

## Technologies

Apache Spark · Spark SQL / DataFrames · Spark MLlib · Scala · PySpark · Parquet · H3 · Google Cloud · Google Cloud Storage

## Sources

[Source repository](https://github.com/MSE-202502-BDA/project-p_roth_ottiger_atallah_jouclard) · [Technical provenance](../../docs/provenance.md#us-accidents--spark)