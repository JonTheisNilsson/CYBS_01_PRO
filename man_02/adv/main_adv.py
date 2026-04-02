import json
import sqlite3
from datetime import datetime
import time
import pprint

from requests import post, get, Response
from pygments import highlight, lexers, formatters


from structs import Incident, Alert, convert_to_incident_dc
import db


def get_token(url: str, email: str) -> str:
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
        expires_at = datetime.fromisoformat(expires_at)
        print(expires_at)
    except Exception as err:
        token = None

    if token is None or expires_at.timestamp() < datetime.now().timestamp():  ## todo: test sammenligning af datetime
        r = request_token(url, email).json()
        print("new token requested")
        with open("token", 'w') as file:
            
            file.write(json.dumps(r, indent=4))
        token = r["token"]

    print("token got")
    return token


def request_token(url: str, email: str) -> Response:
    '''  
    POST /api/auth/token
    Content-Type: application/json

    {"email": "your.name@school.dk}
    '''
    h = {"Content-Type": "application/json"}
    r = post(url + "/api/auth/token", headers=h, json={"email": email})
    
    return r


def get_all_incidents(url: str, token: str) -> list[Incident]:
    incidents = []

    r = get_statistics(url, token)
    r = r.json()
    incidents_left = r['total_incidents']
    
    incidents_left = 5
    
    skip = 0

    while(incidents_left > 0):
        print("left:",incidents_left)

        if incidents_left > 100:
            top = 100
        else:
            top = incidents_left 

        response = request_incidents(url, token, top=top, skip=skip)
        response = response.json()
        incidents_left -= top
        skip += 100

        print(len(response["value"]))

        # convert to dataclasses
        for incident in response["value"]:
            incidents.append(convert_to_incident_dc(incident))
        
        print("wait")
        time.sleep(1.5)

    return incidents


def request_incidents(url: str, token: str, top=10, skip=0) -> Response:
    # GET /api/incidents
    
    h = {"Authorization": "Bearer " + token}
    payload ={"$top": top,
              "$skip": skip}
    r = get(url + "/api/incidents", headers=h, params=payload)

    return r


def request_incident(url: str, token: str, id: str= "INC1108") -> Response:
    # GET /api/incidents/{incidentId}
 
    h = {"Authorization": "Bearer " + token}
    r = get(url + "/api/incidents/" + id, headers=h)

    return r
    

def get_statistics(url: str, token: str) -> Response:
    # GET /api/incidents/summary 

    h = {"Authorization": "Bearer " + token}
    r = get(url + "/api/incidents/summary", headers=h)

    return r


def output_json_to_terminal(r) -> None:
    r = json.dumps(r, indent=4)
    colorful_json = highlight(r, lexers.JsonLexer(), formatters.TerminalFormatter())
    print(colorful_json)


def output_json_to_file(data, path="output.txt") -> None:
    data = json.dumps(data, indent=4)
    with open(path,'w') as output: output.write(data)


def output_dc_to_file(data, path="output.txt") -> None:
    with open(path,'w') as output: output.write(pprint.pformat(data))


def output_to_db(incidents, database="alerts.db") -> None:
    with sqlite3.connect(database) as connection:
        db.init_db(connection)

        for incident in incidents:
            for alert in incident.alerts:
                db.add_alert(connection, alert, incident.incident_id)


def main() -> None:
    url = r"http://164.92.167.24"
    email = "joni0003@stud.ek.dk"
    token = 'student-5zlzrL2_T5uHjdvymH8ccA'

    token = get_token(url, email)
    
    '''
    r = request_incident(url, token)
    r = r.json()
    
    output_dc_to_file(r)'''

    incidents = get_all_incidents(url, token)

    i = incidents[0]
    print(i.comments)

    output_dc_to_file(incidents, "test.txt")

    #pprint.pp(incidents)
    #output_to_db(incidents)


if __name__ == "__main__":
    main()