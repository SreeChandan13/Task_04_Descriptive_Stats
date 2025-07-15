import csv
import json
from collections import defaultdict, Counter
from statistics import mean, stdev, median

def load_metadata(meta_path):
    with open(meta_path, 'r') as f:
        return json.load(f)

def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        return list(reader)

def run_pure_python_analysis(meta_path):
    meta = load_metadata(meta_path)
    rows = read_csv(meta["file"])

    print(f"\n=== Analyzing Dataset: {meta['file']} ===")

    # Numeric Column Summary
    print("\n--- Numeric Column Summary ---")
    for col in meta["numeric_columns"]:
        values = [float(row[col]) for row in rows if row[col]]
        print(f"\n{col}:")
        print(f"Count: {len(values)}")
        print(f"Mean: {mean(values):.2f}")
        print(f"Std: {stdev(values):.2f}" if len(values) > 1 else "Std: N/A")
        print(f"Min: {min(values)}")
        print(f"25%: {sorted(values)[int(0.25*len(values))]}")
        print(f"Median: {median(values)}")
        print(f"75%: {sorted(values)[int(0.75*len(values))]}")
        print(f"Max: {max(values)}")

    # Categorical Column Summary
    print("\n--- Categorical Value Counts ---")
    for col in meta["categorical_columns"]:
        values = [row[col] for row in rows if row[col]]
        counts = Counter(values)
        print(f"\n{col}:")
        for val, count in counts.most_common(10):
            print(f"{val}: {count}")

    # Grouped Summary
    if meta.get("group_by"):
        print(f"\n--- Grouped by {meta['group_by']} ---")
        groups = defaultdict(list)
        for row in rows:
            key = tuple(row[g] for g in meta["group_by"])
            groups[key].append(row)

        for group_key, group_rows in groups.items():
            print(f"\nGroup: {group_key}")
            for col in meta["numeric_columns"]:
                values = [float(r[col]) for r in group_rows if r[col]]
                if values:
                    print(f"  {col} - Count: {len(values)}, Mean: {mean(values):.2f}, Max: {max(values)}")
