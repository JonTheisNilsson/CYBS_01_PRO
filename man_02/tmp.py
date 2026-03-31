import structs

incident = {

'alerts': [ {
    'alertId': 'ALT-SQLI-001-0', 
    'category': 'Exploitation', 
    'computerDnsName': 'CAD01-TCORP.oresund-industrial.dk', 
    'detectionSource': 'Microsoft Defender for Endpoint', 
    'entities': { 
        'domains': ['update-oresund.com'], 
        'emails': ['eng.larsen@oresund-industrial.dk'], 
        'fileHashes': ['5d41402abc4b2a76b9719d911017c592'], 
        'ips': ['192.168.30.10', '172.16.100.10'], 
        'processes': ['python3.exe sqlm=admin\' OR \'1\'=\'1\'-- -&password=x" --dump --tables'], 
        'urls': ["http://172.16.100.http://172.16.100.10/portal/login?username=admin'--&password="]}, 
    'firstSeen': '2026-03-29T00:44:22.420566+00:00', 
    'lastSeen': '2026-03-29T02:04:22.420566+00:00', 
    'machineId': 'CAD01-TCORP', 
    'severity': 'High', 
    'title': 'SQL injection tool (sqlmap) execution detected on CAD01-TCORP'}], 
    
'assignedTo': 'soc.analyst@oresund-industrial.dk', 
'classification': 'TruePositive', 
'comments': [ {
    'comment': 'tion CAD01-TCORP.', 
    'createdBy': 'soc.analyst@oresund-industrial.dk', 
    'createdTime': '2026-03-29T02:04:22.420566+00:00'}], 
'createdTime': '2026-03-29T01:04:22.420566+00:00', 
'determination': 'MaliciousUserActivity', 
'impactedEntities': {'machines': 2, 'mailboxes': 0, 'users': 0}, 
'incidentId': 'INC-SQLI-001', 
'incidentName': 'APT28 - Web Application Attack on WEB01-TCORP', 
'lastUpdateTime': '2026-03-29T02:34:22.420566+00:00', 
'mitreTechniques': ['T1190', 'T1059.001', 'T1505.003'], 
'severity': 'High', 
'status': 'Active', 
'summary': 'APT28 gained foot web server logs.', 
'tags': ['APT28', 'Cobalt Strike', 'Øresund Industrial', 'WebAttack'], 
'threatFamily': 'Cobalt Strike'}



