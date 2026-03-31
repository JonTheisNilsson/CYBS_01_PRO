import datetime

import structs

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


def add_alert(connection, a:structs.alert, incident_id:str):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO alerts (alertID, incidentID, category, machineID, firstSeen, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
        (a.alert_id, incident_id, a.category, a.machine_id, a.first_seen, datetime.datetime.now())
    )
    connection.commit()