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

variable "dataset_id" {
  type        = string
  description = "Dataset ID"
  default     = "raw_data"
}

variable "dataset_description" {
  type        = string
  description = "Dataset description"
  default     = "Dataset for raw data"
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
