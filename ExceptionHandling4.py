import sys


try:
    num=a/2
except Exception:
    print("Exception")



#Arithmetic error
try:
    div=2/0
except ArithmeticError:
    print("Arithmetic error exception")



#Systemexit
try:
    sys.exit()
except SystemExit:
    print("system exit exception")


#Zero division error
try:
    a=2/0
except ZeroDivisionError:
    print("Zero Division exception")


#import error
try:
    import dummy
except ImportError:
    print("Import error exception")
