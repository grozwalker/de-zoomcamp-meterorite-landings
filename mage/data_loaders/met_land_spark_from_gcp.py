
from typing import Dict
from pyspark.sql import types

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(data: Dict, *args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here

    spark = kwargs.get('spark')
    spark._jsc.hadoopConfiguration().set("google.cloud.auth.service.account.json.keyfile","/home/src/personal-gcp.json")
    spark._jsc.hadoopConfiguration().set('fs.gs.impl', 'com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem')

    path = f"gs://{data.get('bucket_name')}/{data.get('object_key')}"

    schema = types.StructType([
      types.StructField('name', types.StringType(), True),
      types.StructField('id', types.IntegerType(), True),
      types.StructField('nametype', types.StringType(), True),
      types.StructField('recclass', types.StringType(), True),
      types.StructField('mass', types.FloatType(), True),
      types.StructField('fall', types.StringType(), True),
      types.StructField('year', types.StringType(), True),
      types.StructField('reclat', types.FloatType(), True),
      types.StructField('reclong', types.FloatType(), True),
      types.StructField('geolocation', types.StringType(), True),
    ])

    df = spark.read \
      .option("header", "true") \
      .schema(schema) \
      .csv(path)

    df.write.parquet('tmp/raw/pq/', mode='overwrite')

    return {}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
