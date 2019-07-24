#Write a program to handle the following exceptions in you program.
#a) KeyboardInterrupt
#b) NameError
#c) ArithmeticError Note: Make use of try, except, else: block statements.


import time

i = 1
try:
    while (i < 5):
        time.sleep(1)
        print
        i
        i += 1
except KeyboardInterrupt:
    print("KeyboardInterrupt")

try:
    name = input("Enter your name:")
    print("Good Morning " + name)
except NameError:  # Enter your name in Quotes else NameError msg will appear
    print("NameError")

try:
    num = 0 / 0
except ArithmeticError:
    print("ArithmeticError")
