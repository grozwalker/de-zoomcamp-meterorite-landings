terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.21.0"
    }
  }
}

provider "google" {
  credentials = file(var.credential_file)
  project     = var.project_id
  region      = var.region
  zone        = var.zone
}
