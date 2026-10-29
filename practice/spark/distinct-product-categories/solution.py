from pyspark.sql import functions as F

prod = spark.table("products")

result = (prod.select("category") \
              .distinct()
        )
