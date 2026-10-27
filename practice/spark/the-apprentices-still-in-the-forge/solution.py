from pyspark.sql import functions as F

summary = spark.table("ml_models")

mid_flight_summary = summary.filter(F.col("status") == "training")
                            .agg(F.count_distinct("mdl_name").alias("training_count"))
