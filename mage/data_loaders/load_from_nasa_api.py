import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://data.nasa.gov/resource/gh4g-9sfh.csv'
    data_chunks=[]
    processing = True
    offset = 0
    limit = 5000

    print('Downloading data from NASA')

    while processing:
        print('.'),
        chunk = pd.read_csv(f'{url}?$offset={offset}&$limit={limit}', sep=',')

        if chunk.empty:
            processing = False
        else:
            data_chunks.append(chunk)
            offset += limit

    print('Data downloaded')

    result = pd.concat(data_chunks)

    return result


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
