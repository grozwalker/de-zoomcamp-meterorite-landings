if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    spark = kwargs.get('spark')

    df_landings = spark.read.parquet('tmp/raw/pq/*')
    df_landings.createOrReplaceTempView('landings')

    landings = spark.sql("""
        SELECT
            id,
            name,
            nametype,
            recclass,
            mass,
            fall,
            reclat,
            reclong,
            concat(reclat, '-', reclong) as coordinates,
            bround(reclat, 0) as rounded_latitude,
            to_date(substring_index(year, 'T', 1)) as landing_year
        FROM
            landings
        WHERE
            to_date(substring_index(year, 'T', 1)) > '1900-01-01'
            AND reclat is not null
    """)


    landings.write.parquet('tmp/raw/pq-transformed/', mode='overwrite')

    return {}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
