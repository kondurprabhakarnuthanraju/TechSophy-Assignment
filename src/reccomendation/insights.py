def generate_recommendations(df):
    insights = []
    total = df["Amount"].sum()

    withdrawals = df[df["TransactionType"] == "Withdrawal"]
    if not withdrawals.empty:
        withdraw_ratio = withdrawals["Amount"].sum() / total
        if withdraw_ratio > 0.4:
            insights.append("High withdrawal volume detected. Consider limiting cash withdrawals.")

    if "Anomaly" in df.columns:
        num_anomalies = df["Anomaly"].sum()
        if num_anomalies > 0:
            insights.append(f"{num_anomalies} unusual transactions flagged for review.")

    return insights
