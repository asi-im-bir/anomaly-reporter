# 🚀 Proactive Access Anomaly Reporting Tool

> **Automated Logical Access Risk Detection & Reporting**  
> A Python + AI-powered tool for continuous access monitoring and GRC-aligned anomaly reporting.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![AI Integration](https://img.shields.io/badge/AI-Claude%20AI-purple)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📘 Overview

The **Proactive Access Anomaly Reporting Tool** offers a lightweight and high-impact way to detect and report **logical access anomalies** across enterprise environments.  
It bridges the gap between **technical detection** and **executive GRC reporting**, aligning outcomes with standards like **ISO/IEC 27001 (A.5.15)** and **NIS2**.

This project combines:
- 🧮 **Python (Pandas/Numpy)** — for anomaly detection and cross-system statistical analysis  
- 🧠 **Claude AI** — for translating technical outputs into structured, compliance-aligned reports  

---

## 🎯 Project Goals

| Objective | Description |
|------------|-------------|
| **Risk Visibility** | Detect statistically abnormal access patterns missed by static rule-based tools. |
| **Compliance Evidence** | Automate report generation aligned to ISO 27001 A.5.15 and NIS2. |
| **Efficiency** | Reduce manual audit work through continuous automated analysis. |
| **Actionable Insight** | Provide management-ready summaries and corrective recommendations. |

---

## 💡 Real-World Problem

Security teams often rely on reactive detection and fragmented monitoring tools.  
Common challenges include:

| Challenge | Description |
|------------|--------------|
| **Reactive Security** | Alerts only after policy violations occur, not when abnormal behaviors begin. |
| **Cross-System Blind Spots** | IAM, VPN, and app logs exist in silos, limiting unified visibility. |
| **Manual GRC Translation** | Engineers manually interpret raw logs for audit reports. |
| **Evidence Gaps** | Hard to prove continuous monitoring during ISO/NIS2 audits. |

---

## 🧩 Solution Approach

This tool creates a continuous **Detect → Reason → Report** loop.

```mermaid

flowchart TD
    A[Access Logs (CSV)] --> B[Python Script: anomaly_detector.py]
    B --> C[Statistical + After-Hours Detection]
    C --> D[final_risk_data_for_claude.txt]
    D --> E[Claude AI Reasoning Engine]
    E --> F[Executive Management Report]

⚙️ How It Works

1️⃣ Data Input
Place your access log file in the project directory:

Example: access_logs.csv

csv
Copy code
UserID,SystemAccessed,AccessTime
U001,ERP_Prod,2025-10-25 23:05:00
U003,S3_Bucket_Fin,2025-10-26 01:45:00
U004,CRM,2025-10-25 15:00:00

2️⃣ Python Detection Script
File: anomaly_detector.py

Key logic:

python
Copy code
threshold = mean_systems + (2 * std_systems)
high_risk_users = unique_systems_count[unique_systems_count > threshold].index.tolist()
Functions:

Detects users accessing an unusually high number of unique systems (mean + 2×STD)

Flags all access outside defined business hours (08:00–18:00)

Generates summarized findings as final_risk_data_for_claude.txt

3️⃣ AI Reasoning Layer
The text output is analyzed by Claude AI, which:

Interprets findings through ISO 27001 and NIS2 frameworks

Produces a structured report with:

Executive Summary

Key Findings

Corrective Actions

Responsible Owners

📊 Example Output
🧮 Python Output (final_risk_data_for_claude.txt)
sql
Copy code
--- WEEKLY LOGICAL ACCESS ANOMALY REPORT DATA ---

1. HIGH STATISTICAL RISK FINDINGS (Users above 2x STD threshold: 8.70 systems):
Users: None detected

2. AFTER-HOURS ACCESS INCIDENTS (Outside 08:00–18:00):
UserID          AccessTime SystemAccessed
U001 2025-10-25 23:05:00   ERP_Prod
U003 2025-10-26 01:45:00   S3_Bucket_Fin

3. NORMALIZATION CONTEXT:
Average number of unique systems accessed per user: 2.80
🧠 Claude AI Output (Executive Report Example)
markdown
Copy code
Executive Summary:
  - Two after-hours access events detected.
  - No high statistical anomalies found.

Top Risks:
  1. Potential misuse of privileged credentials.
  2. Weak after-hours access controls.

Recommended Actions:
  - Review off-hour activity for U001 and U003.
  - Implement Conditional Access policies.
  - Update audit log retention under ISO 27001 A.5.15.
🛠️ Setup Guide
🔧 Prerequisites
Python 3.x

Installed libraries:

bash
Copy code
pip install pandas numpy
Access to Claude AI

▶️ Execution Steps
Place Data File

Ensure access_logs.csv is in your project root directory.

Run Detection Script

bash
Copy code
python anomaly_detector.py
Generate Report

Open final_risk_data_for_claude.txt

Copy contents into Claude AI

Use the pre-defined reasoning prompt (in /docs/prompt_template.txt)

🌟 Key Benefits
Category	Manual Method	Automated Method
Risk Discovery	Rule-based alerts only	Detects hidden statistical outliers
Reporting	Manual consolidation	AI-generated executive report
GRC Alignment	Reactive and fragmented	Continuous, ISO/NIS2 contextualized
Operational Scale	Periodic manual checks	Continuous daily/weekly execution
Team Value	Time-consuming	Frees analysts for higher-value tasks

📁 Project Structure
bash
Copy code
anomaly-reporter/
│
├── anomaly_detector.py
├── access_logs.csv
├── final_risk_data_for_claude.txt
├── /docs/
│   └── prompt_template.txt
├── README.md
└── LICENSE
🧠 Technologies
Layer	Technology	Purpose
Detection	Python (Pandas, NumPy)	Data parsing, statistical analysis
Reporting	Claude AI	Executive reasoning & compliance alignment
Data Format	CSV / TXT	Lightweight, portable file exchange

🚧 Future Enhancements
Area	Enhancement
Integration	API connectors for Okta, Azure AD, and SIEMs
Visualization	Add Tableau/Power BI dashboards
Automation	Direct Claude API integration
Detection	Add geolocation and privilege-based anomaly detection

📜 License
This project is licensed under the MIT License — see LICENSE for details.

🤝 Contributing
Contributions are welcome!
If you’d like to add new detection rules, compliance mappings, or integrations, please fork the repo and open a pull request.

👨‍💻 Author
Developed by: asi-im-bir
Focus Areas: Security Automation | GRC Engineering | Continuous Monitoring
Connect: LinkedIn • GitHub

“Transforming reactive audits into proactive intelligence.”


