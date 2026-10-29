from pyspark.sql import functions as F

logs = spark.table("cdn_logs")

result = (logs.filter(F.col("status") >= 400) \
              .select("req_path") \
              .distinct()
  )
