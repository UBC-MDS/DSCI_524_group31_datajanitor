import pandas as pd
import numpy as np
import pytest

from datajanitor.detect_outliers import detect_outliers

def test_detect_outliers_empty_df():
    """Test that an empty DataFrame returns an empty DataFrame."""
    result = detect_outliers(pd.DataFrame())
    assert isinstance(result, pd.DataFrame) and result.empty

def test_detect_outliers_iqr_logic():
    """Test outlier detection using the interquartile range (IQR) method."""
    data = {'val': [11, 12, 13, 14, 100]}  # 100 is an outlier
    df = pd.DataFrame(data)
    
    result = detect_outliers(df, multiplier=1.5, method="iqr")
    
    assert len(result) == 4
    assert 100 not in result['val'].values
    assert isinstance(result, pd.DataFrame)

def test_detect_outliers_zscore_logic():
    """Test outlier detection using the Z-score method."""
    data = {'val': [-9.5, 10.0, 10.5, 11.0, 80.0]} # 80.0 is an outlier
    df = pd.DataFrame(data)
    
    result = detect_outliers(df, multiplier=3.0, method="zscore")
    
    assert 50 not in result['val'].values

def test_detect_outliers_column_names():
    """Test that outlier detection can be targeted to specific columns or applied to all columns."""
    data = {'A': [1, 2, 1, 2, 1],     # Clean column
            'B': [1, 2, 1, 2, 100]}   # Outlier at index 4
    df = pd.DataFrame(data)
    
    # Check column A
    result = detect_outliers(df, columns = {"A"})
    assert result.equals(df)
    
    # Check all columns
    result = detect_outliers(df, columns = "all")
    assert len(result) == 4
    assert 100 not in result['B'].values

def test_detect_outliers_invalid_df():
    """Test that providing a non-DataFrame input in df raises a TypeError."""
    with pytest.raises(TypeError):
        detect_outliers([1, 2, 3, 100], method = "iqr")

def test_detect_outliers_invalid_type_columns():
    """Test that providing a non-set and non-string input in columns raises a TypeError."""
    df = pd.DataFrame({'val': [1, 2, 3]})
    with pytest.raises(TypeError):
        detect_outliers(df, columns=1)

def test_detect_outliers_invalid_value_columns():
    """Test that providing a string other than "all" in columns raises a ValueError."""
    df = pd.DataFrame({'val': [1, 2, 3]})
    with pytest.raises(ValueError):
        detect_outliers(df, columns="none")

def test_detect_outliers_invalid_method():
    """Test that providing an invalid method raises a ValueError."""
    df = pd.DataFrame({'val': [1, 2, 3]})
    with pytest.raises(ValueError):
         detect_outliers(df, method = "random_guess")
