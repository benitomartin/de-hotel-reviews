# Prefect Workflow Orchestration

A GCS Bucket must be available in GCS to run this code.

Then create prefect block with the following configuration:

- Name of the Bucket: your GCS Bucket
- Add GCS credentials of the service account of your GCS Bucket

To upload the data to the GCS Bucket and send them to BigQuery follow the net steps:

1. Start Prefect Server:

   ```bash
   prefect server start
   ```

2. Upload the files to the GCS Bucket:

   ```bash
   python .\etl_data_to_gcs.py 
   ```

3. Send the data to BigQuery:

    ```bash
     python .\etl_gcs_to_bq.py
    ```
