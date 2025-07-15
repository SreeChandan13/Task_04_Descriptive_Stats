import pandas as pd
import json

def load_metadata(meta_path):
    with open(meta_path, 'r') as f:
        return json.load(f)

def run_pandas_analysis(meta_path):
    meta = load_metadata(meta_path)
    df = pd.read_csv(meta["file"])

    print(f"\n=== Analyzing Dataset: {meta['file']} ===")

    # Numerical Summary
    print("\n--- Numeric Column Summary ---")
    print(df[meta["numeric_columns"]].describe())

    # Categorical Summary
    print("\n--- Categorical Value Counts ---")
    for col in meta["categorical_columns"]:
        print(f"\n{col}:\n{df[col].value_counts()}")

    # Grouped Summary
    if meta.get("group_by"):
        print(f"\n--- Grouped by {meta['group_by']} ---")
        grouped = df.groupby(meta["group_by"])[meta["numeric_columns"]].describe()
        print(grouped)
