from pyspark.sql import functions as F

service = spark.table("svc_health")

unique_service = service.agg(F.count_distinct("svc_name").alias("unique_services"))
