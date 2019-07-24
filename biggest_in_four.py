'''
Write a function to find the biggest of 4 numbers.
a) All numbers are passed as arguments separately (Required argument)
b) use default values for arguments (Default arguments)

'''
def biggest(lst=[1,2,3,4]):
    for l in lst:
        big = 0
        if l > big:
            big = l
    print('biggest in four',big)

input1 = list(map(int,input().split()))
biggest(input1)