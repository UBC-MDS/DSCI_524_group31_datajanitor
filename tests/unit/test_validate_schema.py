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
def test_validate_schema_missing_columns():
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

    data = pd.DataFrame({"age": [1]})
    schema = {
        "age": {"type": "int"},
        "amount": {"type": "int"},
        "name": {"type": "str"},
    }

    with pytest.raises(SchemaValidationError) as excinfo:
        validate_schema(data, schema)

    assert excinfo.value.errors == {
        "amount": "Required Column 'amount' not found in data",
        "name": "Required Column 'name' not found in data",
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

# tests that there are no errors when the data is empty
def test_validate_schema_empty_dataframe():
    data = pd.DataFrame(columns=["customer", "age"])
    schema = {
        "customer": {"type": "str"},
        "age": {"type": "int"}
    }

    result = validate_schema(data, schema)
    assert result is None

# tests that there are no errors when there are extra columns in the data
def test_validate_schema_extra_columns():
    data = pd.DataFrame({
        "customer": ["Sam"],
        "age": [20],
        "purchase_amount": [1000],
        "extra_col": ["unexpected"]
    })

    schema = {
        "customer": {"type": "str"},
        "age": {"type": "int"},
        "purchase_amount": {"type": "int"},
    }

    result = validate_schema(data, schema)
    assert result is None  

# tests that an error is raised when a column has missing values
def test_validate_schema_missing_values():
    data = pd.DataFrame({
        "customer": ["Sam", None],
        "age": [20, 30],
    })

    schema = {
        "customer": {"type": "str"},
        "age": {"type": "int"},
    }

    with pytest.raises(SchemaValidationError) as excinfo:
        validate_schema(data, schema)

    assert excinfo.value.errors == {
        "customer": "Column 'customer' contains missing values."
    }

# tests that an error is raised when a numeric column has values outside the min and max bounds
def test_validate_schema_numeric_bounds():
    data = pd.DataFrame({
        "age": [-5, 20, 30],
    })

    schema = {
        "age": {"type": "int", "min": 5, "max": 100}
    }

    with pytest.raises(SchemaValidationError) as excinfo:
        validate_schema(data, schema)

    assert excinfo.value.errors == {
        "age": "Values in 'age' must be between 5 and 100."
    }

    data = pd.DataFrame({"age": [5, 100]})
    schema = {"age": {"type": "int", "min": 5, "max": 100}}

    assert validate_schema(data, schema) is None

    data = pd.DataFrame({"age": [-1, 10]})
    schema = {"age": {"type": "int", "min": 5}}

    with pytest.raises(SchemaValidationError):
        validate_schema(data, schema)
    
    data = pd.DataFrame({"age": [5, 130]})
    schema = {"age": {"type": "int", "max": 130}}

# tests that an error is raised when the schema is not a dictionary
def test_validate_schema_invalid_schema_type():
    data = pd.DataFrame({"a": [1, 2]})
    schema = [1,2]

    with pytest.raises(TypeError):
        validate_schema(data, schema)

    data = pd.DataFrame({"amount": ["10000", "11000", "120000"]})
    schema = ["apple", "pie"]

    with pytest.raises(TypeError):
        validate_schema(data, schema)

# tests that there are no errors when an optional column is not present in the data.
def test_validate_schema_optional_column_not_required():
    data = pd.DataFrame({"age": [20, 30]})
    schema = {
        "age": {"type": "int"},
        "name": {"type": "str", "required": False},
    }

    assert validate_schema(data, schema) is None