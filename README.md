# 🚨 SOC Lab – Real-World SOC Simulation (Low-Resource Optimized)

GoSOC Lab is a **practical Security Operations Center (SOC) simulation** designed to replicate real-world attack detection and response workflows.

The lab demonstrates how a SOC analyst:

* collects logs
* detects threats
* correlates events
* investigates incidents

All within a **low-resource environment (8GB RAM)**.

---

## ⚠️ System Constraint & Design Approach

This lab was built under the following constraint:

* **Maximum RAM Available: 8GB**

### 🧠 Design Decisions

| Challenge             | Approach                             |
| --------------------- | ------------------------------------ |
| Limited RAM           | Avoided heavy tools (Elastic, Wazuh) |
| Need SIEM             | Used Splunk on host (not VM)         |
| Need detection + logs | Combined roles in Ubuntu             |
| Maintain realism      | Used attacker–victim–SIEM model      |

---

## 🏗️ Detailed Architecture

```id="arch1"
Kali Linux (Attacker VM)
        ↓
Ubuntu Server (Victim + Log Source + IDS)
        ↓
Splunk SIEM (Host Machine)
```

---

### 🔹 1. Kali Linux (Attacker)

* Role: Simulates real-world attacker behavior
* Tools Used:

  * netcat → reverse shell
  * nmap → network scanning
  * hydra → brute force

👉 Generates attack traffic and malicious activity

---

### 🔹 2. Ubuntu Server (Victim + Detection Layer)

Acts as **central monitored system**

#### Responsibilities:

* Executes attacker payloads
* Generates logs
* Runs IDS

#### Components:

**1. auditd**

* Tracks:

  * command execution
  * privilege escalation
  * file access
