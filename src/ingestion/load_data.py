import pandas as pd

def load_transactions(csv_path):
    df = pd.read_csv(csv_path)
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
    df.dropna(subset=["Timestamp", "Amount", "TransactionID"], inplace=True)
    df.sort_values("Timestamp", inplace=True)
    return df
