import os
import csv
import json 
from pathlib import Path

import requests

#print(__file__)
#print(os.path.dirname(__file__))

'''Exercise: Pip it
Practice installing and using the requests library for cybersecurity API calls
Requirements
• Install the requests library using pip: pip install requests
• Write Python code to:
• Import the requests module
• Make a GET request to http://157.230.127.213/
• Print the response status code
• Print the JSON response (your public IP)
• Expected Output
• Status Code: 200
• Response: {'origin': '20.50.2.66'}

hint: use requests.get(url) to make the request
use .status_code
use .json()'''

url =  "http://157.230.127.213/"

def opg1():
    request = requests.get(url)
    print(f"Status code: {request.status_code}")
    print(f"Response: {request.json()}")

#opg1()

'''Exercise: JSON Security Alert
Read a security alert from JSON and display key information
• Create a new file, name it alert.json with this content and structure: as shown on the figure:
{
"alert_id": "ALT-001",
"severity": "high",
"source_ip": "192.168.1.100",
"alert_type": "malware_detected"
}
• Now write a Python program security_warnings that execute these commands:
• Read the JSON file
• Print: "Alert ALT-001: HIGH severity malware_detected from 192.168.1.100"
'''

def opg2():
    try:
        path = Path(os.path.dirname(__file__)) / r"ex9_alert.json"

        with open(path, 'r') as file:
            alert = json.load(file)

            print(f"{alert["alert_id"]}: {alert["severity"].upper()} severity {alert["alert_type"]} from {alert["source_ip"]}")
    except Exception as err:
        print(f"Oh no: {err}")

#opg2()

'''
Exercise: Threat Intelligence Processing
Process threat intelligence data from JSON and export filtered results to CSV
Task for your Python code:
• Read the threat intelligence file from threat_intel.json (get it from link below!)
• Filter for threats with confidence > 80 and serverity = "high"
• Export filtered threats to a file: high-priority-threats.csv
• Print total count of high priority threats found
Expected output format (CSV):
IOC,Type,Severity,Confidence,Last_Seen
192.168.1.100,ip,high,95,2025-09-15T14:30:00Z
malware.example.com,domain,high,88,2025-09-16T09:15:00Z

remember to include headers in your csv output
use a for loop to process each threat indicator

Get the threat intelligence file from:
https://raw.githubusercontent.com/JHB-EK/python_1sem/refs/heads/main/threat_intel.json'''

def opg3():
    try:
        path = Path(os.path.dirname(__file__)) / r"ex9_threat.json"
        filtered_data = list()

        with open(path, 'r') as file:
            file = json.load(file)
            for l in file["indicators"]:
                if l["confidence"] > 80 and l["severity"].lower() == "high":
                    filtered_data.append(l)
                    
            print(f"total count of high priority threats found: {len(filtered_data)}")
            
        csv_output = "IOC,Type,Severity,Confidence,Last_Seen\n"
        for t in filtered_data:
            csv_output += f"{t["ioc_value"]},{t["ioc_type"]},{t["severity"]},{t["confidence"]},{t["last_seen"]}\n"
            
        with open("ex9_out.csv", 'w') as ofile:
            ofile.write(csv_output)
    except Exception as err:
        print(f"Oh no: {err}")

#opg3()    

def opg3csv():
    try:
        path = Path(os.path.dirname(__file__)) / r"ex9_threat.json"
        filtered_data = list()

        with open(path, 'r') as file:
            file = json.load(file)
            for l in file["indicators"]:
                if l["confidence"] > 80 and l["severity"].lower() == "high":
                    intel = [v for k, v in l.items() if k != "description"]
                    filtered_data.append(intel[1:-1])
                    
            print(f"total count of high priority threats found: {len(filtered_data)}")
                
        with open("ex9_out2.csv", 'w', newline='') as ofile:
            csv_writer = csv.writer(ofile)
            csv_writer.writerow(["IOC","Type","Severity","Confidence","Last_Seen"])
            csv_writer.writerows(filtered_data)
            
    except Exception as err:
        print(f"Oh no: {err}")

opg3csv()


def opg3web():
    try:
        url = "https://raw.githubusercontent.com/JHB-EK/python_1sem/refs/heads/main/threat_intel.json"
        request = requests.get(url)
        content = request.text
        content = json.loads(content)

        filtered_data = list()

        for l in content["indicators"]:
            if l["confidence"] > 80 and l["severity"].lower() == "high":
                intel = [v for k, v in l.items() if k != "description"]
                filtered_data.append(intel[1:-1])
                    
        print(f"total count of high priority threats found: {len(filtered_data)}")
                
        with open("ex9_out3.csv", 'w', newline='') as ofile:
            csv_writer = csv.writer(ofile)
            csv_writer.writerow(["IOC","Type","Severity","Confidence","Last_Seen"])
            csv_writer.writerows(filtered_data)
        
    except Exception as err:
        print(f"Oh no: {err}")

#opg3web()