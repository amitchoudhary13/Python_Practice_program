#!/usr/bin/python
'''
Create a list of 5 names and check given name exist in the List.
 a) Use membership operator (IN) to check the presence of an element.
 b) Perform above task without using membership operator.
 c) Print the elements of the list in reverse direction.

'''
name = ['hello','apple','yellow','new','black']
#a
if 'hello' in name:
    print 'presence in list'
#b
if name.__contains__('hello'):
   print 'presence in list'
#c
print name[::-1]