'''Opgave 1: List Slicing & Manipulation
Opgave: Du har en liste over servere: servers = ["Server1", "Server2",
"Server3", "Server4", "Server5"]
1. Print de tre første servere ved hjælp af slicing.
2. Print de to sidste servere ved hjælp af slicing.
3. Udskift "Server3" med "Server3-Maintenance".
4. Print den opdaterede liste.'''

def opg1():
    servers = ["Server1", "Server2", "Server3", "Server4", "Server5"]
    print(servers[:3])
    print(servers[-2:])
    servers[2] = "Server3-Maintenance"
    print(servers)
    
#opg1()

'''Opgave 2: Split & Join (String Konvertering)
Opgave: Du modtager en rå data-streng fra en logfil:
log_data = "Error, Warning, Info, Critical"
1. Konverter strengen om til en liste2. Tilføj "Debug" til listen.
3. Saml listen til en ny streng igen, men denne gang skal ordene adskilles af
en bindestreg " - " i stedet for komma.
4. Print den nye streng.'''

def opg2():
    log_data = "Error, Warning, Info, Critical"
    liste2 = [w.strip() for w in log_data.split(',')]
    log_new = "-".join(liste2)
    print(log_new)

#opg2()

'''Opgave 3: Tuple Trouble (Immutability)
Opgave: Du har en tuple med godkendte IP-adresser:
allowed_ips = ("192.168.1.1", "10.0.0.1")
Du finder ud af, at du mangler "127.0.0.1".
1. Konverter din tuple til en liste.
2. Tilføj "127.0.0.1" til listen.
3. Konverter listen tilbage til en tuple.
4. Print den nye tuple for at bevise, at parenteserne () er tilbage.'''

def opg3():
    allowed_ips = ("192.168.1.1", "10.0.0.1")
    allowed_ips = list(allowed_ips)
    allowed_ips.append("127.0.0.1")
    allowed_ips = tuple(allowed_ips)
    print(allowed_ips)

#opg3()

'''Opgave 4: Dictionary Lookup (Key-Value)
Opgave: Lav en dictionary ports med følgende indhold:
"http": 80, "ssh": 22, "ftp": 21
1. Print portnummeret for "ssh" ved at slå det op direkte på nøglen.
2. Prøv at printe portnummeret for "dns" ved at bruge .get(). Hvis den ikke
findes, skal den printe teksten "Not Found".
3. Opdater din dictionary så "http" nu peger på 8080 i stedet for 80.
4. Print hele din dictionary.'''

def opg4():
    ports = {"http": 80, "ssh": 22, "ftp": 21}
    print(ports["ssh"])
    print(ports.get("dns", "Not found"))
    ports["http"] = 8080
    print(ports)
#opg4()

'''Opgave 5: Network Intrusion Detector [pt. 1]
Del 1: Rengøring af Log (Lists & String Methods)
Du modtager følgende streng af log-data:
raw_log = "admin, user1, user2, guest, hacker, admin, user1,
unknown_actor”
1. Brug split og konverter strengen til en liste.
2. Loggen indeholder dubletter (admin og user1 optræder flere gange).
Konverter listen til et Set for automatisk at fjerne dubletter og gem resultatet
i variablen unique_logins.
3. Print de unikke logins.'''

raw_log = "admin, user1, user2, guest, hacker, admin, user1, unknown_actor"
log = [w.strip() for w in raw_log.split(',')]
unique_logins = set(log)
print(unique_logins)

'''Opgave 5: Network Intrusion Detector [pt. 2]
Del 2: Identifikation af Trusler (Set Operations)
Du har en liste over godkendte brugere (Authorized Personnel):
authorized_users = {"admin", "user1", "user2", "guest"}
1. Brug Set Difference (-) til at finde de brugere, som findes i unique_logins,
men ikke i authorized_users.
2. Gem disse i en variabel kaldet intruders.
3. Print intruders for at se, hvem der er brudt ind.'''

authorized_users = {"admin", "user1", "user2", "guest"}
intruders = unique_logins - authorized_users

print(intruders)

'''Opgave 5: Network Intrusion Detector [pt. 3]
Del 3: Hændelsesrapport (Dictionaries & Tuples)
1. Opret en tom Dictionary kaldet incident_report.
2. Tilføj de fundne intruders til din dictionary manuelt. Key skal være navnet
på intruderren (f.eks. "hacker"), og value skal være trusselsniveauet "High".
3. Opret en Tuple kaldet final_evidence. Denne skal være "immutable", så
den kan bruges som bevis i retten. Tuplen skal indeholde:
◦ Datoen ("2023-10-27")
◦ Navnet på intruderen (hent det fra din dictionary ved hjælp af .keys()
◦ Navnet på systemet ("Server-Main")
4. Print både din dictionary og din bevis-tuple'''

incident_report = dict()
for i in intruders:
    incident_report[i] = "High"

final_evidence = list()
for k,v in incident_report.items():
    final_evidence.append(f"2023-10-27: {k}, Server-Main, level: {v}")

final_evidence = tuple(final_evidence)
print(incident_report)
for e in final_evidence:
    print(e)