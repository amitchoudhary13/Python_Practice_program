#!/usr/bin/python
from sys import argv
#variable declaration 
a = complex(int(argv[1]), int(argv[2]))
b = complex(int(argv[3]), int(argv[4]))
#Implementation
c = a + b
print "\n Addition of two numbers is", c
c = a - b
print "\n Subtraction of two numbers is", c
c = a * b 
print "\n Multiplication of two numbers is", c
c = a / b 
print "\n Division of two numbers is", c