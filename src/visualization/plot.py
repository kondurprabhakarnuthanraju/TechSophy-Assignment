import matplotlib.pyplot as plt
import seaborn as sns

def plot_monthly_spending(df):
    df = df.copy()
    df["Month"] = df["Timestamp"].dt.to_period("M")
    monthly = df.groupby("Month")["Amount"].sum().reset_index()
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=monthly["Month"].astype(str), y=monthly["Amount"])
    plt.title("Monthly Spending Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_transaction_type_distribution(df):
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, y="TransactionType", order=df["TransactionType"].value_counts().index)
    plt.title("Transaction Type Distribution")
    plt.tight_layout()
    plt.show()
