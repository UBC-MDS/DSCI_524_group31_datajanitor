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
    is_valid : bool
        True if the dataset conforms to the schema; False otherwise.

    errors : dict
        Dictionary containing schema validation errors, where keys are column
        names and values are descriptive error messages explaining the failure.

    Raises
    ------
    TypeError
        If the input data is not a pandas DataFrame.

    ValueError
        If the schema is not provided in the expected dictionary format.

    Notes
    -----
    - The function does not modify the original dataset.
    - Extra columns not specified in the schema are ignored by default.
    - Type validation is performed before range validation.
    - This function is intended for data validation, not data cleaning.

    Examples
    --------
    >>> validate_schema(data, schema)
    >>> is_valid, errors = validate_schema(data, schema)
    """
    pass