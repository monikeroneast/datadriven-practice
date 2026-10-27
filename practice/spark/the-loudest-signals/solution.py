from pyspark.sql import functions as F

summary = spark.table("employee_metrics")

employee_summary = summary.select("metric_value")
                          .distinct()
                          .orderBy(F.desc("metric_value"))
                          .limit(5)
