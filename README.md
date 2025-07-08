# 💸 Personal Finance Tracker with Spending Insights

A modular AI-powered Python project that takes raw financial transaction data and generates smart visual insights, detects anomalies, clusters behavior, and recommends actionable improvements.

Designed for real-world applications like **expense auditing**, **budget tracking**, and **automated financial intelligence**.

---

## 📌 Problem Statement

Build a system that:
- Ingests raw financial transactions from a CSV
- Analyzes spending patterns
- Detects unusual (anomalous) transactions
- Clusters similar behaviors using unsupervised ML
- Visualizes monthly trends and category spending
- Recommends insights to users based on financial behavior

---

## 🎯 Project Goals

| Goal | Achieved |
|------|----------|
| 🧹 Data Cleaning & Parsing | ✅ Yes |
| 🔍 Anomaly Detection (Z-Score) | ✅ Yes |
| 🧠 Clustering (KMeans) | ✅ Yes |
| 📈 Visualizations (Seaborn) | ✅ Yes |
| 🤖 Personalized Recommendations | ✅ Yes |
| 📦 Modular Architecture | ✅ Yes |

---

## 🧠 Skills Demonstrated

- AI/ML: Clustering (KMeans), Outlier Detection (Z-Score)
- Data Wrangling: Parsing timestamps, handling missing data
- Visualization: Matplotlib, Seaborn
- Modular Python Design: Reusable `src/` pipeline
- Problem Solving: Making sense of financial behavior

---

## 🧱 Folder Structure

```bash
personal-finance-tracker/
├── data/                          # 🧾 CSV input files (e.g., transactions.csv)
│   └── financial_anomaly_data.csv
├── notebooks/                     # 📒 Jupyter analysis pipeline
│   └── analysis_notebook.ipynb
├── src/                           # 🧠 Core modules
│   ├── ingestion/
│   │   └── load_data.py
│   ├── analysis/
│   │   ├── anomaly_detection.py
│   │   └── cluster_analysis.py
│   ├── visualization/
│   │   └── plots.py
│   └── recommendation/
│       └── generate_insights.py
├── assets/                        # 🖼️ Diagrams or architecture images
│   └── architecture.png (optional)
├── requirements.txt               # 📦 All dependencies
├── .gitignore                     # 🚫 Files to exclude from version control
└── README.md                      # 📘 You're here!
 # Clone the repo
git clone https://github.com/your-username/personal-finance-tracker.git
cd personal-finance-tracker

# Create and activate virtual environment (optional)
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the analysis notebook
cd notebooks
jupyter notebook analysis_notebook.ipynb
CSV Input → Cleaned Data → Anomaly Detection
                          → Clustering
                          → Visualizations
                          → Recommendations

# 💸 Personal Finance Tracker with Spending Insights

A modular AI-powered Python project that takes raw financial transaction data and generates smart visual insights, detects anomalies, clusters behavior, and recommends actionable improvements.

Designed for real-world applications like **expense auditing**, **budget tracking**, and **automated financial intelligence**.

---

## 🚀 Run in Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/personal-finance-tracker/blob/main/notebooks/analysis_notebook.ipynb)

No setup needed — upload your CSV file and run the full pipeline directly in the cloud.

---

## 📌 Problem Statement

...
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO/blob/main/notebooks/analysis_notebook.ipynb)

