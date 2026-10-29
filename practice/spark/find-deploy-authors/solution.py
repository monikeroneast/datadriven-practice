from pyspark.sql import functions as F

logs = spark.table("deploy_logs")

result = (logs.filter((F.lower("author") == "alice") | 
                     (F.lower("author") == "bob")) \
              .select("author") \
              .distinct()
        )
