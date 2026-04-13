🔑 System Logs (auth.log & syslog)
📌 Objective
Capture authentication and system activity logs.

📂 Important Files
/var/log/auth.log
/var/log/syslog
🧠 Why These Logs?
Log	Detects
auth.log	SSH login, brute force
syslog	system events
🧪 Test Log Generation
Failed login simulation:
ssh wronguser@localhost
🔍 Check Logs
cat /var/log/auth.log | grep "Failed password"
📊 Expected Output
multiple failed attempts

source IP

🧠 SOC Insight
This is used for:

brute force detection

lateral movement tracking

⚠️ Common Issues
❌ log empty → SSH not enabled
❌ permission denied → use sudo