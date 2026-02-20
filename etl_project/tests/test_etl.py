import os
import sys

# Add project root directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from ETL_job import transform


def test_transform():
    input_data = pd.DataFrame({
        "order_date": ["2024-01-01", "invalid_date", "2024-01-01"],
        "quantity": [2, None, 2],
        "unit_price": [10.0, 5.0, 10.0],
        "country": ["egypt", "usa", "egypt"],
        "customer_name": ["Ali Ali", "Sara Ahmed", "Ali Ali"]
    })

    result = transform(input_data)

    assert len(result) == 1
    assert result["order_date"].isna().sum() == 0
    assert result.iloc[0]["quantity"] == 2
    assert result.iloc[0]["total_price"] == 20.0
    assert result.iloc[0]["country"] == "EGYPT"
    assert result.iloc[0]["customer_name"] == "Ali Ali"
    #
