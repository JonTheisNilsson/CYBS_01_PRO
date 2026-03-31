import json
import sqlite3
import datetime
import time

import requests

from structs import incident, alert, convert_to_incident_dc
import db


def get_token(url, email) -> str:
    ''' 
    check local
    check expired
    if: request_token()
    '''
    try:
        with open ("token", 'r') as file: 
            token_object = json.load(file)

        token = token_object["token"]
        expires_at = token_object["expires_at"]
        expires_at = datetime.datetime.fromisoformat(expires_at)
        print(expires_at)
    except Exception as err:
        token = None

    if token is None or expires_at.timestamp() < datetime.datetime.now().timestamp():  ## todo: test sammenligning af datetime
        r = request_token(url, email)
        print("new token requested")
        with open("token", 'w') as file:
            
            file.write(json.dumps(r, indent=4))
        token = r["token"]

    print("token got")
    return token


def request_token(url, email):
    '''  
    POST /api/auth/token
    Content-Type: application/json

    {"email": "your.name@school.dk}
    '''
    h = {"Content-Type": "application/json"}
    r = requests.post(url + "/api/auth/token", headers=h, json={"email": email})
    
    r = r.json()

    return r


def get_all_incidents(url, token)-> list[incident]:
    incidents = []

    number_of_incidents = 205  ## todo: get from stats
    left = number_of_incidents
    skip = 0

    while(left > 0):
        print("left:",left)

        if left > 100:
            top = 100
        else:
            top = left 

        response = request_incidents(url, token, top=top, skip=skip)
        json = response.json()
        left -= top
        skip += 100

        print(len(json["value"]))

        # convert to dataclasses
        for incident in json["value"]:
            incidents.append(convert_to_incident_dc(incident))

        print("wait")
        time.sleep(1.5)

    return incidents


def request_incidents(url, token, top=10, skip=0):
    # GET /api/incidents
    
    h = {"Authorization": "Bearer " + token}
    payload ={"$top": top,
              "$skip": skip}
    r = requests.get(url + "/api/incidents", headers=h, params=payload)

    return r


def request_incident(url, token, id: str= "INC1108"):
    # GET /api/incidents/{incidentId}
 
    h = {"Authorization": "Bearer " + token}
    r = requests.get(url + "/api/incidents/" + id, headers=h)

    return r
    

def get_statistics(url, token):
    # GET /api/incidents/summary 

    h = {"Authorization": "Bearer " + token}
    r = requests.get(url + "/api/incidents/summary", headers=h)

    return r


def main():
    url = r"http://164.92.167.24"
    email = "joni0003@stud.ek.dk"
    token = 'student-5zlzrL2_T5uHjdvymH8ccA'

    token = get_token(url, email)
    
    
    incidents = get_all_incidents(url, token)



    with sqlite3.connect("alerts.db") as connection:
        db.init_db(connection)

        for incident in incidents:
            for alert in incident.alerts:
                db.add_alert(connection, alert, incident.incident_id)



if __name__ == "__main__":
    main()