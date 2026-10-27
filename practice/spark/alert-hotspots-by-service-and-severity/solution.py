spark.conf.set("spark.shuffle.set.partitions", "4")

df_select = alert_events.select("svc_name", "severity", "alert_id")
df_group = df_select.groupBy("svc_name", "severity")
df_count = df_group.agg(F.count(F.col("alert_id")).alias("alert_count"))
df_order = df_count.orderBy(F.col("alert_count").desc())
