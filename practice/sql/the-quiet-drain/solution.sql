from pyspark.sql import functions as F

summary = spark.table("cloud_costs")

high_cost_summary = summary.filter(F.trim((F.upper(F.col("provider"))) == "AWS") & (F.col("amount") >= 200))
                           .groupBy("region")
                           .agg(F.countDistinct("svc_name").alias("service_count"))
                           .orderBy(F.desc("service_count"), F.asc("region"))
