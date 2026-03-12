def print_table(x:int=10, y:int=10)->None:
    for i in range(x):
        for j in range(y):
            print((i+1) * (j+1), end="\t")
        print()
        
def print_table_proper(x:int=10, y:int=10)->None:
    digits = len(str(x * y))

    for i in range(x):
        for j in range(y):
            res = str((i+1) * (j+1))
            while (len(res) < digits): res = " " + res
            print(res, end="\t")
        print()

#print_table()
#print()
print_table_proper(10, 10)

#print_table()
#print()
#print_table(5,7)
#print()
#print_table(y=7, x=5)


'''Exercise: Iteration with collections: Mail_Sweep
Make a program Detect_anormaly and make 3 strings called mail_one, mail_two, mail_three
containing the strings from the red box below. Now add som code that:
• Create an empty set for Eavesdropped Mail Communication called emc
• Add the three strings and when doing this convert them to lists with default delimiter
• For each mail check if it contains the word ”bomb” you must print:
Suspecious mail found! The contents says: <print the mail as a string>
'''

mail_one, mail_two, mail_three, mail_four = "Hello, how are you? Regards, Alice", "Urgent: The package contains a bomb. Act now!", "Meeting reminder: Tomorrow at 10 AM", "Security alert: Do not open the bomb threat email."
mails = [mail_one, mail_two, mail_three, mail_four]

def detect_anormaly(_mails:list[str]=list())-> set[str]:
    emc:set[str] = set()

    for mail in _mails:
        if "bomb" in mail.lower():
            print(f"Suspecious mail found! The contents says: \"{mail}\"")
        emc.update(mail.split())
    return emc

#print((detect_anormaly(mails)))