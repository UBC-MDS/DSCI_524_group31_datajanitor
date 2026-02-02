# Welcome to datajanitor

|  |  |
|----|----|
| Package | [![Latest TestPyPI Version](https://img.shields.io/badge/dynamic/json?label=TestPyPI&query=info.version&url=https%3A%2F%2Ftest.pypi.org%2Fpypi%2Fdatajanitor%2Fjson)](https://test.pypi.org/project/datajanitor/) [![Supported Python Versions](https://img.shields.io/badge/python-3.9+-blue)](https://test.pypi.org/project/datajanitor/) |
| Meta | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

## Project Outline

### Data janitor

[`Datajanitor`](https://ubc-mds.github.io/DSCI_524_group31_datajanitor/README.html) is a Python package that focuses on basic data cleaning and validation tasks for tabular data, mainly pandas DataFrames. The goal is to make common cleaning steps easier and clearer than writing everything manually in pandas, especially by providing simple function interfaces and clearer error messages.

### Functions
This package contains four main functions:

#### `standardize_columns()`

##### Description
    Cleans column names by making them consistent (for example, removing extra spaces, converting to lowercase, and replacing spaces with underscores). This helps avoid bugs caused by inconsistent column naming.

##### Input
`df` (pandas.DataFrame): DataFrame with column names to standardize.

##### Output
`pandas.DataFrame`: New DataFrame with standardized column names.


#### `missing_value_handler()`

##### Descriptio
    Handles missing values in a DataFrame using simple strategies such as dropping rows or columns, or filling missing values with a constant or summary statistic like the mean or median.

##### Input
- `df` (pandas.DataFrame): DataFrame containing missing values.
- `strategy` (str): Strategy for filling missing values (e.g., "drop", "mean", "median", "constant").
- `fill_value` (any, optional): Value to fill when strategy="constant".
- `drop_na` (list[str], optional): Columns to drop if they contain missing values.

##### Output
`pandas.DataFrame`: Cleaned DataFrame with missing values handled.

#### `validate_schema()`

##### Description
    Checks whether a DataFrame follows an expected structure, such as having required columns, correct data types, and values within reasonable ranges. If something does not match, the function raises clear errors.

##### Input
- `df` (pandas.DataFrame): DataFrame to validate.
- `schema` (dict): Expected structure in the form {column_name: data_type}.

##### Output
- `bool`: Returns True if validation passes.
- Raises ValueError if the schema does not match.


#### `detect_outliers()`

##### Description
    Identifies potential outliers in numeric columns of a dataframe using a rule-based approach and returns a dataframe with removal of rows containing outliers.

##### Input
- `df` (pandas.DataFrame): DataFrame to check for outliers.
- `columns` (list[str]): Numeric columns to inspect.
- `method` (str, optional): Outlier detection method (e.g., "IQR").

##### Output
`pandas.DataFrame`: DataFrame with outlier rows removed.


NOTE: This package includes no built-in datasets, and all functionality relies on inputs provided by the user.

### Dependencies
`Datajanitor` depends on the following:
- `Python` 3.10 or later
- `Pandas` for data manipulation and tabular display of schedules and tasks
- `pip` for installation and dependency management


### How to use `Datajanitor`

<!-- You can install this package into your preferred Python environment using pip:

``` bash
$ pip install datajanitor
``` -->
#### Installation
To install the latest release from Test PyPi: 
``` bash
pip install -i https://test.pypi.org/simple/ datajanitor
```

#### Example usage

Below is a simple example demonstrating how to use one of the package functions.
<!-- 
``` python
import pandas as pd
from datajanitor.standard_columns import standardize_columns

df = pd.DataFrame({" First Name ": [1], "AGE": [20]})
out = standardize_columns(df)

out.columns.tolist()
``` -->


```python
import pandas as pd

from datajanitor.standard_columns import standardize_columns
from datajanitor.missing_values import missing_value_handler
from datajanitor.schema_validation import validate_schema
from datajanitor.outliers import detect_outliers


# ----------------------------
# 1. Create Sample Data
# ----------------------------
df = pd.DataFrame({
    " First Name ": ["Alice", "Bob", "Charlie", None, "Eve", "Frank"],
    "AGE": [25, 30, 120, 28, 35, 27],
    "Salary ": [50000, None, 70000, 52000, 48000, 600000],
    "Department": ["HR", "IT", "Finance", "IT", None, "Finance"]
})

print("Original DataFrame:")
print(df)
print("\n")
```

##### Step 1: Standardize Column Names
```python
df = standardize_columns(df)
print("After Standardizing Columns:")
print(df.columns.tolist())
print(df.head())
print("\n")

```

##### Step 2: Handle Missing Values
```python
df = missing_value_handler(
    df,
    strategy="mean",             # Fill numeric columns with mean
    drop_na=["department"],      # Drop rows where department is missing
    fill_value={"first_name": "Unknown"}  # Fill missing names
)

print("After Handling Missing Values:")
print(df)
print("\n")

```

##### Step 3: Validate Schema
```python
expected_schema = {
    "first_name": str,
    "age": int,
    "salary": float,
    "department": str
}

validate_schema(df, expected_schema)
print("Schema validation passed!")
print("\n")

```

##### Step 4: Detect and Remove Outliers
```python
clean_df = detect_outliers(
    df,
    columns=["age", "salary"],
    method="IQR"  # Example method
)

print("After Removing Outliers:")
print(clean_df)
print("\n")

```

##### Final Output
```python
print("Cleaned DataFrame ready for analysis:")
print(clean_df)

```

### Development and Documentation Guide

This section provides instructions for collaborators on how to set up the development environment, install the package, run tests, and build and deploy documentation.

#### Clone the repository

Clone the repository and move into the project directory:

``` bash
$ git clone <https://github.com/UBC-MDS/DSCI_524_group31_datajanitor.git> 
$ cd DSCI_524_group31_datajanitor
```

#### Set up the development environment

The development environment is defined in `environment.yml`.

``` bash
conda env create -f environment.yml
conda activate datajanitor
```

#### Installation
Install the package in editable mode from the repository root:

``` bash
pip install -e .
```

#### Run tests

Run the full test suite using pytest:

``` bash
pytest
```

#### Build documentation

Documentation is built using [Quarto](https://quarto.org/) with [quartodoc](https://machow.github.io/quartodoc/) using Hatch:

The documentation is built using Quarto and quartodoc through Hatch.

##### Install the Quarto CLI:
``` bash
pip install quarto-cli
```

##### To preview the documentation locally with live reload:
``` bash
hatch run docs:serve
```

##### Build and render the documentation:
``` bash
hatch run docs:build
```

The generated documentation will be in the docs/ directory.


#### Deploy documentation (automated)

This project uses GitHub Actions for continuous integration and deployment.

Runs on pushes and pull requests to the main branch to build the Quartodoc API reference, render the Quarto site, and publish it to GitHub Pages via the [gh-pages](https://github.com/UBC-MDS/DSCI_524_group31_datajanitor/tree/gh-pages) branch



### Test Files

-   `test_detect_outliers.py`\
    This file contains various tests that check detect_outliers() functionality. Testing includes verifying outlier removal using IQR and Z-score methods, column selection behavior, and error handling for invalid inputs and parameters.

-   `test_missing_value_handler.py`\
    This file contains various tests that check missing_value_handler() functionality. Testing includes verifying correct handling of missing values, unsupported methods, and edge cases such as empty DataFrames and columns with all missing values.

-   `test_standard_columns.py`\
    This file contains various tests that check standardize_columns() functionality. Testing includes verifying correct column name cleaning behavior, handling of edge cases, and proper error raising for invalid inputs.

-   `test_validate_schema.py`\
    This file contains various tests that check validate_schema() functionality. Testing includes verifying error output, missing value/column checks, numerical out of bounds validation as well as various other use case instances.

### Relation to the Python ecosystem

Some existing Python packages provide similar functionality. For example, `pandera` allows users to define and validate schemas for pandas DataFrames. Outlier detection methods are also available in `scikit-learn`, which includes more advanced algorithms.\
Compared to these tools, this package is intentionally lightweight and simpler. It is designed for small projects, assignments, or quick checks where a full validation framework would be unnecessary or too complex.


### Contributors

Group 31: 
- `Karan Partap Bains` [@karanbayns](https://github.com/karanbayns) karanb18@student.ubc.ca

- `Yasaman Eftekharypour` [@yasi44](https://github.com/yasi44) yasimailak@gmail.com

- `Sameel Syed` [@SamSyed12](https://github.com/SamSyed12) sameel12@student.ubc.ca

- `Yuting Ji` [@YutingJi894](https://github.com/YutingJi894) yutingj894@gmail.com

### Copyright

-   Copyright © 2026 Karan Bains, Yasaman Eftekharypour, Sameel Syed, Yuting Ji.
-   Free software distributed under the [MIT License](./LICENSE).
