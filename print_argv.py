#!/usr/bin/python

#libary 
from sys import argv 

#question
'''Write a program to receive 5 command line arguments and print each argument separately.
Example: >> python test.py arg1 arg2 arg3 arg4 arg5
a) From the above statement your program should receive arguments and print them each of them. 
'''
#for loop which print each argument separately
for x in range(len(argv[1:])):
    print argv[x+1]
