📊 Splunk Setup (SIEM on Host Machine)
📌 Objective
Install and configure Splunk SIEM on host machine to:

collect logs

detect threats

create alerts

visualize attacks

⚠️ Why Splunk on Host (IMPORTANT)
Given:

Total RAM = 8GB

❌ Running Splunk inside VM → system crash
✅ Running Splunk on host → better performance

💻 Minimum Requirements
RAM: ~3GB available

OS: Windows/Linux (host machine)

🛠️ Installation Steps
Step 1: Download Splunk
Go to:
👉 Splunk official website

Download:

Splunk Enterprise (Free Trial)

Step 2: Install Splunk
Follow GUI installer (Next → Next → Finish)

Step 3: Start Splunk
Open in browser:

http://localhost:8000
Step 4: Login
Username: admin

Password: (set during install)

⚙️ Initial Configuration
Step 1: Add Data Input
Go to:
Settings → Data Inputs → Add New

Step 2: Enable Receiving Port
Port: 9997

👉 WHY:

Universal Forwarder logs will come here

📦 Install Universal Forwarder (Ubuntu)
(Full config later in logs section)

🧠 How Splunk Works (Simple)
Logs come from Ubuntu

Splunk indexes data

Search queries detect threats

Alerts are triggered

🧪 Test Splunk
Search:

index=_internal
✅ Expected Output
Logs visible in search

No errors

⚠️ Common Issues
❌ Port not open → logs not received
❌ Firewall blocking 9997
❌ Splunk not running

⚡ Optimization Tips
Disable unnecessary apps in Splunk

Use only required indexes

Avoid heavy dashboards initially