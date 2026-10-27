from pyspark.sql import functions as F

audit = spark.table("infra_nodes")

audit_summary = (audit.filter((F.lower(F.col("status")) == "draining") | (F.lower(F.col("status")) == "offline"))
                      .agg(F.countDistinct("hostname").alias("unique_hosts"))
                )
