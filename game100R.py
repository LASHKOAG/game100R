#!/usr/bin/env python3

import random

#get argv from user
import sys

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

#for test
#numberFromUser = int(input("Input your number>")) #input number
f = open("database.txt", 'a') #open file
f.write(str(argumentFromUser)) #writing data in file
f.write("\n") #new line

#closing file
f.close()

#with open("/etc/default/grub", "w") as tw:
#        tw.write(content)

randomNumber = random.randint(0, 100)
print(f"random number from computer: {randomNumber}")


try:
    with open("./database.txt") as tmp_var:
        contentDataBase = tmp_var.read()
except FileNotFoundError:
    contentDataBase = '<<< NOT FOUND >>>'

#test logs
print(f"Data from file (contentDataBase): {contentDataBase}")