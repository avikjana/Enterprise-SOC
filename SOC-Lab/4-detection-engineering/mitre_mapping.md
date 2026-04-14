🧠 MITRE ATT&CK Mapping
📌 Objective

Map each detection rule to real-world attacker techniques.

🎯 Why Important?
Industry standard framework
Helps in:
threat coverage analysis
SOC reporting
detection gaps identification
📊 Mapping Table
Attack Stage	Technique	MITRE ID	Detection
Initial Access	Command Execution	T1059	Reverse Shell
Priv Esc	Sudo Abuse	T1068	Priv Esc Detection
Credential Dump	Shadow Access	T1003	Credential Dump
Lateral Movement	SSH Brute Force	T1110	Brute Force
Persistence	Cron Job	T1053	Persistence
🧠 SOC Insight

👉 A good SOC analyst always thinks in:

“Technique” not just “attack”