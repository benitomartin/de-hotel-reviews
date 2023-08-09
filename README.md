# Data Engineering Hotel Reviews

![dataset-cover](https://github.com/benitomartin/templates/assets/116911431/88d28c42-a2c8-4632-90c5-f95b57bc0004)

The dataset used for this project has been downloaded from [Kaggle](https://www.kaggle.com/datasets/hellbuoy/car-price-prediction) and a preliminary data analysis was performed (see [notebooks](https://github.com/benitomartin/de-hotel-reviews/tree/main/notebooks) folder), to get some insights for the further project development.

Below you can find some instructions to understand the project content. Feel free to clone this repo :wink:

## Tech Stack

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

## Technologies and Tools

- Cloud - **Google Cloud Platform**
- Infrastructure as Code software (IaC) - **Terraform**
- Containerization - [**Docker**](https://www.docker.com), [**Docker Compose**](https://docs.docker.com/compose/)
- Workflow Orchestration - [**Airflow**](https://airflow.apache.org)
- Batch processing - [**Apache Spark**](https://spark.apache.org/), [**PySpark**](https://spark.apache.org/docs/latest/api/python/)
- Data Lake - [**Google Cloud Storage**](https://cloud.google.com/storage)
- Data Warehouse - [**BigQuery**](https://cloud.google.com/bigquery)
- Data Visualization - [**Looker Studio (Google Data Studio)**](https://lookerstudio.google.com/overview?)
- Language - [**Python**](https://www.python.org)

- Cloud: <span style='color: red;'>***GCP***</span>
- Infrastructure as code (IaC): ***Terraform***
- Workflow orchestration: ***Prefect***
- Data Warehouse: ***BigQuery***
- Batch processing: ***Spark***
- Data Transformation: ***dbt-core***
- Data Visualization: ***Looker Studio***
- Software Building Automation Tool: ***Make***
- Virtual Environment: ***Anaconda***
- CICD: ***Git***

### Project infrastructure modules in GCP

* Google Cloud Storage (GCS): Data Lake
- BigQuery: Data Warehouse

### Initial Setup

For this course, we'll use a free version (upto EUR 300 credits).

1. Create an account with your Google email ID
2. Setup your first [project](https://console.cloud.google.com/) if you haven't already
    - eg. "DTC DE Course", and note down the "Project ID" (we'll use this later when deploying infra with TF)
3. Setup [service account & authentication](https://cloud.google.com/docs/authentication/getting-started) for this project
    - Grant `Viewer` role to begin with.
    - Download service-account-keys (.json) for auth.
4. Download [SDK](https://cloud.google.com/sdk/docs/quickstart) for local setup
5. Set environment variable to point to your downloaded GCP keys:

   ```shell
   conda install -c conda-forge google-cloud-sdk
   $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\bmart\Downloads\de-course-394517-9a428abdb6c2.json"
   export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"
   
   # Refresh token/session, and verify authentication
   gcloud auth application-default login
   ```

### Setup for Access

1. [IAM Roles](https://cloud.google.com/storage/docs/access-control/iam-roles) for Service account:
   - Go to the *IAM* section of *IAM & Admin* <https://console.cloud.google.com/iam-admin/iam>
   - Click the *Edit principal* icon for your service account.
   - Add these roles in addition to *Viewer* : **Storage Admin** + **Storage Object Admin** + **BigQuery Admin**

2. Enable these APIs for your project:
   - <https://console.cloud.google.com/apis/library/iam.googleapis.com>
   - <https://console.cloud.google.com/apis/library/iamcredentials.googleapis.com>

3. Please ensure `GOOGLE_APPLICATION_CREDENTIALS` env-var is set.

   ```shell
   export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"
   ```

IAM Roles:
    BigQuery Admin
    Dataproc Administrator
    Storage Admin
    Storage Object Admin
    Viewer

### Terraform Workshop to create GCP Infra

Continue [here](./terraform): `week_1_basics_n_setup/1_terraform_gcp/terraform`
