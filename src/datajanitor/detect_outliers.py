def detect_outliers(df, multiplier: 1.5):
    """
    Detect and remove outliers in the df DataFrame using the interquartile range

    Parameters
    ----------
    df : pd.DataFrame
        A pandas DataFrame
    multiplier: float
        The multiplier for the interquartile range. Default is 1.5

    Returns
    -------
    A pandas DataFrame which is df with outliers removed according to the multiplier
    """
