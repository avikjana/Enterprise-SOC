📡 Log Flow Architecture (SOC Data Pipeline)
📌 Objective
Understand how logs travel from:
👉 Endpoint → Detection → SIEM

🧠 Why This is IMPORTANT?
SOC kaaj actually 80% = log analysis

If log flow wrong:
❌ No detection
❌ No investigation
❌ No alerts

🔥 Log Sources in This Lab
Source	Type	Purpose
auditd	Host logs	User activity, privilege escalation
syslog/auth.log	Authentication logs	SSH, login attempts
Suricata	Network IDS	Malicious traffic detection
📡 Data Flow (Step-by-Step)
Attack happens (Kali → Ubuntu)

Ubuntu generates logs:

auditd → process + file events

auth.log → login activity

Suricata → network alerts

Logs → collected by Splunk Forwarder

Forwarder → sends logs to Splunk (Port 9997)

Splunk:

indexes logs

runs detection queries

generates alerts

🔁 Visual Flow
Ubuntu (Logs Generated)
↓
Splunk Universal Forwarder
↓
Splunk SIEM (Host)
↓
Detection & Alerts

🧠 SOC Insight
👉 Real SOC also works like this:

Multiple log sources

Central SIEM

Correlation across logs

⚠️ Common Mistakes
❌ Not forwarding all logs
❌ Wrong file path
❌ Port not open