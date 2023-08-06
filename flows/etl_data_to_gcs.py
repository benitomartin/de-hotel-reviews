import os
import pandas as pd
from dotenv import load_dotenv
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket

# Load environment variables from a .env file
load_dotenv()

# Define a Prefect task for cleaning the dataset
@task(retries=3, log_prints=True)
def clean(dataset_file: str) -> pd.DataFrame:
    """
    Clean the dataset by removing duplicate rows and rows with missing values.
    
    Args:
        dataset_file (str): Path to the CSV file containing the dataset.
        
    Returns:
        pd.DataFrame: Cleaned pandas DataFrame.
    """
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(dataset_file)

    # Convert 'Review_Date' column to datetime
    df["Review_Date"] = pd.to_datetime(df["Review_Date"])

    # Print data type of the 'Review_Date' column
    print(f'Dtype is: {df[["Review_Date"]].dtypes}')

    print(f'Nr. Rows before cleaning: {len(df)}')

    # Drop duplicate rows and rows with missing values
    df = df.drop_duplicates()
    df = df.dropna()

    print(f'Nr. Rows after cleaning: {len(df)}')

    return df  # Return the cleaned DataFrame

# Define a Prefect task to upload Parquet file to GCS
@task(retries=3, log_prints=True)
def write_gcs(prefect_block: str, parquet_path: str, parquet_file: str) -> None:
    """
    Upload a local Parquet file to Google Cloud Storage (GCS) bucket.
    
    Args:
        prefect_block (str): The identifier for the Prefect GCS block.
        parquet_path (str): Local path to the Parquet file.
        parquet_file (str): Name of the Parquet file.
    """
    try:
        # Load the GCS bucket using the provided PREFECT_BLOCK
        gcs_block = GcsBucket.load(prefect_block)
        print(f'Loaded GCS Bucket: {gcs_block.bucket}')

        # Upload the Parquet file to the GCS bucket
        gcs_block.upload_from_path(from_path=parquet_path, to_path=f'data/{parquet_file}')

        print("File uploaded!")

    except Exception as err:
        print(f"An error occurred during GCS upload: {err}")
        raise err  # Re-raise the exception to trigger Prefect retries

    return

# Define a Prefect flow for the ETL (Extract, Transform, Load) process
@flow
def etl_to_gcs():
    """
    Prefect flow for performing ETL from CSV to Parquet and uploading to GCS.
    """
    # Get the path to the CSV file from environment variables
    CSV_PATH = os.getenv("CSV_PATH")

    # Get the path for the output Parquet file from environment variables
    PARQUET_PATH = os.getenv("PARQUET_PATH")

    # Call the 'clean' task with the CSV file path
    cleaned_df = clean(CSV_PATH)

    # Convert the cleaned DataFrame to Parquet format with Brotli compression
    cleaned_df.to_parquet(PARQUET_PATH, compression="brotli")

    # Get the PREFECT_BLOCK from environment variables
    PREFECT_BLOCK = os.getenv("PREFECT_BLOCK")
    PARQUET_FILE = os.getenv("PARQUET_FILE")

    # Call the 'write_gcs' task to upload the Parquet file to GCS
    write_gcs(PREFECT_BLOCK, PARQUET_PATH, PARQUET_FILE)

if __name__ == "__main__":
    # Execute the Prefect flow
    etl_to_gcs()
