import os
import argparse
from dotenv import load_dotenv

from pyspark.sql import SparkSession, types
from pyspark.sql.functions import to_timestamp
from pyspark.sql.functions import regexp_extract, expr

# Load environment variables from a .env file
load_dotenv()

# Load the CSV data into a Spark DataFrame
CSV_PATH = os.getenv("CSV_PATH")
SPARK_PARQUET_PATH = os.getenv("SPARK_PARQUET_PATH")
SPARK_REPORT = os.getenv("SPARK_REPORT")

# Define command-line arguments
parser = argparse.ArgumentParser(description="Generate a hotel reviews report.")
parser.add_argument("--country", type=str, help="Specify a country to filter the report.")

# Parse the command-line arguments
args = parser.parse_args()

# Initialize a Spark session
spark = SparkSession.builder \
    .appName('test') \
    .getOrCreate()

# Define the schema for the DataFrame
schema = types.StructType([
                    types.StructField('Hotel_Address', types.StringType(), True),
                    types.StructField('Additional_Number_of_Scoring', types.IntegerType(), True),
                    types.StructField('Review_Date', types.StringType(), True),
                    types.StructField('Average_Score', types.DoubleType(), True),
                    types.StructField('Hotel_Name', types.StringType(), True),
                    types.StructField('Reviewer_Nationality', types.StringType(), True),
                    types.StructField('Negative_Review', types.StringType(), True),
                    types.StructField('Review_Total_Negative_Word_Counts', types.IntegerType(), True),
                    types.StructField('Total_Number_of_Reviews', types.IntegerType(), True),
                    types.StructField('Positive_Review', types.StringType(), True),
                    types.StructField('Review_Total_Positive_Word_Counts', types.IntegerType(), True),
                    types.StructField('Total_Number_of_Reviews_Reviewer_Has_Given', types.IntegerType(), True),
                    types.StructField('Reviewer_Score', types.DoubleType(), True),
                    types.StructField('Tags', types.StringType(), True),
                    types.StructField('days_since_review', types.StringType(), True),
                    types.StructField('lat', types.DoubleType(), True),
                    types.StructField('lng', types.DoubleType(), True)
])


# Read the CSV data into the DataFrame with the specified schema
df = spark.read \
    .option("header", "true") \
    .schema(schema) \
    .csv(f"{CSV_PATH}")

# Convert the 'Review_Date' column to a timestamp format
df = df.withColumn("Review_Date", to_timestamp(df["Review_Date"], "M/d/yyyy"))

# Repartition the DataFrame for better parallelism
df = df.repartition(10)


# Write the DataFrame to Parquet format for optimized storage
df.write.parquet(f"{SPARK_PARQUET_PATH}", mode = "overwrite")


# Read the Parquet data into a new DataFrame
df = spark.read.parquet(f"{SPARK_PARQUET_PATH}")

## Cleanse and transform the data
# 1) Transform 'United Kingdom' to 'UK' in the 'Hotel_Address' column
df = df.withColumn('Hotel_Address', expr("regexp_replace(Hotel_Address, 'United Kingdom', 'UK')"))

# 2) Get the last word of each row and create a new 'Hotel_Country' column
df = df.withColumn('Hotel_Country', regexp_extract(df['Hotel_Address'], r'\b(\w+)$', 1))

# Select relevant columns for the report
df_selected = df.select('Hotel_Address', 'Hotel_Country', "Hotel_Name", "Review_Date",
                        "Average_Score", "Reviewer_Nationality", "Reviewer_Score")

# Register the DataFrame as a temporary SQL table
df_selected.createOrReplaceTempView("country_hotel_reviews")

# Get the country argument value
selected_country = args.country


# Define the Spark SQL query with optional country filtering
report_query = """
                SELECT
                    Hotel_Country,
                    Hotel_Name,
                    FORMAT_NUMBER(AVG(Reviewer_Score), 2) AS Avg_Reviewer_Score
                FROM
                    country_hotel_reviews
                {country_filter}
                GROUP BY
                    Hotel_Country, Hotel_Name
                ORDER BY
                    Hotel_Country, Avg_Reviewer_Score DESC
""".format(country_filter=f"WHERE Hotel_Country = '{selected_country}'" if selected_country else "")


# Execute the query
report_df = spark.sql(report_query)


# Coalesce the DataFrame into a single partition
report_df_single_partition = report_df.coalesce(1)

# Write the DataFrame to a Parquet file
report_df_single_partition.write.parquet(f"{SPARK_REPORT}_{selected_country}", mode='overwrite')

# Start an interactive session to check results
spark.sql(report_query).show()