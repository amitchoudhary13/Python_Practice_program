#!/usr/bin/python
'''
Write program to find the biggest and Smallest of N numbers.
 PS: Use the functions to find biggest and smallest numbers. 

'''

number = []

num = input("who many number ")

for x in range(num):
    number.append(input())

print "smallest ",min(number)
print "biggest ",max(number)