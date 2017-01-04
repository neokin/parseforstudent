import sys
import os
inputfile = open("mcha6sem_2.txt")
lines = inputfile.readlines()
print(lines)
for line in lines:
	os.mkdir(line)

