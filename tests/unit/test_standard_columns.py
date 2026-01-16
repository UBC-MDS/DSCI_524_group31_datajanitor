import pandas as pd
import pytest

# Update this import to match your project structure
from datajanitor.standard_columns import standardize_columns

def test_standardize_columns_basic_cleaning_and_no_mutation():
    """
    Basic case:
    - spaces become underscores
    - uppercase becomes lowercase
    - leading/trailing spaces removed
    Also checks input df is NOT modified.
    """
    df = pd.DataFrame({"A Col": [1], "  B  Col  ": [2]})
    original_cols = df.columns.tolist()

    out = standardize_columns(df)

    assert out.columns.tolist() == ["a_col", "b_col"]
    assert df.columns.tolist() == original_cols
    assert out is not df 


def test_standardize_columns_whitespace_tabs_newlines():
    """
    Whitespace includes tabs and newlines.
    Multiple whitespace should become a single underscore.
    """
    df = pd.DataFrame({"A\tCol": [1], "B\nCol   Name": [2]})
    out = standardize_columns(df)

    assert out.columns.tolist() == ["a_col", "b_col_name"]


def test_standardize_columns_converts_non_string_columns_to_string():
    """
    Column names might be integers, tuples, etc.
    The function should convert them to strings before cleaning.
    """
    df = pd.DataFrame({1: [10], " Two ": [20]})
    out = standardize_columns(df)

    assert out.columns.tolist() == ["1", "two"]


def test_standardize_columns_raises_value_error_on_duplicates():
    """
    If cleaning creates duplicates, the function should raise ValueError.
    Example: "A Col" -> "a_col" collides with an existing "a_col".
    """
    df = pd.DataFrame({"A Col": [1], "a_col": [2]})

    with pytest.raises(ValueError):
        standardize_columns(df)


def test_standardize_columns_raises_type_error_for_non_dataframe():
    """
    Defensive: if input is not a DataFrame, raise TypeError.
    """
    with pytest.raises(TypeError):
        standardize_columns(["not a dataframe"])

def test_standardize_columns_empty_dataframe():
    """
    Edge case: empty DataFrame with no columns.
    The function should return a copy and not raise an error.
    """
    df = pd.DataFrame()
    out = standardize_columns(df)

    assert out.columns.tolist() == []
    assert out is not df

def test_standardize_columns_raises_value_error_for_empty_cleaned_name():
    """
    Edge case: column names that become empty after cleaning
    (e.g., only whitespace).
    This should raise ValueError because empty column names are ambiguous.
    """
    df = pd.DataFrame({"   ": [1], "valid": [2]})

    with pytest.raises(ValueError, match="empty"):
        standardize_columns(df)

def test_standardize_columns_cleans_extra_underscores_and_whitespace():
    """
    Edge case: messy column names with extra underscores and whitespace.
    The function should collapse underscores and strip leading/trailing ones.
    """
    df = pd.DataFrame({"A__  __B": [1], "  __C__  ": [2]})
    out = standardize_columns(df)

    assert out.columns.tolist() == ["a_b", "c"]
