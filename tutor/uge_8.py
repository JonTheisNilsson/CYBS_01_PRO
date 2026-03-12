'''Opgave 1: Firewall Rules
Opgave: Lav et program, der beder brugeren indtaste et portnummer (husk
int()).
1. Hvis porten er 80, print "Allow HTTP traffic".
2. Hvis porten er 443, print "Allow HTTPS traffic".
3. Hvis porten er 22, print "Allow SSH traffic".
4. For alle andre porte, print "Block traffic".'''

def opg1():
    match(input("Input port number: ")):
        case "80": print("Allow HTTP traffic")
        case "443": print("Allow HTTPS traffic")
        case "22": print ("Allow SSH traffic")
        case _ : print("Block traffic")


'''Opgave 2: Bruteforce Menu
Opgave: Lav en while True: løkke, der kører uendeligt indtil brugeren vil stoppe.
1. Inde i løkken skal du bede brugeren indtaste en kommando: "start", "stop"
eller "exit"
2. Brug match-case (eller if/elif) til at håndtere inputtet:
Case "start": Print "Starting services...".
Case "stop": Print "Stopping services...".
Case "exit": Print "Goodbye!" og brug break eller exit() til at stoppe løkken.
Case _: Print "Unknown command".'''

'''Opgave 3: Port Scanner Simulator
Her skal du bruge loops inde i loops (nested loops) til at generere data,
præcis som beskrevet i afsnittet om loops,.
1. Lav en liste af servere: servers = ["Server-A", "Server-B"]
2. Lav en liste af porte: ports = [20 , 21 , 22 , 80 , 443]
3. Lav et nested loop (et loop inde i et loop):
Det ydre loop skal køre gennem servers.
Det indre loop skal køre gennem ports.
4. For hver kombination skal du printe: "Scanning [server] on port [port]..."
5. Hvis porten er 22, skal du printe " -> SSH Open" og bruge continue til at
springe til næste port.'''

def opg_3():
    servers = ["Server-A", "Server-B"]
    ports = [20 , 21 , 22 , 80 , 443]

    for server in servers:
        for port in ports:
            print(f"Scanning {server} on port {port}...")
            if port == 22:
                print(" -> SSH Open") 
                #continue

#opg_3()

'''Opgave 4: Data & statistics
Her skal du rense en liste med dubletter og forkerte datatyper, og derefter
lave beregninger.
• Data: data_stream = [13 , 27 , 35 , 43 , 59 , "ERROR" , 27 , 59 , "ERROR" ,
43]
• Opgave:
1. Opret en tom liste clean_data.
2. Loop gennem data_stream.
3. Brug try/except(eller andet) til kun at acceptere tal. Hvis det er tekst
som "ERROR", skal det springes over (brug continue).
4. Konverter alle tal til float og tilføj dem til clean_data.
5. Konverter clean_data til et Set for at fjerne dubletter.
6. Loop gennem dit Set og beregn summen af tallene.'''

def opg_4():
    data_stream = [13 , 27 , 35 , 43 , 59 , "ERROR" , 27 , 59 , "ERROR" , 43]
    clean_data = []
    for data in data_stream:
        if type(data) == int:
            clean_data.append(float(data))
    clean_data = set(clean_data)

    sum = 0
    for i in clean_data:
        sum += i
    print (sum)

#opg_4()

'''Opgave 5: The Network Traffic Analyzer[pt. 1]
Scenarie: Du er sikkerhedsanalytiker. Du skal bygge et script, der kører
uendeligt og lader brugeren indtaste rå log-data. Systemet skal automatisk
tjekke, om IP-adresserne er kendte "skurke", og gemme dataene struktureret
til senere analyse.'''

'''Opgave 5: The Network Traffic Analyzer[pt. 2]
Opsætning af Data (Sets & Lists)
1. Opret et Set kaldet blocked_ips. Fyld det med tre "farlige" IP-adresser.
blocked_ips = {"10.10.10.5", "192.168.0.99", "172.16.0.5"}
2. Opret en tom Liste kaldet traffic_log. Denne skal bruges til at gemme alle
godkendte log-indgange.'''

'''Opgave 5: The Network Traffic Analyzer[pt. 3]
Hovedprogrammet (While Loop)
3. Start en uendelig loop, der holder programmet kørende.
4. Inde i dit loop skal du printe en menu:
◦ 1. Indtast log
◦ 2. Vis analyse
◦ 3. Afslut
5. Bed brugeren vælge et tal (brug input()).
Logik og Datahåndtering (Match-Case & String Methods)
Brug en match-case (eller if-elif-
else) struktur til at håndtere brugerens valg.'''

'''Opgave 5: The Network Traffic Analyzer[pt. 4]
Case "1" (Indtast log):
• Bed brugeren indtaste en log-streng i formatet: "User:IP:Port" (f.eks.
"admin:10.10.10.5:22").
• Brug string-metoden .split(":") til at dele strengen op i tre variabler: user,
ip, port.
• Tjek IP'en:
◦ Hvis ip findes i dit blocked_ips set: Print "ALERT: Blocked IP detected!" og
gør ikke mere ved denne entry.
◦ Hvis ip ikke er blokeret:
Opret et lille Dictionary for denne hændelse: {"User": user, "IP": ip,
"Port": port}.
Tilføj dette dictionary til din traffic_log liste,.
Print "Log added successfully."'''

'''Opgave 5: The Network Traffic Analyzer[pt. 5]
Case "2" (Vis analyse):
• Tjek først om traffic_log er tom (brug len()). Hvis den er tom, print "No
data".
• Hvis der er data: Brug et For-loop til at løbe listen igennem.
• For hver entry skal du printe en pæn besked, f.eks.:
◦ "[User] accessed system from [IP] on port [Port]"
• Bonus: Tæl hvor mange gange brugeren "admin" optræder i loggen.'''

'''Opgave 5: The Network Traffic Analyzer[pt. 6]
Case "3" (Afslut):
• Print "Shutting down monitor..."
• Brug break eller exit() til at stoppe programmet'''

def opg_5():
    blocked_ips = {"10.10.10.5", "192.168.0.99", "172.16.0.5"}
    traffic_log = [{"User": "alice", "IP": "192.168.1.10", "Port": 8080},
                    {"User": "bob", "IP": "192.168.1.11", "Port": 443},
                    {"User": "admin", "IP": "10.0.0.5", "Port": 22},
                    {"User": "david", "IP": "172.16.0.2", "Port": 3306},
                    {"User": "eve", "IP": "192.168.1.12", "Port": 21},
                    {"User": "frank", "IP": "10.0.0.6", "Port": 25},
                    {"User": "grace", "IP": "172.16.0.3", "Port": 5432},
                    {"User": "heidi", "IP": "192.168.1.13", "Port": 8000},
                    {"User": "ivan", "IP": "10.0.0.7", "Port": 27017},
                    {"User": "judy", "IP": "172.16.0.4", "Port": 6379},
                    {"User": "mallory", "IP": "192.168.1.14", "Port": 1521},
                    {"User": "oscar", "IP": "10.0.0.8", "Port": 3389},
                    {"User": "peggy", "IP": "172.16.0.5", "Port": 5900},
                    {"User": "admin", "IP": "192.168.1.15", "Port": 8443},
                    {"User": "admin", "IP": "10.0.0.9", "Port": 123},
                    {"User": "wendy", "IP": "172.16.0.6", "Port": 110},
                    {"User": "xavier", "IP": "192.168.1.16", "Port": 995},
                    {"User": "yvonne", "IP": "10.0.0.10", "Port": 587},
                    {"User": "zach", "IP": "172.16.0.7", "Port": 8081},
                    {"User": "nina", "IP": "192.168.1.17", "Port": 3000},]

    def input_log():
        try:
            log = input("Input i format: \"User:IP:Port\": ")
            user, ip, port = log.split(':')
            if ip in blocked_ips:
                print("ALERT: Blocked IP detected!")
                return
            traffic_log.append({"User": user, "IP": ip, "Port": port})
            print("Log added successfully.")
        except ValueError:
            print("Invalid format")

    def show_analysis():
        admin_count = 0
        if len(traffic_log)==0:
            print("No data")
        else:
            for log in traffic_log:
                if log["User"].lower() == "admin": admin_count += 1
                print(f"{log["User"]} accessed system from {log["IP"]} on port {log["Port"]}")
        print(f"Admin count: {admin_count}")

    while(True):
        match input("1. Indtast log\n2. Vis analyse\n3. Afslut\n: "):
            case "1":
                input_log()
            case "2":
                show_analysis()
            case "3":
                print("Shutting down monitor...")
                exit()
            case _:
                print("Invalid input.")

opg_5()
