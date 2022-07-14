import pytest
from src.dataframes import create_empty_df, create_simple_df, create_full_df

     
def test_sizes():
    assert create_empty_df().shape == (0, 0,)
    assert create_simple_df().shape == (6, 1,)
    assert create_full_df().shape == (3, 5,)

