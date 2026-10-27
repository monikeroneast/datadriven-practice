df_year = cloud_costs.withColumn("fiscal_year", F.year(F.to_date("bill_date")))

df_agg = df_year.groupBy("fiscal_year") \
  .agg(F.round(F.sum(F.col("amount")), 3).alias("total_spend"),
       F.countDistinct(F.col("svc_name")).alias("service_count")
)

df_agg.orderBy("fiscal_year")
