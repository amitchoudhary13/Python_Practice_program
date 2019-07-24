#!usr/bin/python
'''
Basic String operations

Write a program to read string and print each character separately.
    a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.
    b) Repeat the string 100 times using repeat operator *
    c) Read string 2 and concatenate with other string using + operator.
'''
#user input
str1 = raw_input()
str2 = raw_input()
#for loop to read string and print each character separately
for i in str1:
    print "current letter is", i
#a
str3 = str1[2:5]
print "Sub string is", str3
#b
print "Repeated string is ", str1 * 100
#c
print "Concatenated string is ", str1 + str2