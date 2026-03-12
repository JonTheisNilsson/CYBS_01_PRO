''' Exercise: Okay let's look at that Car class…
Create a class named 'Car'
Create a program that will use this class called car_broker
• The Car class should have a constructor that take color, year, model, brand as parameters
• The Car class should have a method called print_info()
• From the broker program create car1 and car2 with som parameters
• Print the info
• Test if you can change year for car1?'''

def opg1():
    class Car:
        def __init__(self, _color: str="", _year: int=-1, _model: str="", _brand: str=""):
            self.color = _color
            self.year = _year
            self.model = _model
            self.brand = _brand

        def print_info(self): 
            print(f"Info: {self}")

        def __str__(self):
            return f"{self.color} {self.year} {self.model} {self.brand}"

        def __repr__(self):
            return f"{self.__class__.__name__}: {self}"


    car1 = Car("brun",1946, "v10", "volvo" )
    car2 = Car("gul",1846, "v20", "bolvo")

    car1.print_info()
    car2.print_info()
    car1.year = 3
    car1.print_info()
    print(car1)
    print(repr(car1))
    x = 5
    print(f"{x=}")
    print(dir(car1))

opg1()

'''Exercise: The Book_shop
Make a program, Book_shop with an empty dictionary called “book_prices”
Add some code so your program execute following tasks:
• Add three books and their prices (see table on the right)
• Print out the price of “Cyber Security”
• Access a book ”Web Design” not in the dictionary using .get()
• Update the price of “Basic Python” to 200
• Add a new book to the list of your choice
• Delete “Cyber Security” from your dictionary
• Check if “Cyber Security” still exists
• Check if “Network Security” still exists
Between each step, it is recommended to print the dictionary to keep track of your changes'''

def opg2():
    book_prices: dict[str,int] = dict()
    book_prices.update({"Basic Python": 150, "Cyber Security" : 500,"Network Security" : 399})

    print(f"{book_prices['Cyber Security'] = }")
    book_prices.get("Web Design")
    book_prices.update({"Basic Python": 200})
    book_prices["Karma Sutra"] = 150
    book_prices.pop("Cyber Security")
    print(f"{'Cyber Security' in book_prices = }")
    print(f"{'Network Security' in book_prices = }")

#opg2()

'''Exercise: set_me_up
• Write a program that does the following:
• Create two sets: set_a and set_b
• set_a should contain the numbers: {1, 2, 3, 4, 5}
• set_b should contain the numbers: {4, 5, 6, 7, 8}
• Print the union of set_a and set_b (all unique elements from both sets)
• Print the intersection of set_a and set_b (elements that exist in both sets)
• Print the difference of set_a and set_b (elements that are only in set_a)'''

def opg3():
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    print(f"Union: {set_a | set_b = }")
    print(f"Intersection: {set_a & set_b = }")
    print(f"Difference: {set_a - set_b = }")

#opg3()

'''Exercise: Mail_Sweep
Make a program Detect_anormaly and make 3 strings called mail_one, mail_two, mail_three
containing the strings from the red box below. Now add som code that:
• Create an empty set for Eavesdropped Mail Communication called emc
• Add the three strings and when doing this convert them to lists with default delimiter
• For each mail check if it contains the word ”bomb” you must print:
Suspecious mail found! The contents says: <print the mail as a string>'''

def opg4():
    mail_one, mail_two, mail_three, mail_four = "Hello, how are you? Regards, Alice", "Urgent: The package contains a bomb. Act now!", "Meeting reminder: Tomorrow at 10 AM", "Security alert: Do not open the bomb threat email."
    mails = (mail_one, mail_two, mail_three, mail_four)

    emc:set[str] = set()

    for mail in mails:
        if "bomb" in mail.lower():
            print(f"Suspecious mail found! The contents says: \"{mail}\"")
        emc.update(mail.split())

    print(emc)

#opg4()



