// Source repository: MA-BDA US Accidents team repository @ 1d55298
// Source path: notebooks/phase3/03_statistical_analysis_3_4.scala
// Selection: Grouped numeric weather summaries and weather-condition counts in SeverityWeatherAnalysis.main
// Purpose: Aggregate weather by severity with Spark DataFrames and export the reduced tables.
// Omissions: Imports, enclosing main, local preview read/casts (1,000-row limit), and Spark shutdown.

// List of numeric weather columns
val weatherCols = Seq(
  "Temperature", "Wind_Chill", "Humidity",
  "Pressure", "Visibility", "Precipitation"
)

// Prepare CSV writer for numeric stats
val statsFile = new PrintWriter("weather_by_severity.csv")
statsFile.println("feature,severity,count,mean,stddev")

weatherCols.foreach { colName =>
  val stats = df
    .filter(col(colName).isNotNull)
    .groupBy("Severity")
    .agg(
      count(colName).alias("count"),
      round(avg(colName), 2).alias("mean"),
      round(stddev(colName), 2).alias("stddev")
    )
    .orderBy("Severity")
    .collect()

  stats.foreach { row =>
    val sev   = row.getInt(0)
    val cnt   = row.getLong(1)
    val mean  = Option(row.getAs[java.lang.Double]("mean")).map(_.toDouble).getOrElse(Double.NaN)
    val sd    = Option(row.getAs[java.lang.Double]("stddev")).map(_.toDouble).getOrElse(Double.NaN)
    statsFile.println(s"$colName,$sev,$cnt,$mean,$sd")
  }
}
statsFile.close()
println("Wrote weather_by_severity.csv")

// Prepare CSV writer for Weather_Condition distribution
val distFile = new PrintWriter("weather_condition_by_severity.csv")
distFile.println("severity,weather_condition,count")

df.groupBy("Severity", "Weather_Condition")
  .agg(count("Weather_Condition").alias("count"))
  .orderBy(col("Severity"), desc("count"))
  .collect()
  .foreach { row =>
    val sev = row.getInt(0)
    val cond = row.getString(1)
    val cnt = row.getLong(2)
    distFile.println(s"$sev,$cond,$cnt")
  }
distFile.close()
println("Wrote weather_condition_by_severity.csv")
