# IaC Terraform

The code here is the IaC for setting up in GCP an infrastructure using Terraform.

First create a `vars` folder and inside a `variables.tfvars` file with the following content:

- project = "your-project-id""
- bucket_name = "your-bucket-name"
- BQ_DATASET = "your-bq-dataset"
- region = "bucket-region"

Then follow the next steps:

- Initialize Terraform and apply the configuration:

    ```bash
    terraform init
    ```

- Plan and apply Terraform adding the absolute path:

    ```bash
    terraform plan -var-file="vars/variables.tfvars"
    ```

    ```bash
    terraform apply -var-file="vars/variables.tfvars"
    ```

This will create the required bucket and bq dataset.
