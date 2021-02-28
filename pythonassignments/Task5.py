# 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
# HINT: Use SyntaxError

# try:
#     eval('x === x')
# except SyntaxError:
#     print("we cannot do that")

# # Normally, the interpreter parses the entire file before executing any of it, so it detects the syntax error before the try statement is executed.
# # We can  catch SyntaxError if it's thrown out of an eval or import operation.

# 2. Write a program in Python to allow the user to open a file by using the argv module. If the
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure
# to use read only mode.

# import sys

# with open(sys.argv['Task2.py'],'r') as file_my:
#     print(file_my.read())

# 3. Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits”

# while True:
#     n = input("Enter your four digit number: ")
#     if len(n)==4:
#         try:
#             print("Success")
#         except ValueError:
#             print("No success")


def fourdigit_code():
    num = ""
    while True:
        num = input("Enter 4 digit code: ")
        if len(num) == 4:
            try:
                return int(num)
            except ValueError:
                print("Error, you must enter a number")
        else:
            print("The length is too short/long !!! Please provide only four digits")
fourdigit_code()

# 4. Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
# should not be more than 3 times.