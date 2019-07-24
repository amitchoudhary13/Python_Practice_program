#!/usr/bin/python

numbers = []
num = 4
for x in range(num):
    numbers.append(float(input()))




if numbers[0] > numbers[1] and numbers[0] > numbers[2] and numbers[0] > numbers[3]:
    print "Biggest of three numberss is", numbers [0]
    
if numbers[1] > numbers[0] and numbers[1] > numbers[2] and numbers[1] > numbers[3]:
    print "Biggest of three numberss is", numbers [1]
    
if numbers[2] > numbers [0] and numbers[2] > numbers[1] and numbers[2] > numbers[3]:
    print "Biggest of three numberss is", numbers [2]
    
if numbers[3] > numbers[0] and numbers[3] > numbers[1] and numbers[3] > numbers[2]:
    print "Biggest of three numberss is", numbers [3]
 
numbers.append(float(input()))

if numbers[4] > numbers[0] and numbers[4] > numbers[1] and numbers[4] > numbers[2]  and numbers[4] > numbers[3]:
    print "Biggest of three numberss is", numbers[4]