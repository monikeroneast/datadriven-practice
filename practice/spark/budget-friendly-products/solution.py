df = products.filter((F.col("price") >= 5) & (F.col("price") <=20))
df_final = df.select("product_name").distinct()
