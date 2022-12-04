#!/usr/bin/env python3


numberFromUser = int(input("Input your number>")) #input number
f = open("database.txt", "w") #open file
f.write(str(numberFromUser)) #writing data in file

#closing file
f.close()
