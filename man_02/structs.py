from dataclasses import dataclass

@dataclass
class alert:
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
class incident:
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


def create_alert_dataclass(_alert):
    tmp = alert(
        alert_id = _alert["alertId"], 
        category = _alert["category"], 
        computer_dns_name = _alert["computerDnsName"], 
        detection_source = _alert["detectionSource"], 
        entities = _alert["entities"],
        first_seen = _alert["firstSeen"], 
        last_seen = _alert["lastSeen"], 
        machine_id = _alert["machineId"], 
        severity = _alert["severity"], 
        title = _alert["title"]
    )
    return tmp


def convert_to_incident_dc(_incident):
    tmp = incident(
        incident_id = _incident["incidentId"],
        incident_name = _incident["incidentName"],
        created_time = _incident["createdTime"],
        last_updated_time = _incident["lastUpdateTime"],
        status = _incident["status"],
        severity = _incident["severity"],
        classification = _incident["classification"],
        determination = _incident["determination"],
        assigned_to = _incident["assignedTo"],
        tags = _incident["tags"],
        threat_family = _incident["threatFamily"],
        mitre_techniques = _incident["mitreTechniques"],
        impacted_entities = _incident["impactedEntities"],
        comments = _incident["comments"],
        summary = _incident["summary"],
        alerts = [] # _incident["alerts"]
    )

    for alert in _incident["alerts"]:
        tmp.alerts.append(create_alert_dataclass(alert))

    return tmp
