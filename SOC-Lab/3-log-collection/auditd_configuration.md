🔐 auditd Configuration (Host-Based Logging)
📌 Objective
Capture system-level activity such as:

command execution

privilege escalation

file access

🧠 Why auditd?
auditd is CRITICAL because:

detects sudo abuse

tracks sensitive file access

logs user behavior

👉 Without auditd → host visibility = ZERO

⚙️ Step 1: Install auditd
sudo apt install auditd audispd-plugins -y
⚙️ Step 2: Enable and start
sudo systemctl enable auditd
sudo systemctl start auditd
⚙️ Step 3: Verify
sudo systemctl status auditd
📂 Log Location
/var/log/audit/audit.log
🔥 Step 4: Add Custom Rules (VERY IMPORTANT)
Edit rules file:

sudo nano /etc/audit/rules.d/audit.rules
✨ Add these rules:
-w /etc/passwd -p wa -k passwd_changes
-w /etc/shadow -p wa -k shadow_access
-w /bin/su -p x -k privilege_escalation
-w /usr/bin/sudo -p x -k sudo_usage
🧠 What These Do?
Rule	Detects
/etc/passwd	user changes
/etc/shadow	credential access
sudo	privilege escalation
su	root switching
🔁 Restart auditd
sudo systemctl restart auditd
🧪 Test Detection
Run:

sudo cat /etc/shadow
🔍 Check Logs
sudo ausearch -k shadow_access
📊 Expected Output
Event showing file access

user, timestamp, command

🧠 SOC Insight
This helps detect:

credential dumping

insider threats

⚠️ Common Issues
❌ No logs → rules not loaded
❌ Permission denied → not root
