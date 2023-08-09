# Spark Processing

## Saving the files locally

There are two files that allow to save locally the clean dataset and a report after running a SQL Query:

- `spark_sql_all.py`
- `spark_sql_country.py`

To get a report off al countries run the "all" file:

    python .\spark_sql_all.py 

To get the report of an specific country run the "country" file and add the argument of one of the 5 countries available (Austria, France, Italy, Netherlands, Spain, UK):

    python .\spark_sql_country.py  --country UK

## Saving the files in the cloud

A GCS Bucket must be available in GCS to run this code. Change the code accordingly and add your bucket name.

There are two files that allow to save in the cloud the clean dataset and a report after running a SQL Query:

- `spark_sql_bq_all.py`
- `spark_sql_bq_country.py`

First you need to upload the files saved locally into your Bucket:

    gsutil -m cp -r C:\Users\path\to\project\de-hotel-reviews\data\spark\* gs://your-bucket/spark-data/

Then create a Dataproc Cluster in GCP with the following configuration:

- Region: same as your Bucket
- Cluster Type: Standard or Single Node are ok

Once the Dataproc Cluster is created, under GCS Buckets, two temporary buckets will be available. Add the "temp" bucket name into both python files in the following line:

    # Set a temporary GCS bucket for intermediate storage 
    spark.conf.set('temporaryGcsBucket', 'dataproc-temp-europe-west6-509134254381-b69h2glg')

Upload the python files into your GCS Bucket to create the job (not the temp one)

    gsutil cp .\spark_sql_bq_all.py gs://your-bucket/scripts/

    gsutil cp .\spark_sql_bq_country.py gs://your-bucket/scripts/

To generate the reports of all hotels and get it in BigQuery run:

    gcloud dataproc jobs submit pyspark --cluster=reviews-hotel --region=europe-west6 --jars=gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar gs://your-bucket/scripts/spark_sql_bq_all.py -- -- --input_path=gs://your-bucket/spark-data/hotel_reviews_spark.parquet/ --output=hotels_all.spark_report

To generate the reports of all hotels in a specific country and get it in BigQuery run this adding the desired country in `--country` and `--output`:

    gcloud dataproc jobs submit pyspark --cluster=reviews-hotel --region=europe-west6 --jars=gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar gs://your-bucket/scripts/spark_sql_bq_country.py -- -- --input_path=gs://your-bucket/spark-data/hotel_reviews_spark.parquet/ --country UK --output=hotels_all.spark_report_UK
