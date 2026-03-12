import csv
import json

'''Opgave 1: Læs den hemmelige besked (Basic File Read)
1. Opret en tekstfil manuelt på din computer (f.eks. i Notepad) og kald den
secret.txt. Skriv en hemmelig besked i filen og gem den samme sted som
dit Python-script.
2. Skriv et Python-script, der åbner filen i læse-tilstand ("r"), læser alt
indholdet og printer det til konsollen.'''

def opg1():
    with open("uge_10_secret.txt", 'r') as file:
        print(file.read())

#opg1()

'''Opgave 2: Blacklist (Write & Append)
1. Lav et script, der åbner en fil kaldet blacklist.txt i skrive-tilstand og skriver
"192.168.1.100" i den.
2. Tilføj derefter en ny IP-adresse "10.0.0.5" til den samme fil, men denne
gang uden at slette den første IP. Brug append-tilstand. Husk linjeskift.'''

def opg2():
    with open("uge_10_blacklist.txt", 'w') as file:
        file.write("192.168.1.100")
    with open("uge_10_blacklist.txt", 'a') as file:
        file.write("\n10.0.0.5")
        
#opg2()


'''Opgave 3: Robust Filhåndtering (File Exceptions)
Opgave: Du skal forsøge at læse en fil, som ikke eksisterer, men uden at
programmet crasher.
1. Forsøg at åbne filen missing_data.txt i læsetilstand.
2. Brug en try-except blok til specifikt at fange en FileNotFoundError.
3. Hvis fejlen opstår, skal programmet blot printe: "Fejl: Filen kunne ikke
findes!" i stedet for at crashe.'''

def opg3():
    try:
        with open("missing_data.txt", 'r'):
            pass
    except FileNotFoundError as err:
        print("Fejl: Filen kunne ikke findes!")

#opg3()

'''Opgave 4: Firewall Log Analysatoren (CSV) pt. 1
Opgavebeskrivelse: Du har en firewall-log i CSV-format, og du skal finde alle
blokerede IP'er.
CSV indhold:
firewall_data = [
['timestamp', 'source_ip', 'destination_ip', 'port', 'action', 'threat_level'],
['2025-09-16 10:30:15', '192.168.1.50', '203.0.113.25', '443', 'blocked',
'medium'],
['2025-09-16 10:31:22', '10.0.0.100', 'malicious-site.com', '80', 'allowed',
'high'],
['2025-09-16 10:32:45', '192.168.1.75', '8.8.8.8', '53', 'allowed', 'low']
]'''

'''Opgave 4: Firewall Log Analysatoren (CSV) pt. 2
Del 1: Forberedelse og indlæsning
Importer csv modulet. Åbn en fil kaldet firewall.csv i læse-tilstand. Brug
csv.reader() til at læse filen og print alle rækker ved hjælp af et for-loop.
Del 2: Skip Headeren
CSV-filer har ofte en overskrift på første linje. Brug funktionen
next(reader_variabel) til at springe overskriften over, før du looper igennem
resten.
Del 3: Filtrer "blocked"
Opdater dit for-loop. Hvis 'action' (f.eks. index 1 i din CSV-række) er lig med
"blocked", skal du printe rækken.'''

def opg4():
    with open("uge_10_firewall_log.csv", 'r') as file:
        csv_reader = csv.reader(file)
        csv_reader.__next__()
        for i in csv_reader:
            if i[4] == "blocked":
                print(", ".join(i))

#opg4()

'''Opgave 5: Konfigurations-Manageren (JSON) pt. 1
Opgavebeskrivelse: Du skal ændre konfigurationen på en server automatisk
ved hjælp af et script.
Del 1: Læs JSON
Opret først en tekstfil config.json og skriv dette i den: {"server": "Ubuntu",
"port": 80}. Brug Python-modulet json og json.load() funktionen til at læse
filen ind som et Python-Dictionary og print port-nummeret.'''

'''Opgave 5: Konfigurations-Manageren (JSON) pt. 2
Del 2: Opdater Data
I din kode skal du nu ændre porten i dit Dictionary fra 80 til 443 (den sikre
port) og tilføje et nyt key-value par: "secure_mode": True.
Del 3: Skriv JSON tilbage
Brug json.dump() til at skrive dit opdaterede Dictionary til en ny fil kaldet
config_secure.json. Sørg for at tilføje parameteren indent=4 for at gøre filen
pæn og læselig.'''

def opg5():
    with open("uge_10_config.json", 'r') as file:
        config = json.load(file)
        print(config["port"])

        config["port"] = 443
        config["secure_mode"] = True

    with open("uge_10_config_secure.json", 'w') as f:
        json.dump(config, f, indent=4)
    
opg5()