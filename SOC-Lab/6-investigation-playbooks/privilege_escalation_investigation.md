# ⬆️ Privilege Escalation Investigation

## 📌 Objective

Investigate unauthorized privilege escalation.

---

## 🚨 Alert Trigger

`privilege_escalation_detection.spl`

---

## 🧠 What Happened?

User gained **root access** using sudo or exploit.

---

## 🔍 Step 1: Identify Sudo Usage

```spl
index=* "sudo"
| table _time user command host
```

---

## 🔍 Step 2: Check Suspicious Commands

👉 Look for:

* `/bin/bash`
* unusual binaries

---

## 🔍 Step 3: Verify User Behavior

```spl
index=* user!=root "sudo"
```

---

## 🔍 Step 4: Validate on System

```bash
whoami
```

```bash
sudo -l
```

---

## 🧠 Analysis

* Normal admin activity vs suspicious escalation
* Time-based anomalies (late night activity)

---

## 📊 Timeline

```spl
index=* "sudo"
| sort _time
```

---

## 🚨 Response

* Remove sudo privileges
* Reset user password
* Review user activity

---

## ✅ Conclusion

Privilege escalation detected → **Attacker gained elevated control**
