# 🔗 Multi-Log Correlation (SOC Level)

## 📌 Objective

Correlate logs from:

* auditd
* auth.log
* Suricata

---

## 🧠 Why Important?

Single log ≠ full story
Multiple logs = **confirmed attack**

---

## 🔍 Example Correlation

### Step 1: Reverse Shell

```spl
index=* "bash -i"
```

---

### Step 2: Sudo Activity

```spl
index=* "sudo"
```

---

### Step 3: Shadow Access

```spl
index=* "/etc/shadow"
```

---

## 🔥 Combine All

```spl
index=* ("bash -i" OR "sudo" OR "/etc/shadow")
| stats count by host, user
```

---

## 🧠 Analysis

If all appear together:
👉 FULL ATTACK CONFIRMED

---

## 📊 SOC Insight

This is how real SOC:

* reduces false positives
* confirms incidents

---

## ✅ Outcome

* Better detection accuracy
* Strong investigation evidence
