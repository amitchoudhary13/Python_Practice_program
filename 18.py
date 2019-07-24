#!/usr/bin/python
'''
Using loop structures print numbers from 1 to 100. and using the same loop print numbers from 100 to 1 (reverse printing)
a) By using For loop 
b) By using while loop
c) Let mystring ="Hello world"
print each character of mystring in to separate line using appropriate loop structure.
'''

list1=[]
for i in range(1,101):
    print i
    list1.append(i)
list1.reverse()
print "\nNumbers 1 to 100 in reverse order using the same for loop",list1

list2=[]
i=1
print "\nPrinting 1 to 100 using while loop"
while i<=100:
    print i
    list2.append(i)
    i+=1
list2.reverse()
print"\nNumbers 1 to 100 in reverse order using the same while loop",list2

mystring='Hello world'
print '\nPrinting each character of string Hello world in separate line'
for each in mystring:
    print each
