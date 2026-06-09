import pandas as pd


def clean_economic_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and standardise economic indicator data."""
    required_columns = {"country", "year", "indicator", "value"}

    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df.copy()
    df["country"] = df["country"].astype(str).str.strip()
    df["indicator"] = df["indicator"].astype(str).str.strip()
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    df = df.dropna(subset=["country", "year", "indicator", "value"])
    df["year"] = df["year"].astype(int)

    return df.sort_values(["country", "indicator", "year"])
