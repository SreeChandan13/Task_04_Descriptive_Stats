import polars as pl

def run_polars_analysis(meta_file):
    import json
    with open(meta_file) as f:
        meta = json.load(f)

        print(type(df))


    df = pl.read_csv(meta["file"])
    print(type(df))    # Should print: <class 'polars.internals.dataframe.DataFrame'>
    print(dir(df))  

    print(f"=== Analyzing Dataset: {meta['file']} ===\n")

    # Numeric summary stats
    numeric_cols = [col for col, dtype in zip(df.columns, df.dtypes) if dtype in [pl.Int64, pl.Float64]]
    stats = ["count", "null_count", "mean", "std", "min", "quantile_25", "median", "quantile_75", "max"]

    summary = []
    for stat in stats:
        if stat == "quantile_25":
            summary.append(pl.col(numeric_cols).quantile(0.25).alias("25%"))
        elif stat == "median":
            summary.append(pl.col(numeric_cols).median().alias("50%"))
        elif stat == "quantile_75":
            summary.append(pl.col(numeric_cols).quantile(0.75).alias("75%"))
        else:
            summary.append(getattr(pl.col(numeric_cols), stat)().alias(stat))

    numeric_summary = df.select(summary)
    print("--- Numeric Column Summary ---")
    print(numeric_summary)

    # Categorical counts
    print("\n--- Categorical Value Counts ---")
    for cat_col in meta.get("categorical", []):
        print(f"\n{cat_col}:")
        counts = df.groupby(cat_col).count().sort("count", reverse=True)
        print(counts)

    # Grouped statistics
    print(f"\n--- Grouped by {meta.get('group_by', [])} ---")

    group_cols = meta.get("group_by", [])
    if group_cols:
        # Build aggregations per numeric column
        aggs = []
        for col in numeric_cols:
            aggs += [
                pl.col(col).count().alias(f"{col}_count"),
                pl.col(col).mean().alias(f"{col}_mean"),
                pl.col(col).std().alias(f"{col}_std"),
                pl.col(col).min().alias(f"{col}_min"),
                pl.col(col).quantile(0.25).alias(f"{col}_25%"),
                pl.col(col).median().alias(f"{col}_50%"),
                pl.col(col).quantile(0.75).alias(f"{col}_75%"),
                pl.col(col).max().alias(f"{col}_max"),
            ]

        grouped_df = df.groupby(group_cols).agg(aggs)
        print(grouped_df)