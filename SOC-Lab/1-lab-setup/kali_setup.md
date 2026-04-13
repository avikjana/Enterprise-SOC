🐉 Kali Linux Setup (Attacker Machine)
📌 Objective
Configure Kali Linux as the attacker system to simulate real-world cyber attacks.

⚠️ Resource Constraint Consideration
Total system RAM = 8GB

Kali must remain lightweight

👉 इसलिए:

RAM = 2GB (sufficient for attack tools)

Avoid running heavy GUI tools

⚙️ VM Configuration
RAM: 2GB

CPU: 1 Core

Disk: 20GB (dynamically allocated)

🌐 Network Configuration
Adapter	Mode	Purpose
Adapter 1	NAT	Internet access
Adapter 2	Host-Only	Attack communication
🛠️ Initial Setup
Step 1: Update system
sudo apt update && sudo apt upgrade -y
👉 WHY: Ensure tools are updated and compatible

Step 2: Install attack tools
sudo apt install netcat nmap hydra -y
🔍 Tool Usage
Tool	Purpose
netcat	Reverse shell
nmap	Network scanning
hydra	Brute force attack
Step 3: Get IP address
ip a
👉 Note Host-Only IP (example: 192.168.56.x)

🧪 Connectivity Test
ping <ubuntu-ip>
✅ Expected Output
Successful ping response

0% packet loss

⚠️ Common Issues
❌ Cannot ping → wrong network adapter
❌ IP not showing → Host-only not configured

🧠 Optimization Tips
Disable unnecessary services

Avoid opening multiple tools simultaneously

Use terminal-based tools instead of GUI