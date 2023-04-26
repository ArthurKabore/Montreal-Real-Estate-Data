from pyspark.sql.functions import round
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Create a SparkSession object
spark = SparkSession.builder.appName("CSV Data").getOrCreate()

# Load the CSV file into a DataFrame
df = spark.read.csv("Outputs/snow_data.csv", header=False, inferSchema=True)

# Rename the columns of the DataFrame
df = df.withColumnRenamed("_c0", "Neighborhood") \
       .withColumnRenamed("_c1", "Rooms") \
       .withColumnRenamed("_c2", "Bedrooms") \
       .withColumnRenamed("_c3", "Bathrooms") \
       .withColumnRenamed("_c4", "Price") \
       .withColumnRenamed("_c5", "Sqft") \
       .withColumnRenamed("_c6", "Year")

# Show the first 5 rows of the DataFrame
df.show(1)

# Group the "Rooms" column and compute the average "Price" for each group
avg_price_df = df.groupBy("Year").avg("Price")

# Round the average price to the nearest integer
avg_price_df = avg_price_df.withColumn("avg(Price)", round(avg_price_df["avg(Price)"]))
avg_price_df = avg_price_df.orderBy("avg(Price)", ascending=False)

price_per_sqft_df = df.groupBy("Neighborhood").agg(round(avg("Price") / avg("Sqft"), 2).alias("Price per Sqft"))
price_per_sqft_df = price_per_sqft_df.orderBy("Price per Sqft", ascending=False)

price_per_sqft_df.show(n=100)

# Show the average price for each number of rooms
avg_price_df.show(n=100)
