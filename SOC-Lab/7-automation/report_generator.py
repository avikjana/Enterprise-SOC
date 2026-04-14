# 🧾 Incident Report Generator

## 📌 Objective

Generate simple SOC incident report

---

```python
def generate_report(incident):
    with open("report.txt", "w") as f:
        f.write("=== SOC INCIDENT REPORT ===\n")
        f.write(f"Incident: {incident}\n")
        f.write("Status: Confirmed Attack\n")
        f.write("Severity: High\n")

generate_report("Reverse Shell Attack")
```
