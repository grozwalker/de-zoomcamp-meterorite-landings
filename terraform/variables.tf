variable "credential_file" {
  type        = string
  description = "Path to Service account credential file"
  default     = "../key/gcp-service-account.json"
}

variable "project_id" {
  type        = string
  description = "Google Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region"
  default     = "europe-west3"
}

variable "zone" {
  type        = string
  description = "GCP Zone"
  default     = "europe-west3-a"
}

variable "dataset_raw_data" {
  type        = map(string)
  description = "Info about dataset raw_data"
  default = {
    "id"          = "raw_data"
    "description" = "Dataset for meteorite raw data"
  }
}

variable "dataset_raw_data_data_marts" {
  type        = map(string)
  description = "Info about dataset raw_data_data_marts"
  default = {
    "id"          = "raw_data_data_marts"
    "description" = "Dataset for meteorite raw data data marts"
  }
}

variable "resource_location" {
  type        = string
  description = "Dataset location"
  default     = "EU"
}

variable "bucket_name" {
  type        = string
  description = "GSB name"
  default     = "meteorite-landings"
}
