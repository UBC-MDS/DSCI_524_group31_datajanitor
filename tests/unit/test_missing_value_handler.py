import pandas as pd
import numpy as np
import pytest
from datajanitor.missing_value_handler import missing_value_handler


def test_missing_value_handler_edge_cases():
    """
    Verify missing_value_handler raises correct errors
    and handles missing values properly.
    """
    
    # edge case 1: if input data is not a dataframe
    with pytest.raises(TypeError):
        missing_value_handler([1, 2, 3])
 
    df = pd.DataFrame({"A": [1, np.nan]})
    
    # edge case 2: if input method is not supported 
    with pytest.raises(ValueError):
        missing_value_handler(df, method="SomethingInvalid")
        
    # edge case 3: if input df is a empty dataframe
    empty_df = pd.DataFrame()
    result = missing_value_handler(empty_df, method="mean")
    assert result.empty
    
    # edge case 4: if all values missing in a column
    all_nan_df = pd.DataFrame({"A": [np.nan, np.nan]})
    result = missing_value_handler(all_nan_df, method="mean")
    assert result["A"].isna().all()
    
    # edge case 5: method is not a string
    with pytest.raises(ValueError):
        missing_value_handler(df, method=123)
    
    
def test_missing_value_handler_drop_method():
    """
    Test that the 'drop' method removes all rows
    containing at least one missing value.

    This test ensures that:
    - Rows with any NaN values are completely removed.
    - Only rows with no missing values remain in the result
    """
    df = pd.DataFrame({
        "A": [1, np.nan, 3],
        "B": [4, 5, np.nan]
    })

    result = missing_value_handler(df, method="drop")

    # Only the first row has no missing values
    assert len(result) == 1
    assert result.iloc[0]["A"] == 1
    assert result.iloc[0]["B"] == 4
    

def test_missing_value_handler_mean_numeric_only():
    """
    Test that the mean imputation method only fills missing values
    in numeric columns and does not affect non-numeric columns.

    This test verifies that:
    - NaN values in numeric columns are replaced with the column mean.
    - Non-numeric columns remain unchanged when using the 'mean' method.
    """
    df = pd.DataFrame({
        "A": [1.0, 2.0, np.nan],
        "B": ["x", None, "y"]
    })

    result = missing_value_handler(df, method="mean")

    assert result.loc[2, "A"] == 1.5
    assert result["B"].isna().sum() == 1
    
    
def test_missing_value_handler_median():
    """
    Test that median imputation correctly fills missing
    values in numeric columns.
    """
    df = pd.DataFrame({"A": [1, 3, np.nan]})

    result = missing_value_handler(df, method="median")

    assert result.loc[2, "A"] == 2