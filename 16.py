#!/usr/bin/python
'''
Write program to perform following:
 i) Check whether given number is prime or not.
 ii) Generate all the prime numbers between 1 to N where N is given number.

'''
a = 7
b = True
for i in range(2, a-1):
    if a % i == 0 :
        b = False
    
if b == False:
    print "The given number ", a, "is not prime"
else:
    print "The given number ", a, "is prime"

a = input("enter a number")
for num in range(2,a):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print num