#!/usr/bin/env python3
import write_read_file as wrfile
import random
#get argv from user
import sys


filename = "./database.txt"


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
