#AI generated for explorative purposes

from functools import cache, lru_cache
import pandas as pd


# Basic Implementation
def describe_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()

# Using functools.cache (Python 3.9+)
@cache
def describe_dataframe_cache(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()

# Using functools.lru_cache
@lru_cache(maxsize=None)
def describe_dataframe_lru_cache(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()

'''
# Example usage
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

print(describe_dataframe(df))
print(describe_dataframe_cache(df))
'''