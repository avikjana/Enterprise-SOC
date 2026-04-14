# 🔐 Credential Dumping Investigation

## 📌 Objective

Investigate access to sensitive credential files.

---

## 🚨 Alert Trigger

`credential_dumping_detection.spl`

---

## 🧠 What Happened?

Attacker accessed:
👉 `/etc/shadow` → password hashes

---

## 🔍 Step 1: Detect File Access

```spl
index=* "/etc/shadow"
| table _time user host
```

---

## 🔍 Step 2: Identify User

👉 Check if:

* root → expected
* normal user → suspicious

---

## 🔍 Step 3: Validate via auditd

```bash
sudo ausearch -k shadow_access
```

---

## 🔍 Step 4: Check Command Used

```spl
index=* "cat /etc/shadow"
```

---

## 🧠 Analysis

* If combined with privilege escalation → confirmed attack chain
* Possible credential theft

---

## 📊 Timeline

```spl
index=* "/etc/shadow"
| sort _time
```

---

## 🚨 Response

* Force password reset
* Monitor login attempts
* Enable stricter access control

---

## ✅ Conclusion

Credential dumping confirmed → **Sensitive data exposure**
