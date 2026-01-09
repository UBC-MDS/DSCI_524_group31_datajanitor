def standard_scaler(df, columns=None):
    """
    Standardize numeric columns in a pandas DataFrame using z-score scaling.

    Each selected column is transformed by subtracting the column mean and
    dividing by the column standard deviation:

        z = (x - mean) / std

    This transformation rescales the data so that each column has a mean of 0
    and a standard deviation of 1.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame containing the data to be standardized.

    columns : list of str, optional
        List of column names to standardize. If None, all numeric columns
        in the DataFrame will be standardized.

    Returns
    -------
    pandas.DataFrame
        A copy of the input DataFrame with the specified columns standardized.

    Raises
    ------
    ValueError
        If any specified column does not exist in the DataFrame.
    """
    pass
