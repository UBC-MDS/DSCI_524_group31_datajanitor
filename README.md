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
    Identifies potential outliers in numeric columns using a simple rule-based approach and flags rows that may need further inspection.

### Relation to the Python ecosystem

Some existing Python packages provide similar functionality. For example, `pandera` allows users to define and validate schemas for pandas DataFrames. Outlier detection methods are also available in `scikit-learn`, which includes more advanced algorithms.\
Compared to these tools, this package is intentionally lightweight and simpler. It is designed for small projects, assignments, or quick checks where a full validation framework would be unnecessary or too complex.

## Get started

You can install this package into your preferred Python environment using pip:

``` bash
$ pip install datajanitor
```

TODO: Add a brief example of how to use the package to this section

To use datajanitor in your code:

``` python
>>> import datajanitor
>>> datajanitor.hello_world()
```

## Contributor

Group 31: Karan Partap Bains, Yasaman Eftekharypour, Sameel Syed, Yuting Ji

## Copyright

-   Copyright © 2026 Karan Bains, Yasaman Eftekharypour, Sameel Syed, Yuting Ji.
-   Free software distributed under the [MIT License](./LICENSE).
