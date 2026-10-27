from pyspark import functions as F

layout = spark.table("devices")

committed_layout = layout.filter(F.col("browser") == "Chrome")
                         .groupBy("device_type")
                         .agg(F.count("device_id").alias("chrome_users")
                            )
                          .filter(F.col("chrome_users") >= 6)
