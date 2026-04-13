🔐 Credential Dumping – /etc/shadow Access
📌 Objective
Extract password hashes from the system.

🧠 Why?
Attackers steal credentials for:

lateral movement

persistence

⚙️ Step 1: Dump shadow file
cat /etc/shadow
💥 Result
Password hashes exposed

📊 Logs Generated
file access logs

auditd file monitoring

🎯 MITRE Mapping
T1003 → Credential Dumping

⚠️ Important
This requires root access