# Set the required Terraform version to 1.0 or higher
terraform {
  required_version = ">= 1.0"

  # Define the backend configuration for storing the Terraform state
  backend "local" {}  # Can change from "local" to "gcs" (for google) or "s3" (for aws), if you would like to preserve your tf-state online

  # Define the required providers and their sources
  required_providers {
    google = {
      source  = "hashicorp/google"
    }
  }
}


# Configure the Google Cloud provider
provider "google" {
  project = var.project
  region = var.region
  credentials = file(var.credentials)  # Use this if you do not want to set env-var GOOGLE_APPLICATION_CREDENTIALS
}

# Data Lake Bucket
# Ref: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket
resource "google_storage_bucket" "data-lake-bucket" {
  name          = "${local.data_lake_bucket}" # Set Name of Bucket (use the one below for more uniqueness)
  # name          = "${local.data_lake_bucket}_${var.project}" # Concatenating DL bucket & Project name for unique naming
  location      = var.region                                 # Set the location of the bucket using the 'region' variable

  # Optional, but recommended settings:
  storage_class = var.storage_class   # Set the storage class using the 'storage_class' variable
  uniform_bucket_level_access = true  # Enable uniform bucket-level access for improved security

  versioning {
    enabled     = true  # Enable versioning for the bucket
  }

  lifecycle_rule {
    action {
      type = "Delete" # Define the action to perform on objects matching the condition
    }
    condition {
      age = 30  // days   # Set the condition to delete objects older than 30 days
    }
  }

  force_destroy = true  # Allow Terraform to force destroy the bucket, even if it contains data
}

# DWH
# Ref: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_dataset
resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.BQ_DATASET   # Set the BigQuery dataset ID using the 'BQ_DATASET' variable
  project    = var.project      # Specify the GCP project ID using the 'project' variable
  location   = var.region       # Set the location of the BigQuery dataset using the 'region' variable
}
