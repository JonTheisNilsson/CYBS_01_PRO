'''
Tutor_opgaver [Input og Concatenation]
Opgavebeskrivelse: Du skal lave et script, der simulerer en simpel log-besked.
1. Bed brugeren indtaste et brugernavn.
2. Bed brugeren indtaste en IP-adresse.
3. Opret en variabel log_entry, der sammensætter disse oplysninger til en
advarselstekst på formatet: "ALERT: User [brugernavn] accessed system from
[IP-adresse]"
4. Print log_entry.
'''
print("Tutor_opgaver [Input og Concatenation]")

bruger_navn = input("Indtast brugernavn: ")
ip = input("Intast ip-adresse: ")
log_entry = f"ALERT: User {bruger_navn} accessed system from {ip}"
print(log_entry)

print()
'''
Tutor_opgaver [Matematik og Modulus]
Opgavebeskrivelse: En server har været oppe i et bestemt antal minutter, f.eks.
total_minutes = 135. Du skal lave et program, der omregner dette til timer og
minutter.
1. Definer variablen total_minutes (sæt den til 135).
2. Beregn hvor mange hele timer det svarer til.
3. Beregn hvor mange minutter der er til rest.
4. Print resultatet på formen: "Server uptime: X timer og Y minutter".
'''
print("Tutor_opgaver [Matematik og Modulus]")

total_minutes = 135
timer = 135 // 60
rest = 135 % 60
print(f"Server uptime: {timer} timer og {rest} minutter.")

print()
'''
Tutor_opgaver [String Metoder]
Opgavebeskrivelse: Lav en variabel url og sæt den til "https://ek.dk/login".
Programmet skal:
1. Printe længden af URL'en.
2. Tjekke om protokollen "https" findes i URL'en (skal printe True/False).
3. Konvertere hele URL'en til store bogstaver (UPPERCASE) og printe den.
4. Udskifte "login" med "logout" ved hjælp af replace() metoden og printe den
nye URL.
'''
print("Tutor_opgaver [String Metoder]")

url = "https://ek.dk/login"
print(len(url))
print("http" in url)
print(url.upper())
url = url.replace("login", "logout")
print(url)

print()
'''
Tutor_opgaver [Split og Join]
Opgavebeskrivelse: Du har en variabel med en IP-adresse: ip_raw = "192.168.0.1".
1. Brug split til at dele IP-adressen op ved hvert punktum, så du får en liste af
tallene.
2. Print listen.
3. Print typen af din nye variabel for at bevise, det er en list.
4. Saml listen igen til en enkelt streng, men denne gang skal tallene være adskilt
af bindestreger (-) i stedet for punktummer.
5. Print den nye streng.
'''
print("Tutor_opgaver [Split og Join]")

ip_raw = "192.168.0.1"
ip = ip_raw.split('.')
print(ip)
print(type(ip))
ip_new = "-".join(ip)
print(ip_new)