import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here
    google_project_id = os.environ.get('GOOGLE_PROJECT')

    spark = kwargs.get('spark')
    spark._jsc.hadoopConfiguration().set("google.cloud.auth.service.account.json.keyfile","/home/src/personal-gcp.json")
    spark._jsc.hadoopConfiguration().set('fs.gs.impl', 'com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem')

    landings = spark.read.parquet('tmp/raw/pq-transformed/*')

    landings.write.format('bigquery') \
      .mode('overwrite') \
      .option("temporaryGcsBucket",f"{google_project_id}-meteorite-landings-tmp") \
      .option("credentialsFile", "/home/src/personal-gcp.json") \
      .option("parentProject", google_project_id) \
      .option('table', 'raw_data_data_marts.meteorite_landings_spark') \
      .save()
