#!/usr/bin/python
'''

Write a program to create two list A & B such that List A contains Employee Id, List B contain Employee name (minimum 10 entries in each list) & perform following operation
a) Print all names on to screen
b) Read the index from the user and print the corresponding name from both list.
c) Print the names from 4th position to 9th position
 d) Print all names from 3rd position till end of the list
e) Repeat list elements by specified number of times (N- times, where N is entered by user)
f)Concatenate two lists and print the output.
g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )

'''
a = []
b = []

for x in range(10):
    a.append(float(input("Enter emp ID ")))
    b.append(raw_input("Enter emp name "))
#a
print '\n'.join(b) 
#b
indx = input("enter index ")
print "emp ID", a[indx], "emp name", b[indx]
#c
print '\n'.join(b[2:9])
#d
print '\n'.join(b[2:])
#e
indx = input("how many times to Repeat")
print '\n'.join(b*indx)
#f
print a+b
#g
for x in range(10):
    print a[x], " ", b[x]