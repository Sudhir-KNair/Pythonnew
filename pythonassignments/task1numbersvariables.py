# 1. Create three variables in a single line and assign values to them in such a manner that each one of
# them belongs to a different data type.

# ----Solution:

x,y,z = 1,"name",3.2
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))

# 2. Create a variable of type complex and swap it with another variable of type integer.

a=3+9j
b=5
print(type(a))
c=a
a=b
b=c
print("value fter swapping :", a)

# 3.Swap two numbers using a third variable and do t
# he same task without using any third variable.

# Swapping values with Temp Variables
a = 10
b = 20
c = a
a = b
b = c
print("value of a after swapping :", a)
print("value of b after swapping :", b)

# Swapping values without temp Variables
x = 5
y = 10
x,y = y,x
print("value of x without variable :", x)
print("value of y without variable :", y)

# 4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
# Version.

x = input("Enter 2 digit number for x: ")
y = input("Enter 2 digit number for y: ")
print("value of x,y :",x,",",y)

# # Python 2

# txt = raw_input("Type something to test this out: ")
# print "You typed :", txt

# 5. Write a program to complete the task given below:
# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
# another variable called z. Add 30 to z and store the output in variable result and print result as the
# final output.

a = int(input("Enter any number from 1-10: "))
b = int(input("Enter any number from 1-10: "))
z= 30+(a+b)
print('Value of z : ',z)

# 6. Write a program to check the data type of the entered values.
# HINT: Printed output should say - The data type of the input value is : int/float/string/etc

x = 10 
b = 'name'
c = 10.2
print('The data type of the input value is : ',type(x))
print('The data type of the input value is : ',type(b))
print('The data type of the input value is : ',type(c))

# 7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
# UPPERCASE.

#UpperCamelcase
UserAccountName = 'Sudhir'

#Lowercamelcase
userAccountId = 1234

#Snakecase
user_email = "sudhir@gmail.com"

#Uppercase
MYVAR = "John"

# 8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
# again. Will it change the value? If Yes then Why?

a = 10
a = "astring"
print(a)

# Yes, it will print the latest value assigned to the variable
