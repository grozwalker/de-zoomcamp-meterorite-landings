# de-zoomcamp-meterorite-landings
Final project for data-engineer zoomcamp 2024


# Requirments
* pre-commit (https://pre-commit.com)


## Installation

### Pre-commit (https://pre-commit.com)
For more information view https://github.com/antonbabenko/pre-commit-terraform

For macos:
```bash
make install-pre-commit-mac
```

For linux:
```bash
make install-pre-commit-linux
```


## GCP
```bash
export GOOGLE_APPLICATION_CREDENTIALS=./key/gcp-service-account.json
```


```bash
cd terraform
cp terraform.tfvars.example terraform.tfvars
```
