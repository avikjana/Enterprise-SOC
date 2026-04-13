🛡️ Suricata Configuration (Network IDS)
📌 Objective
Monitor network traffic and detect malicious activity.

🧠 Why Suricata?
Detects reverse shell traffic

Detects scanning (nmap)

Detects suspicious connections

👉 auditd = host visibility
👉 Suricata = network visibility

⚙️ Step 1: Install Suricata
sudo apt install suricata -y
⚙️ Step 2: Identify Interface
ip a
👉 Look for Host-only interface (e.g., enp0s8)

⚙️ Step 3: Configure Suricata
sudo nano /etc/suricata/suricata.yaml
Change interface:
af-packet:
  - interface: enp0s8
⚙️ Step 4: Start Suricata
sudo systemctl start suricata
📂 Log Location
/var/log/suricata/eve.json
🧪 Test Detection
From Kali:

nmap <ubuntu-ip>
🔍 Check Logs
cat /var/log/suricata/eve.json
📊 Expected Output
alerts about scanning

source IP (Kali)

🧠 SOC Insight
Suricata helps detect:

reconnaissance

C2 traffic

suspicious connections

⚠️ Common Issues
❌ No logs → wrong interface
❌ service not running