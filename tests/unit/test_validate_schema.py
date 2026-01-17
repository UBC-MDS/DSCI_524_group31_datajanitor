import pandas as pd
import pytest
from datajanitor.validate_schema import validate_schema, SchemaValidationError

# tests that an error is raised when the input data is not a pandas DataFrame
def test_validate_schema_invalid_input_type():
    data = {
        "customer": ["Sam", "Jenny"],
        "age": [20, 30]
    }
    schema = {"name": {"type": "str"}}

    with pytest.raises(TypeError) as exc_info:
        validate_schema(data, schema)
    
    assert "must be a pandas DataFrame" in str(exc_info.value)

# tests that there are no errors when the data conforms to the schema
def test_validate_schema_valid_data():
    data = pd.DataFrame({
        "customer": ["Sam", "Jenny", "Mike"],
        "age": [20, 30, 40],
        "purchase_amount": [1000, 11000, 120000],
    })

    schema = {
        "customer": {"type": "str"},
        "age": {"type": "int"},
        "purchase_amount": {"type": "int"},
    }

    result = validate_schema(data, schema)
    assert result is None

# tests that an error is raised when a column is missing from the data
def test_validate_schema_missing_column():
    data = pd.DataFrame({
        "customer": ["Sam", "Jenny", "Mike"],
        "age": [20, 30, 40],
    })

    schema = {
        "customer": {"type": "str"},
        "age": {"type": "int"},
        "purchase_amount": {"type": "int"},
    }

    with pytest.raises(SchemaValidationError) as excinfo:
        validate_schema(data, schema)

    assert excinfo.value.errors == {
        "purchase_amount": "Required Column 'purchase_amount' not found in data"
    }

# tests that an error is raised when a column has the wrong data type
def test_validate_schema_wrong_data_type():
    data = pd.DataFrame({
        "customer": ["Sam", "Jenny", "Mike"],
        "age": [20, 30, 40],
        "purchase_amount": ["10000", "11000", "120000"],
    })

    schema = {
        "customer": {"type": "str"},
        "age": {"type": "int"},
        "purchase_amount": {"type": "int"},
    }

    with pytest.raises(SchemaValidationError) as excinfo:
        validate_schema(data, schema)

    assert excinfo.value.errors == {
        "purchase_amount": "Column 'purchase_amount' has incorrect type. Expected int, got object."
    }

