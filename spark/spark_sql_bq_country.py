import argparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract, expr

# pylint: disable=R0801

# Define command-line arguments
parser = argparse.ArgumentParser(description="Generate a hotel reviews report.")
parser.add_argument('--input_path', required=True)
parser.add_argument("--country", type=str, help="Specify a country to filter the report.")
parser.add_argument("--output", type=str, help="Report file.", required=True)

# Parse the command-line arguments
args = parser.parse_args()

# Initialize a Spark session
spark = SparkSession.builder \
    .appName('test') \
    .getOrCreate()


# Set a temporary GCS bucket for intermediate storage (if applicable)
spark.conf.set('temporaryGcsBucket', 'dataproc-temp-europe-west6-509013154381-b69h2glg')


# Get the input path from command-line arguments
input_path = args.input_path

# Read Parquet data into a DataFrame
df = spark.read.parquet(f"{input_path}")


# # Data Transformation
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


# Execute the query to generate the report DataFrame
report_df = spark.sql(report_query)

# Get the output path from command-line arguments
output = args.output

# Write the report DataFrame to BigQuery
report_df.write.format('bigquery') \
    .option('table', f"{output}") \
    .save()


