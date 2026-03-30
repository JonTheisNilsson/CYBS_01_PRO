from dataclasses import dataclass

@dataclass
class alert:
    alert_id:int
    title: str
    category: str
    severity: str
    detection_source: str
    machine_id: str
    computer_dns_name: str
    first_activity: str
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
    summery: str
    alerts = list[alert]