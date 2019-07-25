#!/usr/bin/python
from sys import argv
'''5 b) Find the biggest of three numbers, where three numbers are passed as command line arguments.'''
#variable declaration
num1 = int(argv[1])
num2 = int(argv[2])
num3 = int(argv[3])
#if Implementation
if num1 > num2  and num1 > num3 :
    print "Biggest of three numbers is", num1
if num2  > num1 and num2 > num3 :
    print "Biggest of three numbers is", num2 
if num3  > num1 and num3  > num2 :
    print "Biggest of three numbers is", num3 
