'''Control Flow, Functions, Files, JSON/CSV:
Practice Exercises
PBA Cybersikkerhed
EXTRA
coag@ek.dk'''


'''Exercise 1: Threat Level Classifier (if/elif/else)
Topics: Control flow, comparison operators, string formatting
Create a program that classifies security threats based on a numerical score:
# Threat score from monitoring system
threat_score = 75
# Your program should classify the threat based on score ranges:
# CRITICAL (90+): Immediate action required
# HIGH (70-89): Investigate within 1 hour
# MEDIUM (40-69): Review within 24 hours
# LOW (20-39): Monitor
# INFORMATIONAL (below 20): No action needed
#
# Print the classification level and its action message
# Include the actual score value in your output
# Example: "Score 75: HIGH - Investigate within 1 hour"
Expected skills: if/elif/else statements, comparison operators
'''

def ex1(threat_score = 75):
    if threat_score > 90:
        print("CRITICAL (90+): Immediate action required")
    elif threat_score >= 70:
         print("HIGH (70-89): Investigate within 1 hour")
    elif threat_score >= 40:
        print("MEDIUM (40-69): Review within 24 hours")
    elif threat_score >=20:
        print("LOW (20-39): Monitor")
    else:
        print("INFORMATIONAL (below 20): No action needed")


'''Exercise 2: Port Classifier (match-case)
Topics: Match-case statement, pattern matching
Create a port classification system using match-case:
# Port number to analyze
port = 443
# Your program should use match-case to classify:
# 22 → "SSH - Secure Shell"
# 80 → "HTTP - Web Traffic (Unencrypted)"
# 443 → "HTTPS - Secure Web Traffic"
# 3306 → "MySQL - Database"
# 3389 → "RDP - Remote Desktop"
# 53 → "DNS - Domain Name System"
# _ (default) → "Unknown Port"
#
# Print the port number and its classification
Expected skills: match-case statement, default case handling
'''

def ex2(port: int=443):
    match port:
        case 22: print("SSH - Secure Shell")
        case 80: print("HTTP - Web Traffic (Unencrypted)")
        case 443: print("HTTPS - Secure Web Traffic")
        case 3306: print("MySQL - Database")
        case 3389: print("RDP - Remote Desktop")
        case 53: print("DNS - Domain Name System")
        case _: print("Unknown Port")


'''Exercise 3: Password Retry System (while loop)
Topics: While loops, counters, boolean conditions
Create a password verification system with limited attempts:
# Correct password stored in system
correct_password = "Cyber2026!"
attempts = 0
max_attempts = 3
# Your program should:
# 1. Use a while loop to allow up to 3 attempts
# 2. Ask user for password input (use input() function)
# 3. Check if password matches correct_password
# 4. If correct: print "Access granted" and exit loop
# 5. If wrong: increment attempts, show remaining attempts
# 6. If max attempts reached: print "Account locked"
Expected skills: while loops, break statement, input validation
'''

def ex3():
    correct_password = "Cyber2026!"
    attempts = 0
    max_attempts = 3

    while (attempts <= max_attempts):
        cand = input("Type password")
        if cand == correct_password:
            print("Access granted")
            return
        attempts += 1
    print("Account locked")

    
'''Exercise 4: IP Scanner (for loop with range)
Topics: For loops, range function, string formatting
Create a simple IP address scanner simulation:
# Network to scan: 192.168.1.1 to 192.168.1.20
# Your program should:
# 1. Use a for loop with range(1, 21)
# 2. Print "Scanning 192.168.1.X..." for each IP
# 3. For IPs ending in 5, 10, 15: print " → Device found!"
# 4. For IP ending in 13: print " → SUSPICIOUS DEVICE!" and break
# 5. Count total IPs scanned before breaking
Expected skills: for loops, range(), break, conditionals in loops
'''

def ex4():
    network_range = range(1,21)
    count = 0

    for i in network_range:
        count += 1
        print(f"Scanning 192.168.1.{i}...", end="")
        if i in [5, 10, 15]:
            print(" → Device found!")
        if i == 13:
            print(" → SUSPICIOUS DEVICE!")
    print(f"Scanned {count} networks.")


'''Exercise 5: Log Filter (for loop with continue)
Topics: For loops, continue statement, lists
Process security logs and filter out noise:'''

security_logs = [
"User login successful",
"Test log entry",
"Failed login attempt from 10.0.0.5",
"System reboot",
"Test connection",
"Malware detected on endpoint",
"Test data sync",
"Unauthorized access attempt"
]


'''# Your program should:
# 1. Loop through all log entries
# 2. Use continue to skip any entry containing "Test"
# 3. Print remaining entries with line numbers
# 4. Count how many entries were processed (not skipped)
# 5. Count how many were skipped
Expected skills: for loops, continue, string methods, counters
'''

def ex5(logs=security_logs):
    count_skipped = 0
    count = 0
    for id, log in enumerate(logs):
        if "test" in log.lower():
            count_skipped += 1
            continue
        count += 1
        print(f"{id} - {log}")


'''Exercise 6: Security Check Function
Topics: Functions, parameters, return values, boolean logic
Create a function to validate security configurations:
# Define a function called check_security_config
# Parameters: firewall_enabled (bool), antivirus_updated (bool), encryption_on (bool)
# Return: True if ALL three are True, False otherwise
#
# Your function should:
# 1. Take three boolean parameters
# 2. Return True only if all three are enabled
# 3. Print a warning message if any check fails
# Test your function with:
# check_security_config(True, True, True)
 # Should return True
# check_security_config(True, False, True)
 # Should return False
# check_security_config(False, False, False) # Should return False
Expected skills: Function definition, parameters, return values, boolean logic
'''

def check_security_config(firewall_enabled:bool, antivirus_updated:bool, encryption_on:bool) -> bool:
    res = all(locals().values())
    if not res: print("oh no")
    return res


'''Exercise 7: Calculate Risk Score Function
Topics: Functions, return values, mathematical operations
Create a function to calculate security risk scores:
# Define a function called calculate_risk_score
# Parameters: vulnerabilities (int), open_ports (int), failed_logins (int)
# Formula: (vulnerabilities * 10) + (open_ports * 2) + (failed_logins * 5)
# Return: integer risk score
#
# Your program should:
# 1. Define the function with the formula above
# 2. Add type hints for parameters and return value
# 3. Test with: calculate_risk_score(3, 15, 8)
 # Should return 100
# Bonus: Add default parameter values of 0 for all parameters
Expected skills: Functions, mathematical operations, type hints, default values
'''

def calculate_risk_score(vulnerabilities: int=0, open_ports: int=0, failed_logins: int=0) -> int:
    risk = (vulnerabilities * 10) + (open_ports * 2) + (failed_logins * 5)
    return risk

risk = calculate_risk_score(3, 15, 8)
assert risk == 100

'''Exercise 8: Safe Division with Exception Handling
Topics: Exception handling, try/except, functions
Create a safe division function with error handling:
# Define a function called safe_divide
# Parameters: numerator, denominator
# Return: result of division or None if error occurs
#
# Your program should:
# 1. Use try/except to catch ZeroDivisionError
# 2. If division by zero: print error message, return None
# 3. If successful: return the result
# 4. Use finally to print "Division attempt complete"
# Test with:
# print(safe_divide(10, 2))
# print(safe_divide(10, 0))
# Should return 5.0
# Should return None with error message
Expected skills: try/except/finally, exception handling, functions
'''
def safe_divide(numerator: int|float, denominator:int|float)->float|None:
    try:
        res = numerator / denominator
        return res
    except ZeroDivisionError as e:
        print(e)
        return None 
    finally:
        print("Division attempt complete")


'''Exercise 9: Reading Security Alerts from File
Topics: File reading, pathlib, with statement
Read and process a text file containing security alerts:
# First, create a file called "alerts.txt" with these lines:'''
# Login failed from 192.168.1.50
# Malware detected on workstation-05
# System update completed
# Suspicious outbound traffic detected
'''# Your program should:
# 1. Use pathlib to get current working directory
# 2. Create filepath using Path.cwd().joinpath("alerts.txt")
# 3. Open file with "with" statement
# 4. Read and print each line
# 5. Count total lines read
# 6. Print lines containing "detected" or "failed“
Expected skills: File reading, pathlib module, with statement, string methods
'''
from pathlib import Path

def ex9():
    p = Path.cwd().joinpath("alerts.txt")
    count = 0

    with open(p, 'r') as file:
        for line in file.readlines():
            print(line)
            count += 1
            if "detected" in line.lower() or "failed" in line.lower():
                print(line)




'''Exercise 10: Writing Incident Log
Topics: File writing, append mode, timestamps
Create a function that logs security incidents to a file:
# Define a function called log_incident
# Parameters: incident_type (str), description (str)
#
# Your program should:
# 1. Open "incident_log.txt" in append mode ('a')
# 2. Write incident in format: "[TYPE] Description"
# 3. Add a newline after each entry
# 4. Close file properly (use with statement)
# Test with:
# log_incident("MALWARE", "Trojan detected on endpoint")
# log_incident("ACCESS", "Unauthorized login attempt")
# log_incident("NETWORK", "Port scan detected")
# Then read the file back and print all incidents
Expected skills: File writing, append mode, functions, with statement
'''

def log_incident(incident_type:str, description:str):
    with open ("incident_log.txt", 'a') as file:
        file.write(f"{incident_type.upper()} {description}")
        file.write("")



'''
Comprehensive(11-13)
Exercises
'''

'''Exercise 11: Security Event Processor
Topics: Functions, loops, conditionals, file operations
Create a complete security event processing system:
# Part 1: Create helper functions
# Function 1: is_critical_event(event_type) -> bool
'''

def is_critical_event(event_type) -> bool:
     return event_type in ["MALWARE", "BREACH", "INTRUSION"]


''' Function 2: generate_alert_id() -> str 
Returns a string like "ALT-001", incrementing each call
#  Hint: Use a global counter variable #'''

# sam opgaven er formuleret, antager jeg et max på 999

counter = 0
def generate_alert_id() -> str:
    global counter
    counter += 1

    result = "ALT-"
    
    match len(str(counter)):
        case 1: result += "00"
        case 2: result += "0"
        
    return result + str(counter) 


# Function 3: process_event(event_type, source_ip, description) -> dict
#  Returns a dictionary with keys: alert_id, event_type, source_ip, description, is_critical'''

def process_event(event_type, source_ip, description) -> dict:
    res = {"alert_id" : generate_alert_id(),
           "event_type" : event_type,
           "source_ip" : source_ip,
           "description" : description,
           "is_critical" : is_critical_event(event_type)}

    return res


# Part 2: Process multiple events
events = [
("LOGIN_FAIL", "192.168.1.100", "Failed authentication"),
("MALWARE", "192.168.1.105", "Ransomware detected"),
("UPDATE", "10.0.0.1", "System patch applied"),
("INTRUSION", "203.0.113.5", "Unauthorized access attempt")
]
'''
# Your program should:
# 1. Loop through events list
# 2. Use process_event() to create alert dictionary for each
# 3. Store all alerts in a list
# 4. Count critical vs non-critical alerts
# 5. Print all critical alerts with their alert_id'''

def process_multiple_events(events: list) -> list:
    alerts = []
    for event in events:
        alerts.append(process_event(*event))

    count_critical = 0
    count_non_critical = 0
    for a in alerts:
        if a["is_critical"]:
            count_critical += 1
            print(json.dumps(a, indent=4))
        else:
            count_non_critical += 1

    return alerts



'''# Part 3: Save to file
# Write all critical alerts to "critical_alerts.txt"
# Format: "[ALERT_ID] TYPE from IP: Description“
Expected skills: Functions, dictionaries, loops, file writing, global variables
'''
import json

def write_to_csv(alerts: list, out:str="critical_alerts.txt") -> None:
    with open (out, mode='w') as file:
        file.writelines(json.dumps(alerts))



'''Exercise 12: JSON Threat Intelligence Parser
Topics: JSON, file operations, dictionaries, loops
Work with JSON formatted threat intelligence data:
# Part 1: Create threat data
# Create a file "threat_intel.json" with this structure:

# Part 2: Read and analyze
# Your program should:
# 1. Read the JSON file
# 2. Count total threats
# 3. Count threats by severity level (create a dictionary)
# 4. Find all unique source IPs (use a set)
# 5. Print all "high" or "critical" threats with their IDs'''
from collections import Counter


def ex12():
    with open("threat_intel.json", 'r') as file:
        js = json.load(file)
    threats = js["threats"]
    count = 0
    count_critical = 0
    for threat in threats:
        print(threat)
        count+=1


    print(count)

#ex12()

'''
# Part 3: Add new threat
# Create a new threat dictionary:'''

new_threat = {
    "threat_id": "THR-004",
    "type": "ransomware",
    "severity": "critical",
    "indicators": ["encrypt.exe", "ransom.note"],
    "source_ips": ["10.0.0.50"]
}

def ex12_part3():
    with open("threat_intel.json", 'r') as file:
        j = json.load(file)
    j["threats"].append(new_threat)
    j = json.dumps(j, indent=2)
    with open("threat_intel.json", 'w') as file:
        file.write(j)

#ex12_part3()

'''
# Add it to the threats list and write back to JSON file
# Use indent=2 for readable formatting
Expected skills: JSON operations, dictionaries, lists, sets, file I/O
'''

'''Exercise 13: CSV Security Report Generator
Topics: CSV, file operations, loops, data processing
Create a system to generate and analyze CSV security reports:
# Part 1: Create sample data
# Create "security_report.csv" with these columns:
# timestamp, event_type, severity, source_ip, destination_ip, action_taken
# Sample data (write this to CSV):'''

import csv

sample_data = [
    ["2026-03-27 08:15:00", "login_failed", "medium", "192.168.1.50", "10.0.0.1", "blocked"],
    ["2026-03-27 08:20:00", "malware", "critical", "192.168.1.105", "10.0.0.5", "quarantined"],
    ["2026-03-27 08:25:00", "port_scan", "high", "203.0.113.10", "10.0.0.1", "blocked"],
    ["2026-03-27 08:30:00", "login_success", "low", "192.168.1.20", "10.0.0.1", "allowed"],
    ["2026-03-27 08:35:00", "data_exfil", "critical", "192.168.1.105", "8.8.8.8", "blocked"]
]


def ex13_1():
    with open("security_report.csv", 'w') as file:
        header = ["timestamp", "event_type", "severity", "source_ip", "destination_ip", "action_taken"]
        csv_writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        csv_writer.writerow(header)
        
        csv_writer.writerows(sample_data)
    
ex13_1()

'''
# Part 2: Write CSV file
# Your program should:
# 1. Use csv.writer to create the file
# 2. Write header row
# 3. Write all data rows
# Part 3: Read and analyze CSV
# Your program should:
# 1. Use csv.reader or csv.DictReader to read the file
# 2. Count events by severity (create severity_counts dict)
# 3. Find all unique source IPs that were blocked
# 4. Count total critical events
# 5. Create a list of all malware and data_exfil events'''

from collections import Counter

def ex13_3():
    severity_counts = dict()
    unique_ip = set()
    count_critical = 0
    malware_and_data_exfil_events = []

    with open("security_report.csv", 'r') as file:
        csv_data = csv.DictReader(file)
        for row in csv_data:
            sev = row["severity"]
            severity_counts[sev] = severity_counts.get(sev, 0) + 1

            unique_ip.add(row["source_ip"])
            
            if sev.lower() == "critical":
                count_critical += 1

            if row["event_type"] == "malware" or row["event_type"] == "data_exfil":
                malware_and_data_exfil_events.append(row)
            


    y = (Counter(severity_counts).most_common())
    print(unique_ip)
    print(count_critical)
    print(malware_and_data_exfil_events)


    with open ("summary_report.csv", 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['severity', 'count'])
        csv_writer.writerows(sorted(severity_counts.items()))

ex13_3()
'''
# Part 4: Generate summary report
# Write a new CSV file "summary_report.csv" with:
# severity, count
# Example:
# critical, 2
# high, 1
# medium, 1
# low, 1
Expected skills: CSV reading/writing, dictionaries, loops, data aggregation
'''