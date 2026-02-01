---
editor: 
  markdown: 
    wrap: 72
---

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Milestone 4

### Added

-   Added new unit tests to improve reliability and prevent
    regressions: - Unit test for `validate_schema` when **multiple
    validations** are applied
    (https://github.com/UBC-MDS/DSCI_524_group31_datajanitor/pull/80)
-   Unit test for `standardize_columns` behavior
    (https://github.com/UBC-MDS/DSCI_524_group31_datajanitor/pull/81)
-   Added clearer **example usage** showing how to use the package
    functions (Issue #74, PR #85)
-   Created a dedicated **`dev` branch** to support ongoing development
    work (Issue #70)
-   Updated README badges to avoid “package or version not found”
    ((Issue #87)

### Changed

-   Updated publishing instructions/command to support publishing to
    **TestPyPI** (Issue #73)
-   Added explicit **Python and pandas version locking** to preserve
    consistent functionality across environments (PR #67)
-   Updated the README function section to include clearer
    **input/output** descriptions (Issue #72, PR #85)
-   Updated the GitHub repository **About** section by adding the GitHub
    link and a short description (Issue #75)

### Fixed

-   Fixed the **Quarto landing page** by updating `quarto.yml`
    configuration (Issue #76, PR #77)

### Maintenance

-   Deleted extra branches to keep the repository clean (Issue #69)

### Governance

-   Added discussion and reasoning for the **license choice** (Issue
    #68)
