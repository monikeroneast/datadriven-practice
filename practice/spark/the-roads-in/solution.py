from pyspark.sql import functions as F

traffic = spark.table("page_views")

blog_traffic = traffic.filter(F.col("page_url").contains("/blog"))
                      .select("referrer")
                      .distinct()
