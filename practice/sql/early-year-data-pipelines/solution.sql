from pyspark.sql import functions as F

runs = spark.table("data_pipes")

bad_pipes = runs.filter(F.col("rows_out") < 0).select("pipe_name").distinct()
