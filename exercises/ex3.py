'''Make a program where you declare a list as such:
my_list = [0,1,2,3,4,5,6,7,8]
Now add some code that does the following:
• Print the full list
• Print the first element of the list
• Print the last element of the list
• Print the first 4 elements
• Declare a list called “second_list” and fill it with the last 3 elements of “my_list”'''

def opg1():
    my_list = [0,1,2,3,4,5,6,7,8]
    print(my_list)
    print(my_list[0])
    print(my_list[-1])
    print(my_list[0:3])
    second_list = my_list[-3::]
    print(second_list)

opg1()

'''Make a Program – Work_With_Lists and declare an empty list: my_list = []
Add som code that comply with these steps:
• Add the numbers 2, 1 and 3 to the list
• Add the string ”cyber” to the list
• Print the index of ”cyber”
• Remove the string from the list
• Put the list in ascending order and print it'''

def opg2():
    my_list :list[int|str]= []
    my_list.extend([2,1,3])
    my_list.append("cyber")

    index = my_list.index("cyber")
    print(index)

    my_list.pop(index)
    my_list.sort()
    print(my_list)

#opg2()

'''After processing an access log with a tool, you have generated the list below of IP
addresses that has accessed the system. This list is chronologically sorted. Write a
script that does the following:
• You received an e-mail telling you that the IP '8.8.8.8' is the latest to access the
system. You need to add this manually.
• How many entries are in the log?
• What are the latest 5 IPs that accessed the system?
• How many times did '3.100.186.196' access the system?'''

def opg3():
    ips = ['189.19.202.26', '124.124.86.154', '111.123.147.92', '191.194.49.89','191.194.49.89', '3.100.186.196',
    '17.102.131.131', '170.40.162.9','66.23.103.242', '203.207.124.71', '3.100.186.196',
    '170.194.124.70','3.100.186.196', '161.240.120.16', '37.161.17.14', '3.100.186.196','144.182.46.41',
    '3.100.186.196', '67.180.5.237', '182.44.178.202']

    ips.append('8.8.8.8')

    print(len(ips))
    print(ips[-5::])
    print(ips.count('3.100.186.196'))

#opg3()

'''Exercise: Split it up
Make a program: ‘Split_Up’ and declare a variable called "full_name" and enter
the value: “John Jacob Jingleheimer Schmidt”. Add code that can do the following:
• Make a list from the string, where each element is a part of the name. Element 0
should be the first name, element 1 middle name etc. Give the list an
appropriate name
• Print out the list
• Prove that your new list is actually a list type
• Make another new list from your "full_name" string, this time splitting on the
“n” character. Print the new list and take a note of what happens
• Finally, put your list back together into a new string. Name this
string "full_name_restored'''

def opg4():
    full_name ="John Jacob Jingleheimer Schmidt"

    name_list = full_name.split()
    print(name_list)
    print(type(name_list))

    list_n = full_name.split('n')
    print(list_n)

    full_name_restored = "n".join(list_n)
    print(full_name_restored)

#opg4()

'''Make a program - Trouble and Declare a tuple nemed house_pets with these values:
house_pets = (“Canarie”,”Turtle”,“Dog”)
You realise that the “Cat” and the “Ferret” are missing in the tuple.
It's up to you to make a program that adds these values to the tuple, despite the fact that tuples don't have an
“append” method. You have to add the value without hardcoding a new tuple, so you end up with a tuple that
looks like this: (“Canarie”,”Turtle”,“Dog”,”Cat”,”Ferret”)'''

def opg5():
    house_pets = ("Canarie","Turtle","Dog")
    print(house_pets)

    temp_list = list(house_pets)
    temp_list.extend(["Cat", "Ferret"])
    print(temp_list)

    house_pets = tuple(temp_list)
    print(house_pets)

#opg5()