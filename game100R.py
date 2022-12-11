#!/usr/bin/env python3

import random

#get argv from user
import os
import sys

filename = "./database.txt"

#function for write data in file
def writeDataInFile(_filename, data):
    if os.path.exists(_filename):
        f = open(_filename, 'a')
        f.write(str(data))
        f.write("\n")

        #closing file
        f.close()
    else:
        print("WARNING:file not exists")


#funcion for read file
def readDataFromFile(_filename):
    try:
        with open(_filename) as tmp_var:
            contentDataBase = tmp_var.read()
    except FileNotFoundError:
        contentDataBase = '<<< NOT FOUND >>>'
    return contentDataBase


# название файла
print(sys.argv)

print ("len(sys.argv) = %d" % len(sys.argv))

for i in range(len(sys.argv)):
    if i == 0:
        print ("Program name: %s" % sys.argv[0])
    else:
        print("%d. argument: %s" % (i, sys.argv[i]))


if len(sys.argv) == 1:
    print("WROND INPUT DATA. Try next with argument")
    exit()


argumentFromUser = sys.argv[1]
print(f"argumentFromUser: {argumentFromUser}")
print("type of  varriable argumentFromUser: " + str(type(argumentFromUser)))
#--------------------------------------------------------------

# #for test
# #numberFromUser = int(input("Input your number>")) #input number


writeDataInFile(filename, argumentFromUser)

databaseContent = readDataFromFile(filename)


#with open("/etc/default/grub", "w") as tw:
#        tw.write(content)

randomNumber = random.randint(0, 100)
print(f"random number from computer: {randomNumber}")




#test logs
print(f"Data from file (contentDataBase): {databaseContent}")