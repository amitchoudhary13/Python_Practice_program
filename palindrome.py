'''
Write a program to check given string is Palindrome or not. (Use function Concepts and Required keyword, Default parameter concepts) i.e Reverse the given string and check whether it is same as original string, if so then it is palindrome. Example: String "malayalam" when reversed will be "malayalam" hence palindrome.

'''

def palindrome(input1):
    if input1 == input1[::-1]:
        print(input1,'is a Palindrome')
    else:
        print(input1,'is not a palindrome')

input1 = raw_input("Enter a Word to check if its a Palindrome : ")