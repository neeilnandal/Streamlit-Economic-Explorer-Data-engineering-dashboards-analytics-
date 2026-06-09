import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load economic data from a CSV file."""
    try:
        return pd.read_csv(path)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Data file not found: {path}") from exc
