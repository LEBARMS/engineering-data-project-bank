# Source repository: MA-BDA US Accidents team repository @ 1d55298
# Source path: notebooks/phase4/4_5_Clustering_Spark_MLlib.ipynb
# Selection: Cells 6, 8 and 10
# Purpose: Assemble location/weather vectors, fit k=8 KMeans and score silhouette in Spark MLlib.
# Omissions: Imports, Spark setup, Parquet ingestion and scaling experiments.

feature_cols = [
    "lat_center","lon_center",
    "Temperature(F)_z","Humidity(%)_z","Pressure(in)_z",
    "Visibility(mi)_z","Wind_Speed(mph)_z","Precipitation(in)_z"
]
vec_assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
clust_df = vec_assembler.transform(df).select("features","lat_center","lon_center").cache()
print("Vectorised rows:", clust_df.count())

kmeans = KMeans(featuresCol="features", k=8, seed=42, maxIter=20)
pipeline = Pipeline(stages=[kmeans])

proc = psutil.Process()
t0 = time.time()
kmodel = pipeline.fit(clust_df)
train_time = time.time() - t0
ram = proc.memory_info().rss/2**30
print(f"Training done in {train_time:.1f}s – RAM ≈ {ram:.2f} GB")

preds = kmodel.transform(clust_df)
evaluator = ClusteringEvaluator(predictionCol="prediction", featuresCol="features",
                                metricName="silhouette", distanceMeasure="squaredEuclidean")
sil = evaluator.evaluate(preds)
print("Silhouette score:", round(sil,3))
