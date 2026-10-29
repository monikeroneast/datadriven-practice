from pyspark.sql import functions as F

items = spark.table("content_items")

result = (items.filter(F.col("creator_id") < 300) \
              .select("content_type") \
              .distinct()
        )
