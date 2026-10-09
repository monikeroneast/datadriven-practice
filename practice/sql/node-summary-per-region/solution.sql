from pyspark.sql import functions as F

summary = spark.table("infra_nodes")

region_summary = summary.groupBy("region")
                        .agg(F.count("node_id").alias("total_nodes")
                           , F.count_distinct("node_type").alias("unique_types")
                         )
                        .orderBy(F.desc("total_nodes"), F.asc("region")
                      )
