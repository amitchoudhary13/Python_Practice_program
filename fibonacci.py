'''
Write a program to generate a Fibonacci series using a function called fib(n), 
a) Where ‘n’ is user specified argument specifies number of elements in the series.

'''

def fib(n):
    a = 0
    b = 1
    c = a
    counter = 1
    while counter <= n :
        print(c)
        counter = counter + 1
        a = b
        b = c
        c = a + b

input1 = input("Enter number of Fibonacci series you want : ")
fib(input1)