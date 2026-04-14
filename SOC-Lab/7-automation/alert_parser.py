# 📊 Alert Parser

## 📌 Objective

Extract useful data from Splunk alerts

---

```python
import json

def parse_alert(file):
    with open(file) as f:
        data = json.load(f)
    
    for event in data:
        print("Time:", event.get("_time"))
        print("Host:", event.get("host"))
        print("User:", event.get("user"))
        print("-"*30)

parse_alert("alerts.json")
```
