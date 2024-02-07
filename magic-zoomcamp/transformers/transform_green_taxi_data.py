import re


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def remove_rows_with_zero_passengers(data, *args, **kwargs):
    print(data['VendorID'].unique())
    print(f'Preprocessing: removing rows with 0 passengers: {len(data[data["passenger_count"] == 0])}')
    print(f'Preprocessing: removing rows with zero trip_distance: {len(data[data["trip_distance"] == 0])}')
    data = data[(data["passenger_count"] != 0) & (data['trip_distance'] != 0
    print(f'Preprocessing: adding lpep_pickup_date column')
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    print(f'Preprocessing: renaming column names from CamelCase to snake_case')
    data.rename(columns=lambda x: re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', x).lower(), inplace=True)
    print(data['vendor_id'].unique())
    return data


@test
def test_output_column_names(output, *args) -> None:
    assert 'vendor_id' in output.columns, f'There is no column with name vendor_id'

@test
def test_output_zero_passengers(output, *args) -> None:
    assert len(output[output["passenger_count"] == 0]) == 0, f'There are passengers with 0 rides'

@test
def test_output_zero_trip_distance(output, *args) -> None:
    assert len(output[output["trip_distance"] == 0]) == 0, f'There are passengers with trip_distance = 0'
