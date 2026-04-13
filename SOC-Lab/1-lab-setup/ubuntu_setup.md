🖥️ Ubuntu Setup (Victim + Detection Machine)
📌 Objective
Configure Ubuntu as:

Target system (victim)

Log generator

Detection sensor (auditd + Suricata)

⚠️ Resource Planning (VERY IMPORTANT)
Ubuntu handles:

system logs

auditd

Suricata IDS

👉 इसलिए इसे ज्यादा RAM चाहिए

RAM: 3GB

CPU: 2 Core

⚙️ VM Configuration
RAM: 3GB

CPU: 2 Core

Disk: 25GB

🌐 Network Configuration
Adapter	Mode
Adapter 1	NAT
Adapter 2	Host-Only
🛠️ Initial Setup
Step 1: Update system
sudo apt update && sudo apt upgrade -y
Step 2: Install required packages
sudo apt install auditd net-tools curl -y
🔐 Configure auditd
Step 1: Enable service
sudo systemctl enable auditd
sudo systemctl start auditd
Step 2: Verify status
sudo systemctl status auditd
Step 3: Test log generation
sudo ausearch -m USER_LOGIN
🌐 Connectivity Check
ping <kali-ip>
🧠 Why auditd?
auditd helps in:

tracking user activity

detecting privilege escalation

monitoring file access

✅ Expected Outcome
auditd running successfully

logs being generated

connectivity established

⚠️ Common Issues
❌ auditd not running → service not enabled
❌ no logs → incorrect configuration

⚡ Optimization Tips
Disable GUI (use minimal Ubuntu)

Stop unnecessary services:

sudo systemctl disable bluetooth