from pyspark.sql import functions as F

logs = spark.table("err_tracks")

err_logs = logs.filter(F.col("svc_name") == "payment-api")
               .groupBy("err_type")
               .agg(F.count("err_id").alias("err_count")
                  )
               .filter(F.col("err_count") > 6)
               .drop("err_count")
