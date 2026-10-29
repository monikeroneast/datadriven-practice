from spark.sql import functions as F

logs = spark.table("cdn_logs")

result = (logs.filter("status >= 400") \
              .select("req_path") \
              .distinct()
  )
