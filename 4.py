#!usr/bin/python
'''Write a program to find the number is Prime or not.'''

#variable declaration
a = 7
b = True
for i in range(2, a-1): # for loop to check numberis not prime
    if a % i == 0 :
        b = False  
if b == False: #if-else Implementation for prime 
    print "The given number ", a, "is not prime"
else:
    print "The given number ", a, "is prime"
