import pandas as pd
import numpy as np
import pytest

from datajanitor.detect_outliers import detect_outliers

def test_detect_outliers_empty_df():
    empty_df = pd.DataFrame()
    result = detect_outliers(empty_df)
    assert result == empty_df

def test_detect_outliers_iqr_logic():
    data = {'val': [11, 12, 13, 14, 100]}  # 100 is a clear outlier
    df = pd.DataFrame(data)
    
    result = detect_outliers(df, multiplier=1.5, method="iqr", columns="all")
    
    assert len(result) == 4
    assert 100 not in result['val'].values
    assert isinstance(result, pd.DataFrame)

def test_detect_outliers_zscore_logic():
    data = {'val': [-9.5, 10.0, 10.5, 11.0, 50]} 
    df = pd.DataFrame(data)
    
    result = detect_outliers(df, multiplier=3.0, method="zscore", columns="all")
    
    assert result == df
    assert 50 not in result['val'].values

def test_detect_outliers_column_names():
    data = {'A': [1, 2, 1, 2, 1],      # Clean column
            'B': [1, 2, 1, 2, 100]    # Outlier at index 4}
    df = pd.DataFrame(data)
    
    # Check column A
    result = detect_outliers(df, columns = ['A'])
    assert result == df
    
    # Check all columns
    result = detect_outliers(df, columns = "all")
    assert len(result) == 4
    assert 100 not in result['B'].values

def test_detect_outliers_invalid_type():
    with pytest.raises(TypeError):
         detect_outliers([1, 2, 3, 100], method = "iqr")

def test_detect_outliers_invalid_method():
    df = pd.DataFrame({'val': [1, 2, 3]})
    
    with pytest.raises(ValueError):
         detect_outliers(df, method = "random_guess")
