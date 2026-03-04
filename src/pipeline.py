"""
Data Quality Deduplication Pipeline
Author: Carlos
"""

import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def detect_duplicates(df, column):
    return df[df.duplicated(column, keep=False)]

if __name__ == "__main__":
    print("Pipeline ready")
