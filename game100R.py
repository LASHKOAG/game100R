#!/usr/bin/env python3


numberFromUser = int(input("Input your number>")) #input number
f = open("database.txt", "w") #open file
f.write(str(numberFromUser)) #writing data in file

#closing file
f.close()

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
		
#--------------------------------------------------------------
