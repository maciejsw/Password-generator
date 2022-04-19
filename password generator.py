import random
import pyperclip
print("Welcome, I'm your password generator!")

length = int(input("Please, give me the desired length of the password: "))

characters = []
characters.extend(["abcdefghijklmnopqrstuvwxyz", "01234567890", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "!@#$%^&*()?"])

password = ""

choosen_text = []
last_text = "5. Reset\n6. Generate!\nYour password is: {}\n7. Copy to the clipboard\n0. Exit"
choosen_text.extend(["Choose the number to include or exclude given characters in your password:\n1. Small letters",
"2. Numbers", "3. Capital letters", "4. Special signs", last_text])
added_text = " ADDED"

choosen = ""

terminate = 0
is_choosen = []

for i in range(4):
    is_choosen.append(0)

while terminate != 1:
    print("\033[H\033[2J", end = "")
    display = ""
    
    choosen_text[4] = last_text.format(password)
    for i in choosen_text:
        display = display + "\n" + i
    custom = int(input(display))

    match custom:
        case 1 | 2 | 3 | 4:
            if is_choosen[custom-1] == 0:
                choosen = choosen + characters[custom-1]
                choosen_text[custom-1] = (choosen_text[custom-1] + added_text)
                is_choosen[custom-1] = 1
            else:
                choosen = choosen.replace(characters[custom-1], "")
                choosen_text[custom-1] = (choosen_text[custom-1].replace(added_text, ""))
                is_choosen[custom-1] = 0
            
        case 5:
            for i in range(4):
                choosen = choosen.replace(characters[i], "")
                choosen_text[i] = choosen_text[i].replace(added_text, "")
                is_choosen[i] = 0
            password = ""
        case 6:
            if len(choosen)>0:
                password = ""
                password = ''.join((random.choice(choosen)) for i in range(length))
        case 7:
            pyperclip.copy(password)
        case 0:
            terminate = 1 
        case _:
            print("")







