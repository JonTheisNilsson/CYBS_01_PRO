import json
import sqlite3
from datetime import datetime
import time
import sys

import requests
from requests import Response

import db


def get_token(url: str, email: str) -> str:
    try:
        with open ("token", 'r') as file: 
            token_object = json.load(file)

        token = token_object["token"]
        expires_at = token_object["expires_at"]
        expires_at = datetime.fromisoformat(expires_at)
        
    except Exception as err:
        print("failure to find token", err)  # catch-all
        token = None

    if expires_at.timestamp() < datetime.now().timestamp():  # todo: test sammenligning af datetime
        print("token expired")
        token = None

    if token is None:  
        print("new token requested")
        response = request_token(url, email)
        response = response.json()
        
        with open("token", 'w') as file:
            file.write(json.dumps(response, indent=4))
        token = response["token"]

    print("token got")
    return token


# test: headeren burde være overflødig siden vi sætter den med json=
def request_token(url: str, email: str) -> Response:
    '''  
    POST /api/auth/token
    Content-Type: application/json

    {"email": "your.name@school.dk}
    '''
    h = {"Content-Type": "application/json"}
    r = requests.post(url + "/api/auth/token", headers=h, json={"email": email})
    
    return r


def get_all_incidents(url: str, token: str):
    incidents = []
    skip = 0
    retry = True

    while(True):
        try:
            response = request_incidents(url, token, top=100, skip=skip)
        except requests.exceptions.Timeout as err:
            if retry: 
                print("Timeout. Retrying in 5 sec")
                time.sleep(5)
                retry = False
                continue

            print("Timeout. Retried once", file=sys.stderr)
            raise SystemExit(1)
        except requests.HTTPError as err:
            print("http error", file=sys.stderr)
            raise SystemExit(1)
        except requests.RequestException as err:
            print("RequestException", file=sys.stderr)
            raise SystemExit(1)
        except Exception as err:
            print("oh no, my {err}", file=sys.stderr)
            raise SystemExit(1)      
                
        response = response.json()

        for i in response["value"]:
            incidents.append(i)

        if "@odata.nextLink" in response:
            skip += 100
            print("wait")
            time.sleep(1.5)
        else:
            break

    return incidents


def request_incidents(url: str, token: str, top=10, skip=0) -> Response:
    # GET /api/incidents
    
    h = {"Authorization": "Bearer " + token}
    payload ={"$top": top,
              "$skip": skip}
    r = requests.get(url + "/api/incidents", headers=h, params=payload)

    return r


def output_to_db(incidents, database="alerts.db") -> None:
    try:
        with sqlite3.connect(database) as connection:
            db.init_db(connection)
        
            for incident in incidents:
                for alert in incident["alerts"]:
                    db.add_alert(connection, alert, incident["incidentId"])
    except Exception as err:
        print("db error. attempting rollback")
        connection.rollback()


def main() -> None:
    url = r"http://164.92.167.24"
    email = "joni0003@stud.ek.dk"

    token = get_token(url, email)
    
    incidents = get_all_incidents(url, token)

    output_to_db(incidents, "simple.db")


if __name__ == "__main__":
    main()