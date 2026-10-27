df_filter = repo_commits.filter(
    F.lower(F.col("repo_name")).contains("data") &
    (F.col("repo_name") != "analytics")
  )
df_filter1 = df_filter.select("repo_name", "author", "message")
df = df_filter1.filter(F.lower(F.col("message")).contains("fix"))
df_group = df.groupBy("repo_name", "author")
df_agg = df_group.agg(F.count("message").alias("fix_count"))
df_final = df_agg.orderBy(F.col("fix_count").desc())
