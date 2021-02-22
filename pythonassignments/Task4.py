from functools import reduce
# 1. Write a program to reverse a string.
# Sample input: “1234abcd”
# Expected output: “dcba4321”

def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0]
s = "1234abcd"
print (reverse(s))

# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12

def stringcount(a):
    countlower = 0
    countupper = 0
    for i in a:
        if i.isupper():
            countupper+=1
        elif i.islower():
            countlower+=1
        else:
            pass
    print("No. of Uppercase characters : ",countupper)
    print("No. of Lower case Characters : ",countlower)
stringcount("abcSdefPghijQkl")

# 3. Create a function that takes a list and returns a new list with unique elements of the first list.

def uniquelist(a):
    b =[]
    for i in a:
        if i not in b:
            b.append(i)
    return(b)

print(uniquelist([1,2,3,5,6,4,2,3,4]))


# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.

n = input("enter the hyphened letters: ")
l = n.split("-")
l.sort()
print('-'.join(l))

# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT

lines = []
print("Enter sequence of lines:  ")
while True:
	line = input(">")
	if not line:
		break
	lines.append(line.upper())

print(lines)

# 6. Define a function that can receive two integral numbers in string form and compute their sum and
# print it in the console.

def suminputs(a,b):
    c = int(a)+int(b)
    return c

num1 = 10
num2 = 20

add = suminputs(num1,num2)
print("Summed up value: ",add)


# 7. Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line
# by line.

def max_length(s1,s2):
    if len(s1) == len(s2):
        print(s1)
        print(s2)
    elif len(s1) < len(s2):
        print(s2)
    else:
        print(s1)
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

max_length(s1,s2)

# 8. Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).

def printsquares():
    t = list()
    for i in range(1,21):
        t.append(i**2)
    print(tuple(t))

printsquares()
    

# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3) (where limit=3)
# Expected output:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

def shownumber(limit):
    for i in range(0, limit):
        if i == 0 or i%2==0:
            print(str(i)+" Even")
        else:
            print(str(i)+" Odd")
num = 6
shownumber(num)

# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)

evennumbers = list(filter(lambda x : x%2==0, range(1,21)))
print(evennumbers)



# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
# numbers in the filtered list. Use lambda() to define anonymous functions.

li =[1,2,3,4,5,6,7,8,9,10]
evennumbers = list(map(lambda x:x**2,filter(lambda x: x%2==0,li)))
print(evennumbers)

# 12. Write a function to compute 5/0 and use try/except to catch the exceptions

def divide():
    return 5/0
try:
    divide()
except ZeroDivisionError:
    print("it is division by 0")
except Exception:
    print("you have an exception")


# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().

li = [1,2,3,4,5,6,7]
joinedlist = reduce(lambda x,y: 10*x+y,li)
print(joinedlist)

