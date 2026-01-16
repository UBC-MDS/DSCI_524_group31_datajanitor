import re
import pandas as pd

def standardize_columns(df):
    """
Cleans column names by making them consistent and predictable.

This function standardizes column names to reduce errors caused by
inconsistent naming in downstream analysis. Specifically, it:
- converts all column names to strings
- strips leading and trailing whitespace
- converts all characters to lowercase
- replaces one or more whitespace characters with underscores
- collapses multiple underscores into a single underscore
- removes leading and trailing underscores

The function returns a copy of the input DataFrame and does not modify
the original object.

Parameters
----------
df : pandas.DataFrame
    Input DataFrame whose column names will be standardized.

Returns
-------
pandas.DataFrame
    A copy of the input DataFrame with standardized column names.

Raises
------
TypeError
    If the input is not a pandas DataFrame.
ValueError
    If standardization results in duplicate column names.
"""
    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "standardize_columns expects a pandas.DataFrame as input."
        )

    if df.shape[1] == 0:
        raise ValueError(
            "standardize_columns does not accept an empty DataFrame with no columns."
        )
   
    def clean_column_name(name):
        """Standardize a single column name."""
        name = str(name).strip().lower()
        name = re.sub(r"\s+", "_", name)
        name = re.sub(r"_+", "_", name)
        name = name.strip("_")
        return name

    new_columns = [clean_column_name(col) for col in df.columns]

    if any(col == "" for col in new_columns):
            raise ValueError(
                "standardize_columns produced an empty column name after cleaning."
            )
    
    if len(new_columns) != len(set(new_columns)):
        raise ValueError(
            "standardize_columns produced duplicate column names after cleaning."
        )

    # Return a copy
    df_copy = df.copy()
    df_copy.columns = new_columns
    return df_copy

