import os
import time

def enter():
    os.chdir("C:\\Users\\aydip\\Player Manager")
    enter_choice = input("Login (l) or Register (r)? >>> ")

    if enter_choice == 'r':
        print("Computer: What is your name?\n")
        nom = input(">>> ")
        fichier = open(f"{nom}.txt",'w')
        fichier.write(f"Name: {nom}")
        fichier.close()

    if enter_choice == 'l':
        print("Computer: What is your name?\n")
        nom = input(">>> ")
        search_name = nom.strip("\"").strip()
        try: 
            file = open(f"{search_name}.txt", 'r')
            print(file.read())
        except:
            print("\nAccount not found.\n")
            enter()
    
    elif enter_choice != 'r' and enter_choice != 'l':
        enter()
        

enter()
time.sleep(5)
os.system('cls')
