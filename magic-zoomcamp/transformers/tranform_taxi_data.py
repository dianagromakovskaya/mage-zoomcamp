if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print(f'Preprocessing: rows with 0 passengers: {len(data[data["passenger_count"] == 0])}')

    return data[data["passenger_count"] > 0]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'


@test
def test_output_zero_passengers(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert len(output[output["passenger_count"] == 0]) == 0, f'There are passengers with 0 rides'
