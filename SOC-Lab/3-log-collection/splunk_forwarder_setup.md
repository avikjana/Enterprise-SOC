📤 Splunk Forwarder Setup (Log Shipping)
📌 Objective
Send logs from Ubuntu → Splunk SIEM

🧠 Why Forwarder?
lightweight agent

real-time log shipping

industry standard

⚙️ Step 1: Download Forwarder
From:
👉 Splunk

Download:

Splunk Universal Forwarder (Linux)

⚙️ Step 2: Install
sudo dpkg -i splunkforwarder*.deb
⚙️ Step 3: Start Forwarder
sudo /opt/splunkforwarder/bin/splunk start --accept-license
⚙️ Step 4: Connect to Splunk
sudo /opt/splunkforwarder/bin/splunk add forward-server <host-ip>:9997
⚙️ Step 5: Add Log Inputs
sudo /opt/splunkforwarder/bin/splunk add monitor /var/log/auth.log
sudo /opt/splunkforwarder/bin/splunk add monitor /var/log/syslog
sudo /opt/splunkforwarder/bin/splunk add monitor /var/log/audit/audit.log
sudo /opt/splunkforwarder/bin/splunk add monitor /var/log/suricata/eve.json
🔁 Restart Forwarder
sudo /opt/splunkforwarder/bin/splunk restart
🧪 Verify in Splunk
Search:

index=* sourcetype=syslog
📊 Expected Output
logs from Ubuntu visible

multiple sources

🧠 SOC Insight
Now you have:

centralized logging

real-time monitoring

detection capability

⚠️ Common Issues
❌ logs not showing → wrong IP
❌ port closed → firewall issue