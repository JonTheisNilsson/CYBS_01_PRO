import json
import sqlite3

import requests

from structs import incident, alert

URL = r"http://164.92.167.24"
email = "joni0003@stud.ek.dk"

token = 'student-5zlzrL2_T5uHjdvymH8ccA'




def get_token():
    ''' 
    check local
    check expired
    if: request_token()
    '''
    raise NotImplemented


def request_token():
    '''  
    POST /api/auth/token
    Content-Type: application/json

    {"email": "your.name@school.dk}
    '''
    h = {"Content-Type": "application/json"}
    payload = {"email": email}
    r = requests.post(URL+"/api/auth/token", headers=h, json=payload)
    
    r = r.json()
    print(r)
    print(type(r))
    
    '''
        {"email":"joni0003@stud.ek.dk","expires_at":"2026-03-31T12:05:34.290336+00:00","expires_in_hours":13.27,"instructions":"Use this token in Authorization header: Bearer <token>","message":"Token retrieved successfully","note":"Token will expire in 13.3 hours. Request a new token if it expires.","token":"student-5zlzrL2_T5uHjdvymH8ccA"}

    '''



def request_incidents():
    ''' GET /api/incidents
    '''
    h = {"Authorization": "Bearer " + token}
    r = requests.get(URL+"/api/incidents", headers=h)
    r = r.json()
    print(r)



def request_incident(id: str= "INC1108"):
    ''' GET /api/incidents/{incidentId}
    returns the full object including all alerts and entities
    '''
    h = {"Authorization": "Bearer " + token}
    r = requests.get(URL+"/api/incidents/" + id, headers=h)
    r = r.json()
    print(r)



def get_statistics():
    ''' GET /api/incidents/summary 
    return 
    '''
    h = {"Authorization": "Bearer " + token}
    r = requests.get(URL+"/api/incidents/summary", headers=h)
    r = r.json()
    print(r)



####################

def init_db(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        alertID     TEXT,
        incidentID  TEXT,
        category    TEXT,
        machineID   TEXT,
        firstSeen   TEXT,
        timestamp   TEXT
        );"""
    )
    
    connection.commit()

def add_alert(connection, alert:alert|None=None):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO alerts (alertID,incidentID,category, machineID, firstSeen , timestamp ) VALUES (?, ?, ?, ?, ?, ?)",
        ("A", "b", 'c','d','e','f')
    )
    connection.commit()


def main():
    with sqlite3.connect("alerts.db") as connection:
        init_db(connection)
        add_alert(connection)


if __name__ == "__main__":
    main()