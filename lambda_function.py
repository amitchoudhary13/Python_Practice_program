'''
Write a program with lambda function to perform following.
a) Perform all the operations of basic calculator (Add, Sub, Multiply, Divide, Modulus, Floor division)

'''

number1 = input("enter number :")
number2 = input("enter number :")

sums = lambda number1, number2 : number1 + number2
product = lambda number1, number2 : number1 * number2
diffrence = lambda number1, number2 : number1 - number2
division = lambda number1, number2 : number1 / number2

print(number1,'+',number2,'=',sums(number1,number2))
print(number1,'*',number2,'=',product(number1,number2))
print(number1,'-',number2,'=',diffrence(number1,number2))
print(number1,'/',number2,'=',division(number1,number2))