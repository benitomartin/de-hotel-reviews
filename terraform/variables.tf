# Define local variables
locals {
  data_lake_bucket = "de-hotel-reviews"  # Local variable to store the name of the data lake bucket
}

# Define input variables (using variables.tf)
variable "project" {
  description = "Your GCP Project ID"  # Description for the 'project' variable
}

variable "region" {
  description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
  default = "europe-west6"  # Zurich is the default GCP region (you can change it if needed)
  type = string             # Type constraint for the 'region' variable (string)
}

variable "bucket_name" {
  description = "The name of the GC Storage Bucket. Must be globally unique."
  default = ""  
}

variable "storage_class" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default = "STANDARD"  # Default storage class is 'STANDARD'
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  type = string               # Type constraint for the 'BQ_DATASET' variable (string)
  default = "hotels_all"  # Default BigQuery dataset name is 'trips_data_all'
}
