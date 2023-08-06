



conda install -c conda-forge terraform

Define variables.tfvars


project = "your-gcp-project-id"
bucket_name = "your-unique-bucket-name"
BQ_DATASET = "custom_dataset_name"
region = "custom-region"  

terraform init

terraform plan -var-file="vars/variables.tfvars"

terraform apply -var-file="vars/variables.tfvars"