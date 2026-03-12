'''
Description: Write a program that:
• Asks the user for their name (string)
• Asks the user for their age (int)
• Asks the user for their height in meters (float)
• Calculates user's birth year (assume the current year is 2026)
• Print “hi <name> you where born in <birth year>”
• Print “You are <height> meters and <age> years old”
• Test also the program when user enters an incorrect data type!
'''

name = input("Name: ")

def validate_input(cand:str, _type:type) -> tuple[bool,int]:
    try:
        casted = _type(cand)
    except ValueError:
        print(f"must be input value type {_type}")
        return False, -1
    return True, casted

is_valid = False
while(not is_valid):
    is_valid, age = validate_input(input("Age: "), int)

height, age = -1, -1
is_valid = False
while(not is_valid):
    is_valid, height = validate_input(input("Height in meter: "), float)

print(f"hi {name} you where born around {2026-age}.")
print(f"You are {height} meters and {age} years old.")
