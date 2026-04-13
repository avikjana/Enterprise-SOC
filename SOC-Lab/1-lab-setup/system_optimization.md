 System Optimization (LOW RAM SURVIVAL GUIDE)
📌 Objective
Optimize entire SOC lab to run smoothly within 8GB RAM constraint

⚠️ Reality Check
Without optimization:
❌ VM lag
❌ Splunk crash
❌ Suricata drop packets

🧠 Optimization Strategy
Reduce memory usage

Disable unnecessary services

Use lightweight configurations

🖥️ Ubuntu Optimization
Step 1: Disable GUI (if installed)
sudo systemctl set-default multi-user.target
👉 WHY: Saves ~500MB RAM

Step 2: Disable unused services
sudo systemctl disable bluetooth
sudo systemctl disable cups
Step 3: Reduce Swappiness
sudo sysctl vm.swappiness=10
🐉 Kali Optimization
Use terminal-based tools only
❌ Avoid:

Burp Suite

Metasploit GUI

✅ Use:

netcat

nmap

hydra

📊 Splunk Optimization
Limit memory usage
Edit:

$SPLUNK_HOME/etc/system/local/server.conf
Add:

[general]
parallelIngestionPipelines = 1
Reduce indexing load
Only ingest required logs

Avoid unnecessary data sources

🔥 Suricata Optimization
Edit config:

sudo nano /etc/suricata/suricata.yaml
Reduce:

threads

logging verbosity

🧠 Golden Rule
👉 “Run only what is needed”

✅ Expected Outcome
Smooth VM performance

No lag

Stable detection

⚠️ Common Mistakes
❌ Running all tools at once
❌ Using GUI everywhere
❌ Ignoring RAM usage