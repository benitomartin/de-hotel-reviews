import os

import pandas as pd
import pandas_gbq
from dotenv import load_dotenv
from prefect import flow, task
from prefect_gcp import GcpCredentials

# Load environment variables from a .env file
load_dotenv()


# Task to extract GCS Parquet file path
@task(retries=3, log_prints=True)
def extract_from_gcs(parquet_file: str, data_lake_bucket: str) -> str:
    """
    Task to extract the GCS Parquet file path.

    Args:
        parquet_file (str): Name of the Parquet file.
        data_lake_bucket (str): Name of the GCS bucket.

    Returns:
        str: GCS Parquet file path.
    """
    return f"gs://{data_lake_bucket}/data/{parquet_file}"


# Task to load Parquet data from GCS to BigQuery
@task(retries=3, log_prints=True)
def load_parquet_to_bigquery(
    gcs_path, project_id: str, dataset_id: str, table_id: str, credentials
):
    """
    Task to load Parquet data from GCS to BigQuery.

    Args:
        gcs_path (str): GCS path to the Parquet file.
        project_id (str): BigQuery project ID.
        dataset_id (str): BigQuery dataset ID.
        table_id (str): BigQuery table ID.
        credentials: Google Cloud credentials.

    Returns:
        None
    """
    # Read Parquet data into a DataFrame
    df = pd.read_parquet(gcs_path)

    # Construct the fully-qualified BigQuery table reference
    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    # Load the Parquet data into BigQuery using provided credentials
    pandas_gbq.to_gbq(df, destination_table=table_ref, if_exists="replace", credentials=credentials)


# Define the Prefect flow
@flow()
def etl_gcs_to_bq():
    """
    Prefect flow for extracting Parquet data from GCS and loading it into BigQuery.
    """
    # Set your GCS Parquet file path
    PARQUET_FILE = os.getenv("PARQUET_FILE")
    DATA_LAKE_BUCKET = os.getenv("DATA_LAKE_BUCKET")

    # Extract GCS Parquet file path
    parquet_gcs_path = extract_from_gcs(PARQUET_FILE, DATA_LAKE_BUCKET)

    # Load the credentials from the provided gcp_credentials_block
    PREFECT_CRED_BLOCK = os.getenv("PREFECT_CRED_BLOCK")

    gcp_credentials_block = GcpCredentials.load(PREFECT_CRED_BLOCK)
    creds = gcp_credentials_block.get_credentials_from_service_account()

    # Set your BigQuery project, dataset, and table information
    PROJECT_ID = os.getenv("PROJECT_ID")
    BQ_DATASET = os.getenv("BQ_DATASET")
    TABLE_ID = os.getenv("TABLE_ID")

    # Load the Parquet data from GCS to BigQuery using provided credentials
    load_parquet_to_bigquery(parquet_gcs_path, PROJECT_ID, BQ_DATASET, TABLE_ID, creds)


# Execute the flow if this script is run directly
if __name__ == "__main__":
    etl_gcs_to_bq()
