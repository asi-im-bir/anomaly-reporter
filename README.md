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

This is a great, detailed plan for a security automation tool. I've reformatted it into a professional, clear, and engaging GitHub README.md document that prioritizes readability and impact.🕵️‍♂️ Access Anomaly Reporter (Detect $\rightarrow$ Report)Continuous GRC Monitoring and AI-Powered Risk Reporting💡 Project Value PropositionThis tool automates the process of auditing logical access logs, transitioning security and GRC oversight from a periodic, manual check to a continuous intelligence loop. It automatically surfaces anomalies and leverages Generative AI (Claude) to interpret findings within the context of regulatory frameworks like ISO 27001 and NIS2.🌟 Key BenefitsCategoryManual MethodAutomated Method (This Tool)Risk DiscoveryRule-based alerts only.Detects hidden statistical outliers (mean + 2 $\times$ STD).ReportingTime-consuming, manual data consolidation.AI-generated executive report with actionable recommendations.GRC AlignmentReactive and fragmented.Continuous, contextualized against ISO/NIS2 controls.Team ValueAnalysts spend time on low-value data crunching.Frees analysts for higher-value threat hunting and response.🧩 Solution Approach: The Detect $\rightarrow$ Reason $\rightarrow$ Report LoopThe system is designed as a simple, powerful pipeline connecting raw data to final executive insights.Code snippetflowchart TD
    A[Access Logs (CSV)] --> B{Python Script: anomaly_detector.py};
    B --> C[Statistical + After-Hours Detection];
    C --> D[final_risk_data_for_claude.txt];
    D --> E{Claude AI Reasoning Engine};
    E --> F[Executive Management Report (GRC Contextualized)];
⚙️ How It WorksData Input: You provide the access log data in the root directory as access_logs.csv.Required Format Example:Code snippetUserID,SystemAccessed,AccessTime
U001,ERP_Prod,2025-10-25 23:05:00
Python Detection Script (anomaly_detector.py):Statistical Anomaly: Identifies users accessing a number of unique systems that exceeds the average by a statistically significant margin (mean + $2\sigma$ standard deviations).Time Anomaly: Flags all access incidents occurring outside of defined business hours ($\mathbf{08:00–18:00}$).Output: Generates a summarized, structured text file: final_risk_data_for_claude.txt.AI Reasoning Layer (Claude AI):The text summary is analyzed by Claude using a predefined prompt.Claude interprets the risks through the lens of GRC frameworks.Final Report Output: A structured report including an Executive Summary, Key Findings, Corrective Actions, and Responsible Owners.📊 Example OutputPython Summary (final_risk_data_for_claude.txt)This is the raw data fed to the AI engine:--- WEEKLY LOGICAL ACCESS ANOMALY REPORT DATA ---

HIGH STATISTICAL RISK FINDINGS (Users above 2x STD threshold: 8.70 systems):
Users: None detected

AFTER-HOURS ACCESS INCIDENTS (Outside 08:00–18:00):
UserID  AccessTime             SystemAccessed
U001    2025-10-25 23:05:00    ERP_Prod
U003    2025-10-26 01:45:00    S3_Bucket_Fin

NORMALIZATION CONTEXT: 
Average number of unique systems accessed per user: 2.80
🧠 Claude AI Executive Report ExampleThis is the AI-generated final output:Executive Summary:Two after-hours access events detected. No high statistical anomalies found this period.Top Risks:Potential misuse of privileged credentials during unsupervised hours.Weak after-hours access controls for critical systems.Recommended Actions:Immediate: Review off-hour activity for U001 and U003 with their managers.Technical: Implement Conditional Access policies to restrict system access by time-of-day.Compliance: Update audit log retention under ISO 27001 A.5.15.🛠️ Setup and Execution GuidePrerequisitesPython 3.xLibraries: Install the dependencies:Bashpip install pandas numpy
Access to the Claude AI chat interface (or API, for future integration).▶️ Execution StepsPlace Data FileEnsure your log file is named access_logs.csv and is located in the project root.Run Detection ScriptExecute the Python script in your terminal:Bashpython anomaly_detector.py
Generate AI ReportOpen final_risk_data_for_claude.txt.Copy the entire contents.Paste the contents into the Claude AI chat interface.Use the reasoning prompt located in /docs/prompt_template.txt to generate the final, structured report.📁 Project StructureBashanomaly-reporter/
│ 
├── anomaly_detector.py             # Core script for data processing and detection
├── access_logs.csv                 # INPUT: Raw access logs
├── final_risk_data_for_claude.txt  # OUTPUT: Summary data for AI
├── /docs/
│   └── prompt_template.txt         # Template for the AI reasoning prompt
├── README.md
└── LICENSE
🚧 Future EnhancementsAreaEnhancementIntegrationAPI connectors for Okta, Azure AD, and SIEM platforms.AutomationDirect API integration with Claude (or other LLMs) to fully automate report generation.DetectionAdd geolocation, privilege-based, and peer-group anomaly detection rules.VisualizationIntegrate with Tableau/Power BI for dashboard reporting.🤝 Contributing & LicenseThis project is licensed under the MIT License—see the LICENSE file for details. Contributions, bug reports, and suggestions for new detection logic are highly welcome! Please feel free to fork the repository and open a pull request.👨‍💻 AuthorDeveloped by: asi-im-birFocus Areas: Security Automation | GRC Engineering | Continuous MonitoringConnect: LinkedIn • GitHub
