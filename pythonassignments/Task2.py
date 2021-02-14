# 1. Write a program in Python to perform the following operation:
#     If a number is divisible by 3 it should print “Consultadd” as a string
#     If a number is divisible by 5 it should print “Python Training” as a string
#     If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
#     string.

x= int(input("please provide your number: "))
if x%3==0 and x%5==0:
    print("Consultadd-Python Training")
elif x%3==0:
    print("Consultadd")
elif x%5==0:
    print("Python Training")
else:
    print("Not Divisible")
     
# 2. Ask user to choose the following option first:

# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If User Enter 4 - Multiplication
# If User Enter 5 - Average

# Ask user to enter two numbers and keep those numbers in variables num1 and num2
# respectively for the first 4 options mentioned above.

# Ask the user to enter two more numbers as first and second for calculating the average as
# soon as the user chooses an option 5.


userinput=int(input("Enter a number between 1-5: "))
num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))

if userinput==1:
    sum = num1+num2
    if sum < 0:
        print("negative")
    else:
        print(sum)
elif userinput==2:
    subtraction = num1-num2
    if subtraction < 0:
        print("negative")
    else:
        print(subtraction)
elif userinput==3:
    division = num1/num2
    if division < 0:
        print("negative")
    else:
        print(division)
elif userinput==4:
    multiplication = num1*num2
    if multiplication < 0:
        print("negative")
    else:
        print(multiplication)
elif userinput==5:
    Firstnumber = int(input("Firstnumber: "))
    Secondnumber = int(input("Secondnumber: "))
    Average = num1+num2+Firstnumber+Secondnumber/4
    print(Average)

# 3.Write a program in Python to implement the given flowchart:

a=10
b=20
c=30
avg = int((a+b+c)/3)
print("Avg = ", avg)
if avg>a and avg>b and avg>c:
    print("Avg is higher than a,b,c")
elif avg>a and avg>b:
    print("Avg is higher than a,b")
elif avg>a and avg>c:
    print("Avg is higher than a,c")
elif avg>b and avg>c:
    print("Avg is higher than b,c")
elif avg>a:
    print("Avg is just higher than a")
elif avg>b:
    print("Avg is just higher than b")
else:
    print("Avg is just higher than c")

# 4. Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”
while True:
    num = int(input("Enter a number: "))
    if num<0:
        print("Negative number")
        break
    if num>0:
        print("Good Going")
        continue

# 5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200.

for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        print(i)
    
# 6. What is the output of the following code examples?
# x=123
# for i in x:
#     print(i)

# # The problem with this line for i in x: is that we are trying to iterate over a number.Objects of type int are not iterable.

# i = 0
# while i < 5:
#     print(i)
#     i+=1
#     if i == 3:
#         break
#     else:
#         print("error")

# # Until the number reaches 3 it will keep on printing the number along with error message

# count = 0
# while True:
#     print(count)
#     count+=1
#     if count>=5:
#         break

# Basically the count will interate and keeps on adding a number to it until it reaches 5 or more than 5 then it breaks

# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
# Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement
    
for i in range(0,6):
    i+1
    if i==3 or i==6:
        continue
    print(i)

# 8. Write a program that accepts a string as an input from the user and calculate the number of digits
# and letters.
# Sample input: consul72
# Expected output: Letters 6 Digits 2

ui = str(input("Please enter here: "))
d=0
l=0
for i in ui:
    if i.isalpha():
        d=d+1
    elif i.isdigit():
        l=l+1
    else:
        pass
print("Letters:",d, "Digits :",l)

# 9. Read the two parts of the question below:
# Write a program such that it asks users to “guess the lucky number”. If the correct number is
# guessed the program stops, otherwise it continues forever.

x=int(input("Guess the Lucky number: "))
if x==6:
    print("you are winner")
else:
    print("not lucky")

# Modify the program so that it asks users whether they want to guess again each time. Use two
# variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
# to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
# The program continues as long as a user has not answered “no” and has not guessed the correct
# number)

number = -1
answer = "yes"

while number !=5 and answer != "no":
    number = int(input("Guess the Lucky number: "))
    if number !=5:
        print("You are not lucky")
        answer = str(input("Would you like to guess again?:yes/no "))

    
# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
# such as

# counter = 1
# While counter <= 5:
# print(“Type in the”, counter, “number”
# counter=counter+1

# The program asks for five guesses (no matter whether the correct number was guessed or not). If the
# correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”.

counter = 1
while counter <=5:
    number = int(input("Guess the "+ str(counter) +". number: "))
    if number !=10:
        print("Try again")
    else:
        print("Good guess")
    counter = counter +1
else:
    print("Game over")

# 11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
# the while loop so that users do not have to continue guessing after they found the number. If the user
# does not guess the number at all, print “Sorry but that was not very successful”.

counter = 1
while counter <=5:
    number = int(input("Guess the "+ str(counter) +". number: "))
    if number != 10:
        print("Try again")
    else:
        print("Good guess")
        break
    counter = counter +1
else:
    print("Sorry but that was not very successful")
