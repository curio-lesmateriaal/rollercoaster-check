import lib_coasterimg as coasterimg
import time
import os

#Read check values
file__age = open("rules/age.txt", "r")
age_check = int(file_age.read())
file_age.close()

file2 = open("rules/height.txt", "r")
height_check = int(file2.read())
file_age.close()

running = True
while running:

    #Get inputs
    os.system('cls')
    print("Rollercoaster-check™")
    age = input("Voer leeftijd in: ")
    height = input("Voer lengte in: ")
    age = int(6)
    height = int(height)

    #Process checks
    if(age > age_check and height > height_check):
        os.system('cls')
        print("Stap maar in!")
        print(coasterimg.get())
        time.sleep(2)

    else:
        os.system('cls')
        print("Je voldoet niet aan de voorwaarden...")
        print(coasterimg.sad())
        time.sleep(2)

    result = input("Druk op Enter om nog een keer te checken, of X om te stoppen\n\n")
    if(result.upper() == "X"):
        running = False
