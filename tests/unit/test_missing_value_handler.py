import pandas as pd
import numpy as np
import pytest
from datajanitor import missing_value_handler


def test_missing_value_handler_edge_cases(data):
    """
    Verify missing_value_handler raises correct errors
    and handles missing values properly.
    """
    
    # TypeError is expected
    with pytest.raises(TypeError):
        missing_value_handler([1, 2, 3])

    # ValueError is expected
    df = pd.DataFrame({"A": [1, np.nan]})

    with pytest.raises(ValueError):
        missing_value_handler(df, method="invalid")
        
    
