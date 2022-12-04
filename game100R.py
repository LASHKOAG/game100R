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
f = open("database.txt", "w") #open file
f.write(str(argumentFromUser)) #writing data in file

#closing file
f.close()


