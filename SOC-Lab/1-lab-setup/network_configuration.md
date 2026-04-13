🌐 Network Configuration (MOST CRITICAL)
📌 Objective
Ensure proper communication between:

Kali (attacker)

Ubuntu (victim)

Splunk (SIEM)

⚠️ Why This Matters
Without proper network:
❌ No attack simulation
❌ No log forwarding
❌ No SOC workflow

🧠 Network Design
Use Dual Adapter Setup

🔧 Configuration (VirtualBox)
For BOTH Kali & Ubuntu:
Adapter 1:
Mode: NAT

Purpose: Internet access

Adapter 2:
Mode: Host-Only Adapter

Name: vboxnet0

🧪 Verify IP Address
Run on both machines:

ip a
Example Output
Kali → 192.168.56.101

Ubuntu → 192.168.56.102

🔁 Connectivity Test
From Kali:
ping 192.168.56.102
From Ubuntu:
ping 192.168.56.101
✅ Expected Output
Ping successful

No packet loss

🔥 Splunk Connectivity
Ubuntu → send logs to host:

Check host IP:

ipconfig   # Windows
⚠️ Common Issues
❌ Host-only adapter missing
❌ Wrong network selected
❌ IP not assigned
