CREATE TABLE IF NOT EXIXTS alerts (
id          INTEGER PRIMARY KEY AUTOINCREMENT,
alertID     TEXT,
incidentID  TEXT,
category    TEXT,
machineID   TEXT,
firstSeen   TEXT,
timestamp   TEXT
);