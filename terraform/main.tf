resource "google_bigquery_dataset" "raw_data" {
  dataset_id  = var.dataset_raw_data.id
  description = var.dataset_raw_data.description
  location    = var.resource_location
}

resource "google_bigquery_dataset" "raw_data_data_marts" {
  dataset_id  = var.dataset_raw_data_data_marts.id
  description = var.dataset_raw_data_data_marts.description
  location    = var.resource_location
}

resource "google_storage_bucket" "meteorite_landings" {
  name     = "${var.project_id}-${var.bucket_name}"
  location = var.region

  uniform_bucket_level_access = true
}

resource "google_storage_bucket" "meteorite_landings_tmp" {
  name     = "${var.project_id}-${var.tmp_bucket_name}"
  location = var.region

  uniform_bucket_level_access = true
}
