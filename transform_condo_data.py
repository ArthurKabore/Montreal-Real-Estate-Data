from pyspark.sql import SparkSession

spark = SparkSession.builder\
          .appName("SparkByExamples.com") \
          .getOrCreate()

df = spark.read.csv("summary_data")

df.printSchema()
