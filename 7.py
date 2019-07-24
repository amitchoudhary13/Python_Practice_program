#!usr/bin/python
''' 
Basic LIST Operations
Create a list with at least 10 elements having integer values in it
Print all elements
Perform slicing operations
Perform repetition with * operator
Perform concatenation with other list.
'''

list1 = [12, 23, 22, 55, 62, 54, 61, 12, 84, 45] #list 

for x in range(len(list1)): #for loop for printing all elements
    print list1[x]

#slicing list
print "Sub string is", list1[2:5]
#Repeated string
print "Repeated string is ", list1 * 5
#concatenated string
list2 = [101, 4232]
print "Concatenated string is ", list1 + list2