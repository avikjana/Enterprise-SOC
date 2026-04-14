# 🌐 IP Enrichment Script (VirusTotal / AbuseIPDB)

## 📌 Objective

Automatically enrich suspicious IP addresses.

---

## 🧠 Why?

SOC analysts need:

* IP reputation
* threat intelligence

---

## ⚙️ Script

```python
import requests

API_KEY = "YOUR_API_KEY"

def check_ip(ip):
    url = f"https://api.abuseipdb.com/api/v2/check"
    
    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }
    
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"\nIP: {ip}")
        print(f"Abuse Score: {data['data']['abuseConfidenceScore']}")
    else:
        print("Error fetching data")

# Example
check_ip("8.8.8.8")
```

---

## ✅ Output

* IP reputation score
* helps in investigation

---

## 🚀 Usage

```bash
python ip_enrichment.py
```
