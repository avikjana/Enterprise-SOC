⚔️ Attack Simulation Overview
📌 Objective
Simulate a complete cyber attack lifecycle to test SOC detection and response capabilities.

🧠 Attack Chain (Real-World Inspired)
Initial Access → Reverse Shell

Privilege Escalation → Sudo Abuse

Credential Dumping → /etc/shadow access

Lateral Movement → SSH brute-force

Persistence → Cron Job

🎯 Why This Scenario?
This attack chain mimics:

Real attacker behavior

Multiple MITRE ATT&CK techniques

Multi-stage compromise

🔥 Attack Flow
Kali (Attacker)
↓
Gain access to Ubuntu
↓
Escalate privileges
↓
Steal credentials
↓
Maintain persistence

🧠 SOC Perspective
Each stage generates:

logs

alerts

indicators

👉 Used for:

detection

correlation

investigation

⚠️ Important Notes
Perform attacks ONLY inside lab

Monitor logs continuously

Take screenshots