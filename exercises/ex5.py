'''Make a program where you enter you name and you age.
• Use if elif else to decide what user may drive. (under 16: bicycle, 16-18: small
motorbike, over 18: all vehicles are possible)'''

def opg1(name: str, age: int) -> str:
    res = name + " may drive "
    if age < 16:
        res += "bicycle"
    elif age <= 18:
        res += "small motorbike"
    else:
        res += "all vehicles are possible" 
    return res

#print(opg1("Anon",18))


def opg1alt(name: str, age: int) -> str:
    res = name + " may drive "
    match age:
        case _ if age < 16:
            res += "bicycle"
        case _ if age <= 18:
            res += "small motorbike"
        case _:
            res += "all vehicles are possible" 
    return res

#print(opg1alt("Anon",18))


'''Exercise: Match and while - ”bruteforce”
• Create a program: bruteforce.py
• Make a dictionary with user_id as key and value is a list with pw and role as elements (role can be one of these: admin, usr, guest)
• let the dictionary start with two users ”Alice”, pw=”Alice123”, role=”admin”, and user_id ”Bob”: pw=”Bob123” and role = ”usr”
• Now contruct some code that will run infinitly with a menu:
1. Add user (add a user to your dict)
2. Delete user (remove a user from your dict)
3. Show admins (seach list for users with admin privillige and print their usernames)
4. Guess password for user (type a username and guess the pw (password) - press ”Q” for exit)
5. Exit (exit the program)
• Use Match case for handling menu choices, use while loop for guessing'''

roles = ["admin", "usr", "guest"]

users:dict[str, list[str]] = dict()
users["Alice"] = ["Alice123", "admin"]
users["Bob"] = ["Bob123", "usr"]

menu_options = "Type 1 to add user. \nType 2 to delete user.\nType 3 to show admins.\nType 4 to guess pw.\nType q to quit."

def opg2():
    while (True):
        print(menu_options)
        match input("Option: ").lower():
            case '1':
                add_user()
            case '2':
                delete_user()
            case '3':
                show_admins()
            case '4':
                guess_pw()
            case 'q':
                exit()
            case _:
                print("Invalid input")

def add_user():
    print("Creating new user:")
    while (True):
        name = input("Input username: ")
        if name in users:
            print("Username already in use. ")
            continue
        break
    pw = input("Input pw: ")
    while (True):
        role = input("Input role: ")
        if role not in roles:
            print("Role must be: admin, usr or guest")
            continue
        break
    users[name]=[pw, role]
    print(f"User: {name} created.\n")

def delete_user():
    while (True):
        name = input("Input username to delete (q to cancel): ")
        if (name == 'q'): return
        if name not in users:
            print("User doesn't exist. ")
            continue
        break
    
    tries = 3
    while(tries > 0):
        pw = input("Input pw:")
        if pw == users[name][0]:
            users.pop(name)
            print(f"User {name} has been deleted.")
            break
        else:
            tries -= 1
            print(f"wrong password. {tries} tries left.")
    if(tries==0):
        print("Too many tries. Account locked")

def show_admins():
    print("Admins:")
    for k, v in users.items():
        if v[1]=="admin":
            print(k)
    print()

def guess_pw():
    while (True):
        user = input("Input user to guess: ")
        if user not in users:
            print(f"User {user} does not exist.")
            continue
        break
    v = users[user]
    pw = v[0]
    while (True):
        guess = input("Guess password (q to quit): ")
        if guess == pw:
            print("You guessed it")
            break
        elif guess == 'q':
            break
        else:
            print("try again.")

#opg2()

'''Exercise: Loop around
Make a simple loop going from 0 to 50 using the range function
• The loop should print the numbers on the way but…
• When i comes to 10 we want to skip this number and print ”we don't print '10'”
• When i comes to 45 we want to stop the loop'''

def opg3():
    for i in range(51):
        if i == 10:
            print("we don't print '10'")
        elif i == 45:
            break
        else:
            print(i)

#opg3()