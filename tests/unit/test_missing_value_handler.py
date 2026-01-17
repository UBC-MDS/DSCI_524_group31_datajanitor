import pandas as pd
import numpy as np
import pytest
from datajanitor import missing_value_handler


def test_missing_value_handler_edge_cases(data):
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
    