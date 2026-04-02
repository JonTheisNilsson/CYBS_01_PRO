from dataclasses import dataclass

@dataclass
class Alert:
    alert_id: str
    title: str
    category: str
    severity: str
    detection_source: str
    machine_id: str
    computer_dns_name: str
    first_seen: str
    last_seen: str
    entities: dict[str,str]


@dataclass
class Incident:
    incident_id: str
    incident_name: str
    created_time: str
    last_updated_time: str
    status: str
    severity: str
    classification: str
    determination: str
    assigned_to: str | None
    tags: list[str]
    threat_family: str
    mitre_techniques: list[str]
    impacted_entities: dict[str,int]
    comments: list[dict[str,str]]
    summary: str
    alerts: list


def create_alert_dataclass(alert):
    tmp = Alert(
        alert_id = alert["alertId"], 
        category = alert["category"], 
        computer_dns_name = alert["computerDnsName"], 
        detection_source = alert["detectionSource"], 
        entities = alert["entities"],
        first_seen = alert["firstSeen"], 
        last_seen = alert["lastSeen"], 
        machine_id = alert["machineId"], 
        severity = alert["severity"], 
        title = alert["title"]
    )
    return tmp


def convert_to_incident_dc(incident):
    tmp = Incident(
        incident_id = incident["incidentId"],
        incident_name = incident["incidentName"],
        created_time = incident["createdTime"],
        last_updated_time = incident["lastUpdateTime"],
        status = incident["status"],
        severity = incident["severity"],
        classification = incident["classification"],
        determination = incident["determination"],
        assigned_to = incident["assignedTo"],
        tags = incident["tags"],
        threat_family = incident["threatFamily"],
        mitre_techniques = incident["mitreTechniques"],
        impacted_entities = incident["impactedEntities"],
        comments = incident["comments"],
        summary = incident["summary"],
        alerts = []
    )

    for alert in incident["alerts"]:
        tmp.alerts.append(create_alert_dataclass(alert))

    return tmp
