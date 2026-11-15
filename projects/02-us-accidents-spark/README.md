# Large-Scale US Accidents Analytics with Apache Spark

This project explored **Big Data processing and distributed analytics** using a dataset of **7,728,394 US traffic-incident records** from 2016–2023, representing approximately **3.06 GB** of raw data.

The objective was not simply to train models on an accident dataset. The project was designed to work with the tools and computational patterns used when analytical workflows move from conventional in-memory processing toward **distributed data processing**.

Apache Spark provided the central execution framework, while Parquet was used to create reusable analytical datasets for downstream transformations, statistical analysis and machine-learning workloads.

## Big Data workflow

The original accident data was distributed as CSV.

The workflow progressively transformed this raw source into data structures better suited to repeated analytical processing:

1. ingest and clean the raw accident records with Spark;
2. cast and normalize the required fields;
3. engineer temporal, weather and geographical features;
4. persist cleaned and prepared datasets in **Parquet**;
5. reuse these Parquet datasets for Spark SQL/DataFrame analysis and Spark MLlib workloads;
6. execute and benchmark selected Spark workloads on Google Cloud.

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
- applying fitted models with `transform` to produce distributed DataFrames with predictions or cluster assignments.

Representative actions and model evaluation steps included:

- `count`;
- `collect` for compact aggregated outputs;
- model `fit`;
- silhouette evaluation.

For example, the weather/severity analysis groups accident records by severity and calculates distributed counts, means and standard deviations for weather variables before collecting only the reduced result table.

The clustering workflow uses `VectorAssembler` to construct feature vectors and **Spark MLlib KMeans** to fit an eight-cluster model directly from the Spark DataFrame.

## Why Parquet?

Repeatedly parsing and preparing the original CSV would duplicate preprocessing work across the different analyses.

The cleaned and engineered data was therefore persisted in **Parquet**, providing a reusable columnar analytical representation for subsequent Spark workloads.

This separated the ingestion/preparation stage from the downstream analyses and allowed multiple questions and models to operate on a common prepared dataset.

## Analytical workloads

The project covered several types of distributed analysis, including:

- weather and severity statistics;
- temporal and geographical feature engineering;
- Spark MLlib clustering;
- predictive modelling;
- execution-time and memory benchmarking across increasing input sizes.

This made it possible to compare not only analytical outputs but also the computational behavior of different Spark workloads.

## Cloud execution and benchmark

Selected Spark workloads were executed and benchmarked on **Google Cloud**, with Google Cloud Storage used as part of the distributed workflow.

The recorded benchmark increased the amount of processed data up to approximately **7 million rows** and measured execution time and memory behavior for several analytical questions.

![Execution time and memory behavior for selected Spark workloads as the processed sample size increases](assets/spark-benchmark.png)

### Benchmark workloads

- **Q3 — Accident duration prediction** using random forest regression.
- **Q5 — Spatial clustering** using Spark MLlib KMeans.
- **Q6 — Hourly accident count prediction** using random forest regression.

The benchmark shows that the different workloads do not have identical computational profiles. Execution time increases as the processed sample grows, while the relative cost and memory requirements depend on the analysis being performed.

The objective of this experiment was to observe **scaling behavior and resource use in a distributed analytics setting**, rather than to report a single model-performance score.

## Technical evidence

- [Grouped weather and severity statistics in Scala](code/weather_by_severity.scala)
- [Spark MLlib feature assembly, KMeans and silhouette evaluation in PySpark](code/spark_clustering.py)

## Technologies

Apache Spark · Spark SQL / DataFrames · Spark MLlib · Scala · PySpark · Parquet · H3 · Google Cloud · Google Cloud Storage

## Sources

[Technical evidence, benchmark and cloud provenance](../../docs/evidence-register.md#large-scale-us-accidents-analytics-with-apache-spark)
