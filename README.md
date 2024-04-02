# Meteorite landings map
Final project for data-engineer zoomcamp 2024

## About project

For my project I decided to analyse meteorites which landings to Earth with coordinates, years and other additionals params. I get data from The Meteoritical Society which contains information about all of the known meteorite landings and want to figure out in which areas meteorite fragments concentrated.

In this project, I am going to implement some data engineering best practices (partition table, pre commits hooks and others) and gain interesting metrics, such as:

* number of meteorites by year
* distribution of the number of meteorites by latitude
* distribution meteorites by types
* interactive map of meteorite landings

Go to https://lookerstudio.google.com/reporting/6c8488a2-2e39-4b79-a966-de9cba50b83c/page/lo3tD to view report

_In fact, a partitioned table is not needed for such a small amount of data, but I decided to add it to show that I can do it. Also processing with spark._

## Dataset

In this project I get Meteorite Landings from [NASA data open portal](https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data).

## Technologies

* [Mage](https://www.mage.ai/) for orchestrating workflow
* [dbt](https://www.getdbt.com/) for data transformation
* [Spark](https://spark.apache.org/) for data transformation
* [Google BigQuery](https://cloud.google.com/bigquery) for data warehousing and analysis
* [Google Looker Studio](https://lookerstudio.google.com) for dashboard
* [Terraform](https://www.terraform.io/) for provisioning BigQuery dataset
* [Docker](https://www.docker.com/) for running services on local machine


# Reproduction Step

## Prerequisites

1. A [Google Cloud Platform](https://cloud.google.com/) account
1. Docker (https://www.docker.com/get-started/)

### Create a Google Cloud Project

Go to [Manage Resource](https://console.cloud.google.com/cloud-resource-manager) page in the Google Cloud console. Click _Create Project_ and fill in the fields, after that click _Finish_.

### Enable necessary api

* [IAM API](https://console.cloud.google.com/flows/enableapi?apiid=iam.googleapis.com)
* [IAM Service Account Credentials API](https://console.cloud.google.com/apis/library/iamcredentials.googleapis.com)

### Create a Service Account and key

1. In the Google Cloud console, go to the [Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create) page
1. Select a Google Cloud project
1. Fill necessary fields
1. Add this roles: _BigQuery Admin_, _Cloud Datastore Owner_, _Cloud SQL Admin_, _Storage Admin_, _Storage Object Admin_, _Viewer_
1. Click **Done** to finish creating the service account.
1. In the Service account dashboard find just now created account and click on **Actions -> Manage keys**
1. Click on **Add key -> Create new key** and choose key type **JSON**
1. Save file as `gcp-service-account.json` and store it in your project folder, in `{project_folder}/key`.

### Create BQ infrastructure

```bash
git clone git@github.com:grozwalker/de-zoomcamp-meterorite-landings.git
cd de-zoomcamp-meterorite-landings/terraform
cp terraform.tfvars.example terraform.tfvars
# fill the variable **project_id** with the value of the project ID that you created above
terraform init
terraform apply
```


## Start project localy

In project folder run:

```bash
cp dev.env .env
nano .env # fill GOOGLE_PROJECT_ID
make build
make ingest_data
```

If you want access to mage ui run: `make ui` and open http://localhost:6789/pipelines/meteorite_landings
