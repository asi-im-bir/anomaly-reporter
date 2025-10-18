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


## 🧩 Solution Approach: The Detect $\rightarrow$ Reason $\rightarrow$ Report Loop

The system is designed as a simple, powerful pipeline connecting raw data to final executive insights.

```mermaid
flowchart TD
    A[Access Logs (CSV)] --> B{Python Script: anomaly_detector.py};
    B --> C[Statistical + After-Hours Detection];
    C --> D[final_risk_data_for_claude.txt];
    D --> E{Claude AI Reasoning Engine};
    E --> F[Executive Management Report (GRC Contextualized)];
```

### ⚙️ How It Works

1.  **Data Input:** You provide the access log data in the root directory as **`access_logs.csv`**.

      * *Required Format Example:*
        ```csv
        UserID,SystemAccessed,AccessTime
        U001,ERP_Prod,2025-10-25 23:05:00
        ```

2.  **Python Detection Script (`anomaly_detector.py`):**

      * **Statistical Anomaly:** Identifies users accessing a number of unique systems that exceeds the average by a statistically significant margin (mean + $2\sigma$ standard deviations).
      * **Time Anomaly:** Flags all access incidents occurring outside of defined business hours ($\mathbf{08:00–18:00}$).
      * **Output:** Generates a summarized, structured text file: **`final_risk_data_for_claude.txt`**.

3.  **AI Reasoning Layer (Claude AI):**

      * The text summary is analyzed by Claude using a predefined prompt.
      * Claude **interprets the risks** through the lens of GRC frameworks.
      * **Final Report Output:** A structured report including an Executive Summary, Key Findings, **Corrective Actions**, and Responsible Owners.

-----

## 📊 Example Output

### Python Summary (`final_risk_data_for_claude.txt`)

This is the raw data fed to the AI engine:

```
--- WEEKLY LOGICAL ACCESS ANOMALY REPORT DATA ---

HIGH STATISTICAL RISK FINDINGS (Users above 2x STD threshold: 8.70 systems):
Users: None detected

AFTER-HOURS ACCESS INCIDENTS (Outside 08:00–18:00):
UserID  AccessTime             SystemAccessed
U001    2025-10-25 23:05:00    ERP_Prod
U003    2025-10-26 01:45:00    S3_Bucket_Fin

NORMALIZATION CONTEXT: 
Average number of unique systems accessed per user: 2.80
```

### 🧠 Claude AI Executive Report Example

This is the AI-generated final output:

> **Executive Summary:**
> Two after-hours access events detected. No high statistical anomalies found this period.
>
> **Top Risks:**
>
> 1.  Potential misuse of privileged credentials during unsupervised hours.
> 2.  Weak after-hours access controls for critical systems.
>
> **Recommended Actions:**
>
> 1.  **Immediate:** Review off-hour activity for U001 and U003 with their managers.
> 2.  **Technical:** Implement Conditional Access policies to restrict system access by time-of-day.
> 3.  **Compliance:** Update audit log retention under **ISO 27001 A.5.15**.

-----

## 🛠️ Setup and Execution Guide

### Prerequisites

  * **Python 3.x**
  * **Libraries:** Install the dependencies:
    ```bash
    pip install pandas numpy
    ```
  * Access to the **Claude AI** chat interface (or API, for future integration).

### ▶️ Execution Steps

1.  **Place Data File**

      * Ensure your log file is named **`access_logs.csv`** and is located in the project root.

2.  **Run Detection Script**

      * Execute the Python script in your terminal:

    <!-- end list -->

    ```bash
    python anomaly_detector.py
    ```

3.  **Generate AI Report**

      * Open **`final_risk_data_for_claude.txt`**.
      * Copy the entire contents.
      * Paste the contents into the Claude AI chat interface.
      * Use the reasoning prompt located in **`/docs/prompt_template.txt`** to generate the final, structured report.

-----

## 📁 Project Structure

```bash
anomaly-reporter/
│ 
├── anomaly_detector.py             # Core script for data processing and detection
├── access_logs.csv                 # INPUT: Raw access logs
├── final_risk_data_for_claude.txt  # OUTPUT: Summary data for AI
├── /docs/
│   └── prompt_template.txt         # Template for the AI reasoning prompt
├── README.md
└── LICENSE
```

-----

## 🚧 Future Enhancements

| Area | Enhancement |
| :--- | :--- |
| **Integration** | API connectors for Okta, Azure AD, and SIEM platforms. |
| **Automation** | Direct API integration with Claude (or other LLMs) to fully automate report generation. |
| **Detection** | Add geolocation, privilege-based, and peer-group anomaly detection rules. |
| **Visualization** | Integrate with Tableau/Power BI for dashboard reporting. |

-----

## 🤝 Contributing & License

This project is licensed under the **MIT License**—see the `LICENSE` file for details. Contributions, bug reports, and suggestions for new detection logic are highly welcome\! Please feel free to fork the repository and open a pull request.

-----

### 👨‍💻 Author

Developed by: **asi-im-bir**

Focus Areas: Security Automation | GRC Engineering | Continuous Monitoring

Connect: [LinkedIn](https://www.google.com/search?q=https://www.linkedin.com/in/asi-im-bir) • [GitHub](https://www.google.com/search?q=https://github.com/asi-im-bir)
