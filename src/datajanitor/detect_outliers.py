import pandas as pd

def detect_outliers(df, multiplier=1.5, method="iqr", columns="all"):
    """
    Identifies potential outliers in numeric columns of a DataFrame using a rule-based approach 
    (for example, the interquartile range (IQR) method) and returns a filtered DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        The input dataset containing numeric columns to be analyzed for potential outliers. 
        
    multiplier : float, default=1.5
        The coefficient used to determine the reach of the bounds or "whiskers." For example, a value of 1.5 is the standard for flagging mild outliers, 
        while 3.0 is often used for extreme outliers in IQR method.

    method : str, default="iqr"
        The statistical method to use ("iqr" or "zscore").

    columns: set, default="all"
        The set of all numeric columns to be checked for outliers. Outliers are detected in all numeric columns if columns="all".
    
    Returns
    -------
    A new pandas DataFrame with the identified outlier rows removed according to the specified method and the multiplier.

    Raises
    ------
    ValueError
        If an unsupported method is provided.

    TypeError
        If the input df is not a pandas DataFrame.

    Notes
    -----
    - The original dataset is not modified.
    - The missing values in numeric columns are ignored.

    Examples
    --------
    >>> detect_outliers(data, method="zscore")
    >>> detect_outliers(data, multiplier=3.0)
    >>> detect_outliers(data, multiplier=2.5, method="zscore")
    >>> detect_outliers(data, method="iqr", columns={"A","B"})
    """
    if not isinstance(df, pd.DataFrame):
        raise(TypeError)

    if method != "iqr" and method != "zscore":
        raise(ValueError)
        
    for c in df.columns:
        if pd.api.types.is_numeric_dtype(df[c]) and (columns=="all" or c in columns):
            if method == "iqr":
                lower_q = df[c].quantile(0.25)
                upper_q = df[c].quantile(0.75)
                iqr = upper_q-lower_q
                not_outliers = ((df[c] < upper_q+multiplier*iqr) & 
                               (df[c] > lower_q-multiplier*iqr))
                df = df[not_outliers]
            elif method == "zscore":
                mean = df[c].mean()
                std = df[c].std()
                not_outliers = ((df[c] < mean+multiplier*std) &
                                (df[c] > mean-multiplier*std))
                df = df[not_outliers]
    return df
