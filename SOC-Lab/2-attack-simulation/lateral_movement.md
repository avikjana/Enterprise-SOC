 Lateral Movement – SSH Brute Force
📌 Objective
Move to another system using stolen credentials.

🧠 Why?
Attackers expand access across network.

⚙️ Step 1: Use Hydra (Kali)
hydra -l user -P passwords.txt ssh://<target-ip>
💥 Result
Successful login

📊 Logs Generated
multiple failed logins

SSH logs

🎯 MITRE Mapping
T1110 → Brute Force