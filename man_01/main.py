import json
import csv

with open ("incident.json", 'r') as file: 
    report = json.load(file)

alerts = report["alerts"]

with (open("csv1.csv", 'w') as csv1,
      open("csv2.csv", 'w') as csv2,
      open("csv3.csv", 'w') as csv3,
      open("csv4.csv", 'w') as csv4):

    csv_writer1 = csv.writer(csv1, quoting=csv.QUOTE_ALL)
    csv_writer2 = csv.writer(csv2, quoting=csv.QUOTE_ALL)
    csv_writer3 = csv.writer(csv3, quoting=csv.QUOTE_ALL)
    csv_writer4 = csv.writer(csv4, quoting=csv.QUOTE_ALL)

    csv_writer1.writerow(["alertId", "machineId", "firstActivity", "domains"])
    csv_writer2.writerow(["alertId", "machineId", "firstActivity", "fileHashes"])
    csv_writer3.writerow(["alertId", "machineId", "firstActivity", "ips"])
    csv_writer4.writerow(["alertId", "machineId", "firstActivity", "processes"])

    for alert in alerts:
        alert_id = alert["alertId"]
        machine_id = alert["machineId"]
        first_activity = alert["firstActivity"]

        for domain in alert["entities"]["domains"]:
            csv_writer1.writerow([alert_id, machine_id, first_activity, domain])

        for file_hash in alert["entities"]["fileHashes"]:
            csv_writer2.writerow([alert_id, machine_id, first_activity, file_hash])

        for ip in alert["entities"]["ips"]:
            csv_writer3.writerow([alert_id, machine_id, first_activity, ip])

        for process in alert["entities"]["processes"]:
            csv_writer4.writerow([alert_id, machine_id, first_activity, process])
