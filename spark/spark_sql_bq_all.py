
import argparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract, expr



# Define command-line arguments
parser = argparse.ArgumentParser(description="Generate a hotel reviews report.")
parser.add_argument('--input_path', required=True)
parser.add_argument("--output", type=str, help="Report file.", required=True)

# Parse the command-line arguments
args = parser.parse_args()

spark = SparkSession.builder \
    .appName('test') \
    .getOrCreate()

spark.conf.set('temporaryGcsBucket', 'dataproc-temp-europe-west6-509013154381-b69h2glg')

input_path = args.input_path


df = spark.read.parquet(f"{input_path}")


# 1) Transform 'United Kingdom' to 'UK' in the 'Hotel_Address' column
df = df.withColumn('Hotel_Address', expr("regexp_replace(Hotel_Address, 'United Kingdom', 'UK')"))

# 2) Get the last word of each row and create a new 'Hotel_Country' column
df = df.withColumn('Hotel_Country', regexp_extract(df['Hotel_Address'], r'\b(\w+)$', 1))

df_selected = df.select('Hotel_Address', 'Hotel_Country', "Hotel_Name", "Review_Date",
                        "Average_Score", "Reviewer_Nationality", "Reviewer_Score")

# Register the DataFrame as a temporary SQL table
df_selected.createOrReplaceTempView("hotel_reviews")

# Define the Spark SQL query
report_query = """
                SELECT
                    Hotel_Country,
                    Hotel_Name,
                    FORMAT_NUMBER(AVG(Reviewer_Score), 2) AS Avg_Reviewer_Score
                FROM
                    hotel_reviews
                GROUP BY
                    Hotel_Country, Hotel_Name
                ORDER BY
                    Hotel_Country, Avg_Reviewer_Score DESC
"""

# Execute the query
report_df = spark.sql(report_query)

output = args.output

report_df.write.format('bigquery') \
    .option('table', output) \
    .save()
    
