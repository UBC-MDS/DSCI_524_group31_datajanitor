# Welcome to datajanitor

|  |  |
|------------------------------------|------------------------------------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/datajanitor.svg)](https://pypi.org/project/datajanitor/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/datajanitor.svg)](https://pypi.org/project/datajanitor/) |
| Meta | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

## Project Outline

### Data janitor

This project is a Python package that focuses on basic data cleaning and validation tasks for tabular data, mainly pandas DataFrames. The goal is to make common cleaning steps easier and clearer than writing everything manually in pandas, especially by providing simple function interfaces and clearer error messages.

### Functions

-   `standardize_columns()`\
    Cleans column names by making them consistent (for example, removing extra spaces, converting to lowercase, and replacing spaces with underscores). This helps avoid bugs caused by inconsistent column naming.

-   `missing_value_handler()`\
    Handles missing values in a DataFrame using simple strategies such as dropping rows or columns, or filling missing values with a constant or summary statistic like the mean or median.

-   `validate_schema()`\
    Checks whether a DataFrame follows an expected structure, such as having required columns, correct data types, and values within reasonable ranges. If something does not match, the function raises clear errors.

-   `detect_outliers()`\
    Identifies potential outliers in numeric columns of a dataframe using a rule-based approach and returns a dataframe with removal of rows containing outliers.

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

## Get started

You can install this package into your preferred Python environment using pip:

``` bash
$ pip install datajanitor
```

## Development and Documentation Guide

This section provides instructions for collaborators on how to set up the development environment, install the package, run tests, and build and deploy documentation.

### Clone the repository

Clone the repository and move into the project directory:

``` bash
$ git clone <https://github.com/UBC-MDS/DSCI_524_group31_datajanitor.git> 
$ cd DSCI_524_group31_datajanitor
```

### Set up the development environment

The development environment is defined in `environment.yml`.

``` bash
conda env create -f environment.yml
conda activate datajanitor
```

### Install the package

Install the package in editable mode from the repository root:

``` bash
pip install -e .
```

### Run tests

Run the full test suite using pytest:

``` bash
pytest
```

### Build documentation

Documentation is built using quartodoc.

To build the documentation locally:

``` bash
quarto render
```

To preview the documentation:

``` bash
quarto preview
```

### Deploy documentation (automated)

Documentation is built using Quarto with quartodoc for automatic API generation.

On pushes to the deployment branch (typically main), the documentation workflow builds the site and publishes it to GitHub Pages automatically.

## Example usage

Below is a simple example demonstrating how to use one of the package functions.

```python
import pandas as pd
from datajanitor.standard_columns import standardize_columns

df = pd.DataFrame({" First Name ": [1], "AGE": [20]})
out = standardize_columns(df)

out.columns.tolist()
```

## Contributors

Group 31: Karan Partap Bains, Yasaman Eftekharypour, Sameel Syed, Yuting Ji

## Copyright

-   Copyright © 2026 Karan Bains, Yasaman Eftekharypour, Sameel Syed, Yuting Ji.
-   Free software distributed under the [MIT License](./LICENSE).
