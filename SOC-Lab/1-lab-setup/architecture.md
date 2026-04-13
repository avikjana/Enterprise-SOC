🏗️ SOC Lab Architecture (Low-Resource Optimized)
📌 Objective
Design and implement a real-world Security Operations Center (SOC) lab capable of simulating a complete cyber attack lifecycle while operating under strict hardware constraints.

⚠️ System Constraint (IMPORTANT)
This lab is intentionally designed for:

💻 Maximum Available RAM: 8GB

❌ Avoid heavy tools like Elastic, Wazuh

✅ Use lightweight alternatives (Splunk + auditd + Suricata)

🧠 Architecture Overview
Kali Linux (Attacker)
↓
Ubuntu Server (Victim + Log Source + IDS Sensor)
↓
Host Machine (Splunk SIEM)

🎯 Design Philosophy
Instead of running everything in multiple heavy VMs, this lab:

Uses Host machine for Splunk

Combines Victim + Detection (Ubuntu)

Keeps attack machine lightweight

👉 This ensures:

No RAM crash

Smooth performance

Realistic SOC workflow

💻 Resource Allocation Strategy
Component	RAM	CPU	Reason
Kali Linux	2 GB	1 Core	Lightweight attacker
Ubuntu Server	3 GB	2 Core	Handles logs + IDS
Host (Splunk)	~3 GB	2 Core	SIEM processing
🧠 Why this allocation?
Splunk is memory-heavy → kept on host

Suricata + auditd need stable memory → given 3GB

Kali requires minimal resources

🌐 Network Design (CRITICAL)
Adapter 1 → NAT
Used for:

package installation

internet access

Adapter 2 → Host-Only
Used for:

internal lab communication

attack simulation

📡 Data Flow Explanation
Attacker (Kali) launches attack

Ubuntu:

Generates logs (auditd, auth logs)

Detects network traffic (Suricata)

Logs are forwarded to Splunk

Splunk:

detects attack

correlates logs

generates alerts

🔥 Real SOC Mapping
Lab Component	Real-World Equivalent
Kali Linux	External Threat Actor
Ubuntu	Endpoint + IDS Sensor
Splunk	SIEM Platform
✅ Expected Outcome
End-to-end attack visibility

Multi-source log collection

Detection + correlation capability

SOC-style investigation readiness

⚠️ Common Mistakes (IMPORTANT)
❌ Running Splunk inside VM → system lag/crash
❌ Allocating equal RAM to all machines
❌ Not using Host-only network