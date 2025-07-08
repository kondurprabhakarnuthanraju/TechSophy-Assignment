# TechSophy-Assignment
# 💸 Personal Finance Tracker with Spending Insights

A modular Python system that analyzes personal financial transaction data and provides intelligent insights using anomaly detection, clustering, and visual analytics. Built as part of the **Techsophy Coding Test** for software engineering assessment.

---

## 🚀 Project Overview

This system helps individuals understand their spending patterns by:
- Parsing raw transaction data
- Identifying unusual spending behavior
- Grouping similar transactions using unsupervised learning (clustering)
- Visualizing trends across time and category
- Generating smart, human-readable recommendations

---

## 🧠 Skills Demonstrated

| Category        | Skills Applied |
|----------------|----------------|
| **AI/ML**       | KMeans clustering, Z-score anomaly detection |
| **Data Handling** | Parsing timestamps, cleaning missing data, handling categorical formats |
| **Critical Thinking** | Categorizing behavior, defining anomalies, suggesting improvements |
| **Visualization** | Spending trends, transaction type charts |
| **Software Design** | Modular code structure, pipeline-based processing |

---

## 🧱 Folder Structure
personal-finance-tracker/
├── data/ # Place raw CSV transaction files here
│ └── financial_anomaly_data.csv
│
├── notebooks/
│ └── analysis_notebook.ipynb # Complete pipeline using all modules
│
├── src/
│ ├── ingestion/
│ │ └── load_data.py # Load and clean transaction data
│ ├── analysis/
│ │ ├── anomaly_detection.py # Z-score based anomaly detection
│ │ └── cluster_analysis.py # KMeans clustering on amount + type
│ ├── visualization/
│ │ └── plots.py # Monthly trends and category distributions
│ └── recommendation/
│ └── generate_insights.py # Generate smart text-based insights
│
├── assets/ # (Optional) Diagrams or visuals
│
└── README.md # This file

---

## 📥 Input Format (CSV)

Your CSV file must include these fields:

| Column          | Description                         |
|-----------------|-------------------------------------|
| `Timestamp`      | Date and time of transaction        |
| `TransactionID`  | Unique transaction identifier       |
| `AccountID`      | Unique customer/account ID          |
| `Amount`         | Value of the transaction            |
| `Merchant`       | Vendor/merchant of the transaction  |
| `TransactionType`| Purchase, Withdrawal, etc.          |
| `Location`       | Place of transaction                |

---

## 📊 Features

✅ Clean and ingest transaction data  
✅ Perform **anomaly detection** using Z-score  
✅ Apply **clustering** (KMeans) to group similar transaction behaviors  
✅ Generate **line plots** for monthly trends  
✅ Produce **bar plots** for transaction category distributions  
✅ Output **personalized insights and recommendations**

---

## 📈 Sample Insights

- 🔍 "5 unusual transactions detected this month exceeding ₹10,000."
- 📉 "High withdrawal volume — over 40% of your spending is in cash."
- 🛍️ "Most of your April spending was in 'Shopping' — ₹18,000."

---



