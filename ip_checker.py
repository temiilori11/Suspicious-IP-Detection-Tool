import csv
import requests
import json

API_KEY = "ENTER YOUR API KEY"
API_URL = "https://api.abuseipdb.com/api/v2/check"

def check_ip(ip):
    try:
        params = {
            "ipAddress": ip,
            "maxAgeInDays": 90
        }
        headers = {
            "Key": API_KEY,
            "Accept": "application/json"
        }

        response = requests.get(API_URL, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()["data"]
        else:
            return {"error": "API error"}
    except Exception as e:
        return {"error": str(e)}

def main():
    results = []

    with open("connections.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            ip = row["RemoteAddress"]

            # ignore empty or local addresses
            if ip == "0.0.0.0" or ip == "::" or ip.strip() == "":
                continue

            print(f"Checking IP: {ip}")
            data = check_ip(ip)

            results.append({
                "ProcessName": row["ProcessName"],
                "IP": ip,
                "AbuseConfidence": data.get("abuseConfidenceScore", "N/A"),
                "TotalReports": data.get("totalReports", "N/A"),
                "IsPublic": data.get("isPublic", "N/A")
            })

    with open("analysis_report.json", "w") as outfile:
        json.dump(results, outfile, indent=4)

    print("Report saved as analysis_report.json")

if __name__ == "__main__":
    main()
