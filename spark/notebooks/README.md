
To upload to the bucket

gsutil -m cp -r C:\Users\bmart\OneDrive\12_Data_Engineering\de-hotel-reviews\data\spark\* gs://de-hotel-reviews/spark-data/

Then we download the hadoop connector gcs-connector-hadoop3-2.2.15


run  
python .\spark_sql_all.py for whole report

python .\spark_sql_country.py  --country UK for country report

Then create a Dataproc cluster


Upload the files to create the job

gsutil cp .\spark_sql_bq_all.py gs://de-hotel-reviews/scripts/

gsutil cp .\spark_sql_bq_country.py gs://de-hotel-reviews/scripts/


--input_path=gs://de-hotel-reviews/spark-data/hotel_reviews_spark.parquet/hotel_reviews_spark.parquet/
--output=gs://de-hotel-reviews/spark-data/spark_report

gcloud dataproc jobs submit pyspark --cluster=reviews-hotel --region=europe-west6 --jars=gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar gs://de-hotel-reviews/scripts/spark_sql_bq_all.py -- -- --input_path=gs://de-hotel-reviews/spark-data/hotel_reviews_spark.parquet/ --output=hotels_all.spark_report


gcloud dataproc jobs submit pyspark --cluster=reviews-hotel --region=europe-west6 --jars=gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar gs://de-hotel-reviews/scripts/spark_sql_bq_country.py -- -- --input_path=gs://de-hotel-reviews/spark-data/hotel_reviews_spark.parquet/ --country UK --output=hotels_all.spark_report_UK