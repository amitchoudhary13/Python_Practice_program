#Create a Calculator with the following functions.
#a) Addition/subtraction/multiplication and division of two numbers ( Note: Create separate function for each operation )
#b) Find square root of a given number.( Use keyword arguments in your function)
#c) Create a list of sub strings from a given string

def Addition(a,b):
    sums=a+b
    print("sum is",sums)

def Subtraction(a,b):
    sub=a-b
    print("Subtraction is",sub)

def Multiply(a,b):
    mul=a*b
    print("multiplication is",mul)

def Division(a,b):
    div=a/b
    print("Division is",div)

def Sqrt(num):
    print("SQrt is ",num**0.5)

Addition(3,5)
Subtraction(9,3)
Multiply(3,5)
Division(4,2)
Sqrt(9)
Sqrt(num=81)

'''
sum is 8
Subtraction is 6
multiplication is 15
Division is 2.0
SQrt is  3.0
SQrt is  9.0
'''

def subStrCrest(strg,delimiter):
    return s.split(delimiter)

strg = input("Enter your string: ")
delimiter = input("Enter the delimiter on which you want to creat substings: ")
print(subStrCrest(strg,delimiter))

'''
Enter your string: Pack: My: Box: With: Good: Food
Enter the delimiter on which you want to creat substings: :
['Pack', ' My', ' Box', ' With', ' Good', ' Food']
'''
