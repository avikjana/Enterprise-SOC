# 🚨 Reverse Shell Investigation Playbook

## 📌 Objective

Investigate and confirm a suspected reverse shell attack.

---

## 🚨 Alert Trigger

Detection rule: `reverse_shell_detection.spl`

---

## 🧠 What Happened?

Reverse shell means:
👉 Victim machine initiated connection to attacker
👉 Attacker gained remote access

---

## 🔍 Step 1: Identify Source & Destination

### Splunk Query:

```spl
index=* ("bash -i" OR "/dev/tcp/")
| table _time host src_ip dest_ip dest_port
```

### ✔ What to Look For:

* Unusual destination IP
* Uncommon port (e.g., 4444)

---

## 🔍 Step 2: Check Process Execution

```spl
index=* "bash -i"
| table _time user process host
```

👉 Confirm suspicious command execution

---

## 🔍 Step 3: Validate Network Connection

```spl
index=* dest_port=4444
| stats count by src_ip dest_ip
```

---

## 🔍 Step 4: Verify on Ubuntu (Victim)

```bash
ps aux | grep bash
```

```bash
netstat -antp
```

👉 Check active connections

---

## 🧠 Analysis

* Outbound connection + bash execution = strong compromise indicator
* If repeated → attacker persistence possible

---

## 📊 Timeline Reconstruction

```spl
index=* host=<victim>
| sort _time
```

---

## 🧾 Root Cause

* User executed malicious command OR
* Exploited service

---

## 🚨 Response Actions

* Kill process:

```bash
kill -9 <pid>
```

* Block attacker IP
* Remove malicious scripts

---

## ✅ Conclusion

Reverse shell confirmed → **Initial Access achieved by attacker**
