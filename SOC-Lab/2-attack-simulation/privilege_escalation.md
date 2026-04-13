⬆️ Privilege Escalation – Sudo Abuse
📌 Objective
Gain root access from a normal user account.

🧠 Why This?
Attackers aim to:

gain full control

bypass restrictions

⚙️ Step 1: Check sudo permissions
sudo -l
⚙️ Step 2: Abuse sudo
Example:

sudo /bin/bash
💥 Result
Root shell obtained

🧪 Verify
whoami
👉 Output: root

📊 Logs Generated
sudo logs

auth logs

auditd privilege events

🎯 MITRE Mapping
T1068 → Privilege Escalation