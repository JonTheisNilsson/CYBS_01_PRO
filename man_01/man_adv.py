import json
import csv
import argparse
import logging


def generate_csvs(incident_path: str = "incident.json") -> None:
    logger = setup_logger()

    try:
        with open (incident_path, 'r') as file: 
            report = json.load(file)

        logger.info(f"Loaded json file {incident_path}")

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

        logger.info(f"Wrote csv-file(s)")

    except Exception as err:
        logger.error(err)
        print(f"Oh no. My {err}")


def setup_logger(log_path = "app.log") -> logging.Logger:
    logging.basicConfig(
        filename=log_path,
        encoding="utf-8",
        filemode="a",
        format="{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",
    )

    logger = logging.getLogger("SimpleLogger")
    logger.setLevel(logging.INFO)

    return logger


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--Input", help="Path to incident json")
    args = parser.parse_args()

    if args.Input:
        generate_csvs(args.Input)
    else:
        generate_csvs()


if __name__ == "__main__":
    main()