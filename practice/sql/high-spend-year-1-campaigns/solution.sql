from pyspark import functions as F

campaign = spark.table("ad_impressions")

earning_campaign = campaign.withColumn("impression_year", F.substring("impression_time", 1, 4))
                        .groupBy("ad_campaign", "impression_year")
                        .agg(F.sum("revenue").alias("total_revenue")
                           , F.count_distinct("user_id").alias("unique_users")
                          )
                        .filter(F.col("total_revenue") > 5)
                        .drop("total_revenue")
