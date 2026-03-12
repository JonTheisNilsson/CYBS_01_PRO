'''Exercise: What happens inside the function stays inside the function… or?
• Make a py-program: my_def_scope
• Make a list: original_list = [1,2,3]
• Make a string: original_string = ”Private Scope”
• Make an integer: my_number = 7
• Now make a function that takes a list, a string and an integer as parameters
• Let the function add 4 to the list, change the string to ”for inside use only” and add 1 to the integer
• Let the function print alle the variables
• Now call the function
• Now end wit a print of all values
• What happened with the original values??'''

original_list = [1,2,3]
original_string = "Private Scope"
my_number = 7

def my_def(lst:list[int], string:str, integer:int):
    lst.append(4)
    string = "for inside use only"
    integer += 1

    print(f"{lst = }, {string = }, {integer = }")


print(f"{original_list = }, {original_string = }, {my_number = }")
my_def(original_list, original_string, my_number)
print(f"{original_list = }, {original_string = }, {my_number = }")

'''
'''

from ex7_module import input_number

def sum_it_up(_type:type):
    try:
        a = input_number(_type)
        b = input_number(_type)
        print(f"{a + b = }")
    except ValueError:
        print("you don't wanna play - bye!")

#sum_it_up(int)
sum_it_up(float)


'''Exercise: Okay let's look at that Car class…
Create a class named 'Car'
Create a program - that will use this class - called car_broker
• The Car class should have a constructor that take color, year, model, brand as parameters
• The Car class should have a method called print_info()
• From the broker program create car1 and car2 with som parameters
• Print the info
• Test if you can change year for car1?'''

class Car:
    def __init__(self, _color:str, _year:int, _model:str, _brand:str):
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
#print(dir(car1))




