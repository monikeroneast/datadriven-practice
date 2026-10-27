from pyspark.sql import functions as F

engagement = spark.table("user_sessions")

weak_engagement = engagement.groupBy("user_id")
                  .agg(F.avg("session_duration_sec").alias("avg_duration"))
                  .filter(F.col("avg_duration") < 1000)
