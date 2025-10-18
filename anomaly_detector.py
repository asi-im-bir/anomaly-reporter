import pandas as pd
import numpy as np

# --- 1. DETECTION FUNCTIONS (One is statistical, complex logic) ---

# This function detects users accessing an unusually high number of unique systems.
# This is the type of code you would ask Claude to generate in a real scenario.
def detect_high_system_access(df):
    """Identifies users accessing an unusually high number of unique systems 
       using the Mean + 2*Standard Deviation rule."""
    
    # Calculate the number of unique systems accessed per user
    unique_systems_count = df.groupby('UserID')['SystemAccessed'].nunique()
    
    # Calculate the mean and standard deviation
    mean_systems = unique_systems_count.mean()
    std_systems = unique_systems_count.std()
    
    # Define the threshold (Mean + 2 * Standard Deviation)
    # This finds highly unusual behavioral spikes
    threshold = mean_systems + (2 * std_systems)
    
    # Identify users whose unique system count is above the threshold
    high_risk_users = unique_systems_count[unique_systems_count > threshold].index.tolist()
    
    # Also return the users who are above the average but below the 2*STD for context
    above_average_users = unique_systems_count[
        (unique_systems_count > mean_systems) & (unique_systems_count <= threshold)
    ].index.tolist()
    
    return high_risk_users, above_average_users, threshold

# --- 2. MAIN EXECUTION LOGIC ---

# Load Data
try:
    df = pd.read_csv('access_logs.csv')
    df['AccessTime'] = pd.to_datetime(df['AccessTime'])
except FileNotFoundError:
    print("Error: access_logs.csv not found. Please create the file as instructed.")
    exit()

# Set Detection Parameters
START_HOUR = 8
END_HOUR = 18

# A) After-Hours Anomaly Detection
df['Hour'] = df['AccessTime'].dt.hour
after_hours_anomalies = df[
    (df['Hour'] < START_HOUR) | (df['Hour'] >= END_HOUR)
]

# B) Statistical Anomaly Detection
high_risk_users, above_average_users, threshold = detect_high_system_access(df)

# --- 3. COMPILE FINAL RISK SUMMARY FOR CLAUDE ---

# Raw after-hours data string
after_hours_raw = after_hours_anomalies[['UserID', 'AccessTime', 'SystemAccessed']].to_string(index=False)

# Compile the comprehensive text summary
final_risk_data = f"""
--- WEEKLY LOGICAL ACCESS ANOMALY REPORT DATA ---

1. HIGH STATISTICAL RISK FINDINGS (Users above 2x Standard Deviation threshold: {threshold:.2f} systems):
Users: {', '.join(high_risk_users) if high_risk_users else 'None detected'}
Detail: User(s) {', '.join(high_risk_users)} accessed a statistically anomalous number of unique systems in a short period. This indicates potential credential compromise or excessive privilege usage.

2. AFTER-HOURS ACCESS INCIDENTS (Outside 08:00-18:00):
{after_hours_raw}

3. NORMALIZATION CONTEXT:
Average number of unique systems accessed per user: {df.groupby('UserID')['SystemAccessed'].nunique().mean():.2f}

--- BUSINESS & COMPLIANCE CONTEXT FOR AI ---
1. Primary GRC Risk: Logical Access Control Failure (ISO 27001 A.5.15) and Insider Threat.
2. Regulatory Focus: Need to demonstrate Continuous Monitoring and strong access controls for NIS2 compliance.
"""

# Save the comprehensive data for the final prompt
with open('final_risk_data_for_claude.txt', 'w') as f:
    f.write(final_risk_data)
    
print("-" * 50)
print("SUCCESS: Anomaly detection complete.")
print(f"High-Risk Users Detected (Statistical): {high_risk_users}")
print("Final risk data compiled in 'final_risk_data_for_claude.txt'. Proceed to Step 3.")
print("-" * 50)