# 🧾 Travel Expense Tracker

A lightweight, user-friendly web app to **record, analyze, and visualize travel expenses** — built using Python, Streamlit, and Google Sheets.

![App Screenshot](https://via.placeholder.com/900x400?text=Insert+Screenshot+Here)

---

## 🚀 Features

- 📅 Add travel expenses with date, category, amount, location & description
- 🔍 Filter by date range or category
- 📊 Visual summary with pie and bar charts
- ☁️ Real-time data sync using Google Sheets
- 🔐 Secrets managed securely with Streamlit Cloud
- 📥 CSV/Excel export support (coming soon)

---

## 🛠️ Tech Stack

| Layer        | Tools Used                        |
|--------------|-----------------------------------|
| Frontend     | Streamlit                         |
| Backend/API  | Python + gspread + pandas         |
| Data Store   | Google Sheets                     |
| Visualization| Plotly                            |

---

## 💻 How to Run Locally

### 🔧 Prerequisites
- Python 3.9 or later
- Streamlit, gspread, oauth2client, pandas, plotly

### 📦 Installation

```bash
git clone https://github.com/kalmeshsaunshi01/travel-expense-tracker.git
cd travel-expense-tracker
pip install -r requirements.txt


🔑 Add Google Service Credentials
Create .streamlit/secrets.toml

Paste your GCP service account credentials:


Copy code
[gcp_service_account]
type = "service_account"
project_id = "..."
private_key_id = "..."
private_key = "-----BEGIN PRIVATE KEY-----\\nMIIE..."
client_email = "..."
sheet_name = "Travel Expenses"

▶️ Run the App
streamlit run main.py

🌍 Deployment
Deployed on Streamlit Cloud 👉 Click Here to Launch App
(replace with your real link after deployment)





📬 Feedback & Contributions
We’re actively improving the app. Issues, feedback, or suggestions are welcome via GitHub Issues.

🛡️ License
This project is open-source and available under the MIT License.

yaml
Copy code

---

### ✅ To Use It:
1. Save as `README.md` in the root of your repo
2. Customize the links and screenshot when deployed