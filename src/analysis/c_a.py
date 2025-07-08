def detect_anomalies(df, threshold=3.0):
    df = df.copy()
    mean = df["Amount"].mean()
    std = df["Amount"].std()
    df["Z_score"] = (df["Amount"] - mean) / std
    df["Anomaly"] = df["Z_score"].abs() > threshold
    return df
