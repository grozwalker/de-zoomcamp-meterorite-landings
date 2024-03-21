resource "google_bigquery_dataset" "raw_data" {
  dataset_id  = var.dataset_id
  description = var.dataset_description
  location    = var.resource_location
}

resource "google_storage_bucket" "meteorite_landings" {
  name     = "${var.project_id}-${var.bucket_name}"
  location = var.region

  uniform_bucket_level_access = true
}
