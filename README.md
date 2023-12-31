# Data Engineering Hotel Reviews

<p>
    <img src="/images/Cover.jpg"/>
</p>

This is a personal data engineering project based on a hotel reviews [Kaggle](https://www.kaggle.com/datasets/jiashenliu/515k-hotel-reviews-data-in-europe) dataset.

Below you can find some instructions to understand the project content. Feel free to clone this repo :wink:

## Tech Stack and Tools

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C.svg?style=for-the-badge&logo=Apache-Spark&logoColor=white)
![Prefect](https://img.shields.io/badge/Prefect-024DFD.svg?style=for-the-badge&logo=Prefect&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B.svg?style=for-the-badge&logo=dbt&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Looker Studio](https://img.shields.io/badge/Looker-4285F4.svg?style=for-the-badge&logo=Looker&logoColor=white)
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

* Data Analysis & Exploration: **SQL/Python**
* Cloud: **Google Cloud Platform**
  * Data Lake - **Google Cloud Storage**
  * Data Warehouse: **BigQuery**
* Infrastructure as Code (IaC): **Terraform**
* Workflow Orchestration: **Prefect**
* Distributed Processing: **Spark**
* Data Transformation: **dbt**
* Data Visualization: **Looker Studio**
* CICD: **Git**, **dbt**

## Project Structure

The project has been structured with the following folders and files:

* `.github:` contains the CI/CD files (GitHub Actions)
* `data:` raw dataset, saved parquet files and data processed using Spark
* `dbt:` data transformation and CI/CD pipeline using dbt
* `flows:` workflow orchestration pipeline
* `images:` printouts of results
* `looker:` reports from looker studio
* `notebooks:` EDA performed at the beginning of the project to establish a baseline
* `spark:` batch processing pipeline using spark
* `terraform:` IaC stream-based pipeline infrastructure in GCP using Terraform
* `Makefile:` set of execution tasks
* `.pre-commit-config.yaml`: pre-commit configuration file
* `pre-commit.md:` readme file of the pre-commit hooks
* `pyproject.toml:` linting and formatting
* `requirements.txt:` project requirements

## Project Description

The dataset was obtained from [Kaggle](https://www.kaggle.com/datasets/jiashenliu/515k-hotel-reviews-data-in-europe) and contains various columns with hotel details and reviews of 5 countries ('Austria', 'France', 'Italy', 'Netherlands', 'Spain', 'UK'). To prepare the data an **Exploratory Data Analysis** was conducted. The following actions are performed either using pandas or spark to get a clean data set:

* Remove rows with NaN
* Remove duplicates
* Create a new column with the country name

Afterwards, some columns have been selected the final clean data are ingested to a GCP Bucket and Big Query. This is done either using **Prefect** (see [flows](./flows) folder), **dbt** (see [dbt](./dbt) folder) or **Spark** (see [spark](./spark) folder).

<h3 align="center"><i>Prefect Data Ingestion</i></h3>
&nbsp;

<p>
    <img src="/images/etl_to_gcs flow.png"/>
</p>
<p>
    <img src="/images/etl_gcs_to_bq flow.png"/>
</p>

<h3 align="center"><i>dbt Data Ingestion</i></h3>
&nbsp;

<p>
    <img src="/images/dbt build all passed.png"/>
</p>

<h3 align="center"><i>Spark Data Ingestion</i></h3>
&nbsp;

<p>
    <img src="/images/spark deployment all hotels.png"/>
</p>

## Visualization

<p>
    <img src="/images/Hotel Reviews.png"/>
</p>
<p>
    <img src="/images/Hotel Reviews France.png"/>
</p>

## CI/CD

Finally, to streamline the development process, a fully automated **CI/CD** pipeline was created using GitHub Actions and dbt as well:

<h3 align="center"><i>dbt CI/CD</i></h3>
&nbsp;

<p>
    <img src="/images/dbt build production.png"/>
</p>

<h3 align="center"><i>GitHub Actions CI/CD</i></h3>
&nbsp;

<p>
    <img src="/images/CICD Github.png"/>
</p>

## Project Set Up

The Python version used for this project is Python 3.9.

1. Clone the repo (or download it as zip):

   ```bash
   git clone https://github.com/benitomartin/de-hotel-reviews.git
   ```

2. Create the virtual environment named `main-env` using Conda with Python version 3.9:

   ```bash
   conda create -n main-env python=3.9
   conda activate main-env
   ```

3. Execute the `requirements.txt` script and install the project dependencies:

    ```bash
    pip install -r requirements.txt

    or

    make install
    ```

4. Install terraform:

   ```bash
    conda install -c conda-forge terraform
    ```

Each project folder contains a **README.md** file with instructions about how to run the code. I highly recommend creating a virtual environment for each one. Additionally, please note that a **GCP Account**, credentials, and proper **IAM** roles are necessary for the scripts to function correctly. The following IAM Roles have been used for this project:

* BigQuery Admin
* BigQuery Data Editor
* BigQuery Job User
* BigQuery User
* Dataproc Administrator
* Storage Admin
* Storage Object Admin
* Storage Object Creator
* Storage Object Viewer
* Viewer

## Best Practices

The following best practices have been implemented:

* :white_check_mark: Makefile
* :white_check_mark: CI/CD pipeline
* :white_check_mark: Linter and code formatter
* :white_check_mark: Pre-commit hooks
