'''
import sys

count = 0
print("test")
print("oh no, my {err}", file=sys.stderr)
raise SystemExit(1)  

def is_critical_event(event_type) -> bool:
     return event_type in ["MALWARE", "BREACH", "INTRUSION"]

counter = 0
def generate_alert_id() -> str:
    global counter
    counter += 1

    result = "ALT-"
    
    match len(str(counter)):
        case 1: result += "00"
        case 2: result += "0"
    return result + str(counter) 
        

def process_event(event_type, source_ip, description) -> dict:
    res = {"alert_id" : generate_alert_id(),
           "event_type" : event_type,
           "source_ip" : source_ip,
           "description" : description,
           "is_critical" : is_critical_event(event_type)}

    return res

events = [
("LOGIN_FAIL", "192.168.1.100", "Failed authentication"),
("MALWARE", "192.168.1.105", "Ransomware detected"),
("UPDATE", "10.0.0.1", "System patch applied"),
("INTRUSION", "203.0.113.5", "Unauthorized access attempt")
]

def process_multiple_events(events: list) -> list:
    alerts = []
    for event in events:
        alerts.append(process_event(*event))
    return alerts

alerts = process_multiple_events(events)

for i in events:
    print(*i)
'''

import json

tmp = {
"threat_id": "THR-003",
"type": "ddos",
"severity": "critical",
"indicators": ["flood-attack"],
"source_ips": ["192.0.2.100", "192.0.2.101", "192.0.2.102"]
}

print(json.dumps(tmp, indent=2))