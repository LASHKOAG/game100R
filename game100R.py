#!/usr/bin/env python3
import write_read_file as wrfile
import random
#get argv from user
import sys


filename = "./database.txt"

def check_valid_input_data():
    if len(sys.argv) == 1:
        print("WROND INPUT DATA. Try next with argument")
        exit()


check_valid_input_data()

argumentFromUser = sys.argv[1]
print(f"argumentFromUser: {argumentFromUser}")
print("type of  varriable argumentFromUser: " + str(type(argumentFromUser)))
#--------------------------------------------------------------


databaseContent = wrfile.readDataFromFile(filename)
listdata = []
listdata = databaseContent.split("\n")

listdataclear = []

for i in range(0, len(listdata)-1):
    tmp_list = listdata[i].split("\n")
    listdataclear.append(tmp_list[0])


for i in range(len(listdataclear)):
    if argumentFromUser == listdataclear[i]:
        print("Game over, number exists yet, make new attempt")
        exit()

randomNumber = random.randint(0, 100)
print(f"random number from computer: {randomNumber}")

if argumentFromUser == randomNumber:
    print("You win! Get your 100r!")
else:
    print("Try again...")
    wrfile.writeDataInFile(filename, argumentFromUser)
"""

#for test
#numberFromUser = int(input("Input your number>")) #input number
wrfile.writeDataInFile(filename, argumentFromUser)

databaseContent = wrfile.readDataFromFile(filename)


#with open("/etc/default/grub", "w") as tw:
#        tw.write(content)

randomNumber = random.randint(0, 100)
print(f"random number from computer: {randomNumber}")




#test logs
print(f"Data from file (contentDataBase): {databaseContent}")


# filename = "./111.txt"
# wrfile.deleteFile(filename)

#test commit
print("test commit")
"""