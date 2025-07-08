def detect_anomalies(df, threshold=3.0):
    """
    Detect anomalies in transaction amounts using Z-score method.

    Parameters:
        df (DataFrame): Input dataframe with 'Amount' column
        threshold (float): Z-score threshold to consider an anomaly

    Returns:
        DataFrame: Original dataframe with added columns:
                   - 'Z_score': Z-score of each transaction
                   - 'Anomaly': Boolean flag for anomaly
    """
    df = df.copy()
    mean = df["Amount"].mean()
    std = df["Amount"].std()
    
    # Avoid division by zero
    if std == 0:
        df["Z_score"] = 0
        df["Anomaly"] = False
        return df

    df["Z_score"] = (df["Amount"] - mean) / std
    df["Anomaly"] = df["Z_score"].abs() > threshold
    return df
