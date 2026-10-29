from pyspark.sql import functions as F

pods = spark.table("k8s_pods")

result = pods.filter((F.col("status") == "Error") |
                      (F.col("status") == "CrashLoopBackOff")) \
              .groupBy("nspace") \
              .agg(F.count("*").alias("failing_count")) \
              .filter(F.col("failing_count") > 12) \
              .select("nspace", "failing_count")
