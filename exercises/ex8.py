'''Exercise: Warm up file handling
• Create two small txt.file in notepad: a.txt b.txt and fill some text lines in them…
• Now make a program that will create a new file c.txt and add a.txt and b txt to to
the file.
• Verify that it has the content of both files'''

def warm_up() -> str:
    res = ""

    with open("ex8_a.txt", 'r') as file:
        res += file.read()
    
    with open("ex8_b.txt", 'r') as file:
        res += file.read()
    
    with open("ex8_c.txt", 'w') as file:
        file.write(res)

    with open("ex8_c.txt", 'r') as file:
        assert res == file.read()

    return res

print(warm_up())

'''Exercise: myfile.txt
Make a program myfile.txt
• Print ”Hello - write texs to file <enter> for next line <Q> for quit
• Open file myfile.txt (append to file)
• Make an infinite whileloop
• If ”Q” then close file and call exit()
• Print input to file (remember /n'''

def myfile():
    with open("ex8_myfile.txt", 'a') as file:
        while (True):
            i = input("”Hello - write text to file <enter> for next line <Q> for quit: ")
            if i.upper() == 'Q':
                file.close()
                exit()
            file.write(i + "\n")

#myfile()