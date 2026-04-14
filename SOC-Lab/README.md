# 🚨 SOC Lab – Real-World SOC Simulation (Low-Resource Optimized)

## 📌 Overview

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

**2. System Logs (auth.log, syslog)**

* Tracks:

  * SSH logins
  * failed authentication
  * system activity

**3. Suricata (IDS)**

* Monitors:

  * network traffic
  * scanning activity
  * suspicious connections

---

### 🔹 3. Splunk (SIEM – Host Machine)

* Central log analysis platform
* Performs:

  * log ingestion
  * indexing
  * detection (SPL queries)
  * alert generation
  * dashboard visualization

👉 Running on host reduces VM memory load

---

## 🌐 Network Architecture

Each VM uses **dual network interfaces**:

### Adapter 1 → NAT

* Internet access (updates, tools)

### Adapter 2 → Host-Only

* Internal communication:

  * Kali ↔ Ubuntu ↔ Splunk

---

## 📡 Log Flow Pipeline

```id="arch2"
Attack (Kali)
   ↓
Logs Generated (Ubuntu)
   ↓
Splunk Universal Forwarder
   ↓
Splunk SIEM (Host)
   ↓
Detection → Correlation → Alerts
```

---

## ⚔️ Attack Lifecycle Simulated

| Stage                | Description               |
| -------------------- | ------------------------- |
| Initial Access       | Reverse shell established |
| Privilege Escalation | Sudo abuse to gain root   |
| Credential Dumping   | Access to /etc/shadow     |
| Lateral Movement     | SSH brute-force attempts  |
| Persistence          | Cron job backdoor         |

---

## 🔍 Detection Engineering

The lab includes multiple detection rules based on:

* command execution patterns
* authentication anomalies
* file access monitoring
* network activity

All detections are mapped to **MITRE ATT&CK techniques**.

---

## 🔗 Correlation Strategy

Instead of relying on single alerts, the lab implements:

* multi-log correlation
* timeline-based analysis
* attack chain reconstruction

This allows:

* better accuracy
* reduced false positives
* full attack visibility

---

## 🧪 Investigation Workflow

Each alert is investigated using:

1. Splunk search queries
2. Host-level validation commands
3. Timeline reconstruction
4. Root cause analysis

---

## ⚙️ Automation

Basic SOC automation is implemented using Python:

* IP reputation enrichment
* alert parsing
* incident report generation

---

## 📊 Dashboards

Custom dashboards provide:

* alert distribution
* attack timeline
* top source IPs
* detection coverage

---

## 📈 SOC Metrics

The lab tracks:

* Mean Time to Detect (MTTD)
* Mean Time to Respond (MTTR)
* Alert volume
* Detection coverage

---

## 📁 Project Structure

```id="fs1"
SOC-Lab/
│
├── 1-lab-setup/
├── 2-attack-simulation/
├── 3-log-collection/
├── 4-detection-engineering/
├── 5-correlation/
├── 6-investigation-playbooks/
├── 7-automation/
├── 8-dashboards/
├── 9-metrics/
├── screenshots/
│
├── README.md
└── requirements.txt
```

---

## 📦 Requirements

### 🔧 System Requirements

* 8GB RAM (minimum)
* Oracle VirtualBox

---

### 🧰 Software Requirements

* Kali Linux
* Ubuntu Server
* Splunk Enterprise
* Suricata
* auditd

---

### 🐍 Python Requirements

```id="req1"
requests
```

Install using:

```id="req2"
pip install -r requirements.txt
```

---

## 📌 Key Highlights

* Lightweight SOC lab (8GB optimized)
* Real-world attack simulation
* Multi-source log analysis
* Detection + correlation + investigation
* Practical SOC workflow implementation

---

## 📸 Screenshots

* Attack execution
* Log ingestion
* Detection alerts
* Correlation results
* Dashboard view

---

## 📌 Conclusion

This project demonstrates a **complete SOC pipeline**, from attack simulation to detection and investigation, using a resource-efficient architecture aligned with real-world practices.

---
