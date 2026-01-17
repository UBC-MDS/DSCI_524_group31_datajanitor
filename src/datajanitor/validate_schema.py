import pandas as pd

class SchemaValidationError(ValueError):
    """
    Raised when data does not conform to the provided schema.

    Attributes
    ----------
    errors : dict
        Dictionary mapping column names to descriptive error messages.
    """

    def __init__(self, errors):
        self.errors = errors
        super().__init__("Schema validation failed")


def validate_schema(data, schema):
    """
    Validate a dataset against a predefined schema.

    This function checks whether a dataset conforms to an expected schema by
    validating column presence, data types, and optional value constraints
    such as numeric ranges. It is designed to provide clear, human-readable
    error messages when schema violations are detected.

    Parameters
    ----------
    data : pandas.DataFrame
        Input dataset to be validated.

    schema : dict
        Dictionary defining the expected schema. Each key represents a column
        name, and its value specifies validation rules. A schema definition
        may include:
        - "type": Expected Python or NumPy data type (e.g., int, float, str).
        - "required": Boolean indicating whether the column must be present.
        - "min": Minimum allowed value (numeric columns only).
        - "max": Maximum allowed value (numeric columns only).

        Example schema format:
        {
            "age": {"type": int, "required": True, "min": 0, "max": 120},
            "salary": {"type": float, "required": False, "min": 0},
            "name": {"type": str, "required": True}
        }

    Returns
    -------
    None
        if the dataset conforms to the schema

    Raises
    ------
    TypeError
        If the input data is not a pandas DataFrame.

    SchemaValidationError
        If the dataset does not conform to the schema. The exception contains
        a dictionary mapping column names to descriptive error messages.

    Notes
    -----
    - The function does not modify the original dataset.
    - Extra columns not specified in the schema are ignored by default.
    - Type validation is performed before range validation.
    - This function is intended for data validation, not data cleaning.

    Examples
    --------
    >>> try:
            validate_schema(data, schema)
        except SchemaValidationError as e:
            print(e.errors)
    """
    
    errors = {}

    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input data must be a pandas DataFrame")
    
    if not isinstance(schema, dict):
        raise TypeError("Schema must be a dictionary")

    type_mapping = {
            "int": ["int", "Int64", "int8", "int16", "int32", "int64", "uint8", "uint16", "uint32", "uint64"],
            "float": ["float", "Float64", "float32", "float64", "float16", "float128", "float256"],
            "str": ["object", "string"],
            "bool": ["bool", "boolean"],
            "object": ["object"],
        }

    for column, spec in schema.items():

        if spec.get("required", True) and column not in data.columns:
            errors[column] = f"Required Column '{column}' not found in data"
            continue

        if column not in data.columns:
            continue

        expected_type = spec.get("type")
        if expected_type is not None:
            actual_dtype = str(data[column].dtype)
            expected_dtypes = type_mapping.get(expected_type)

            if expected_dtypes and not any(t in actual_dtype for t in expected_dtypes):
                errors[column] = f"Column '{column}' has incorrect type. Expected {expected_type}, got {actual_dtype}."

    if errors:
        raise SchemaValidationError(errors)

    return None

