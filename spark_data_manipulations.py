from pyspark.sql.functions import round
from pyspark.sql import SparkSession

# Create a SparkSession object
spark = SparkSession.builder.appName("CSV Data").getOrCreate()

# Load the CSV file into a DataFrame
df = spark.read.csv("Outputs/snow_data4.csv", header=False, inferSchema=True)

# Rename the columns of the DataFrame
df = df.withColumnRenamed("_c0", "Neighborhood") \
       .withColumnRenamed("_c1", "Rooms") \
       .withColumnRenamed("_c2", "Bedrooms") \
       .withColumnRenamed("_c3", "Bathrooms") \
       .withColumnRenamed("_c4", "Price") \
       .withColumnRenamed("_c5", "Year")

# Show the first 5 rows of the DataFrame
df.show(1)

# Filter the DataFrame to only keep rows where the "Neighborhood" column is "Ville-Marie"
vm_df = df.filter(df.Neighborhood == "Ville-Marie")

# Group the "Rooms" column and compute the average "Price" for each group
avg_price_df = vm_df.groupBy("Year").avg("Price")

# Round the average price to the nearest integer
avg_price_df = avg_price_df.withColumn("avg(Price)", round(avg_price_df["avg(Price)"]))
avg_price_df = avg_price_df.orderBy("avg(Price)", ascending=False)
# Show the average price for each number of rooms
avg_price_df.show(n=100)
