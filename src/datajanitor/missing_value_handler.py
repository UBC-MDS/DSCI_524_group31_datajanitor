import pandas as pd


def missing_value_handler(data, method="mean"):
    """
    Handle missing values in a dataset using a specified method.

    This function processes missing values (e.g., NaN or None) in a dataset
    by either removing rows with missing values or replacing missing values
    using a simple imputation rule.

    Parameters
    ----------
    data : pandas.DataFrame
        Input dataset containing missing values.

    method : str, default="mean"
        Method used to handle missing values. Supported methods are:
        - "drop": Remove all rows that contain at least one missing value.
        - "mean": Replace missing values with the column mean (numeric columns only).
        - "median": Replace missing values with the column median (numeric columns only).
        - "mode": Replace missing values with the column mode.

    Returns
    -------
    cleaned_data : pandas.DataFrame
        A copy of the dataset with missing values handled according to the
        specified method.

    Raises
    ------
    ValueError
        If an unsupported method is provided.

    TypeError
        If the input data is not a pandas DataFrame.

    Notes
    -----
    - The original dataset is not modified.
    - Non-numeric columns are ignored for mean and median methods.
    - The function assumes missing values are represented by NaN.

    Examples
    --------
    >>> missing_value_handler(data, method="drop")
    >>> missing_value_handler(data, method="mean")
    """
    # input validation
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input data must be a pandas DataFrame")

    if not isinstance(method, str):
        raise ValueError("Method must be a string")
    
    # to avoid modifying the original data
    df = data.copy()

    if method == "drop":
        return df.dropna()

    elif method == "mean":
        return df.fillna(df.mean(numeric_only=True))

    elif method == "median":
        return df.fillna(df.median(numeric_only=True))

    elif method == "mode":
        modes = df.mode()
        if modes.empty:
            return df
        return df.fillna(modes.iloc[0])

    else:
        raise ValueError("Unsupported method")
