# 1. Create a list of given structure and get the Access list as provided below:
# x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# Access list: [1, 2, 3, 4]Access list: [600, 700]
# Access list: [100, 300, 500, 600, 800]
# Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
# Access list: [10]
# Access list: [ ]



# 2. Create a list of thousand numbers using range and xrange and see the difference between each
# other.
# (For reference:https://www.techbeamers.com/python-xrange-range/)

a = list(range(10))
print(a)
# x = xrange(1,1000) 
# print(type(x))

# The variable storing the range created by range() takes more memory as compared to variable storing the range using xrange(). 
# The basic reason for this is the return type of range() is list and xrange() is xrange() object.

# 3. How Tuple is beneficial as compared to the list?

# Operations on tuples can be executed faster compared to operations on lists
# A tuple is an immutable or unchangeable finite ordered sequence of elements
# Tuple being immutable requires less memory space as compared to list.


# 4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
# the number which is divisible by 3 and is a multiple of 2.

for i in range(1,100):
    if i%3==0 and i%2==0:
        print (i)

# 5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
# string with their index.

x = "consultadd" [::-1]
res = []
for i in x:
    if i in "aeiou":
        print(i)
for a in range(len(x)):
    if x[a] in "aeiou":
        res.append(a)
print("Index positions: "+ str(res))



# 6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
# string which is having an even length.

def printeven(a):
    a = a.split(" ")
    for i in a:
        if len(i)%2==0:
            print(i)

a = "hello my name is abcde"
printeven(a)
    
# 7. Write a program in python to print the pair of numbers whose sum is equal to the result
# number that is let's say 8.
# x=[1,2,3,4,5,6,7,8,9,-1]

def pairprint(ls,x,sum):
    for i in range(0,x):
        for j in range(i+1,x):
            if(ls[i] + ls[j] == sum):
                print("(",ls[i],",",ls[j],")",sep="")

ls = [1,2,3,4,5,6,7,8,9,-1]
x = len(ls)
sum = 8
pairprint(ls,x,sum)


# 8. Write a program in Python to complete the following task:
# Create two lists such as even_list and odd_list
# Ask user to enter a number in the range of 1,50 and make sure if the entered number is
# even, append it to the even_list and if the entered number is odd append it to the odd_list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you enter all the 5 elements, calculate the sum of the list and return the
# maximum of the list.

# ls = int(input("Enter a number from 1 to 50: "))

# even_list = []
# odd_list = []

# for i in range(1,50):
#     if i%2==0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# print(even_list)
# print(odd_list)

def splitevenodd(A): 
   evenlist = [] 
   oddlist = [] 
   for i in A: 
      if (i % 2 == 0): 
         evenlist.append(i)
         
      else: 
         oddlist.append(i)
   print("Even lists:", evenlist) 
   print("Odd lists:", oddlist) 

A=list()
print("Enter a number from 1 to 50: ")
for i in range(5):
   k=int(input(""))
   A.append(k)
splitevenodd(A)

# 9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
# Sample input: 12abcbacbaba344ab
# Expected output: a=5 b=5 c=2
# NOTE: Make sure to avoid counting the occurrence of numeric values in the string.

inp_str = "12abcbacbaba344ab"
outpt = {x : inp_str.count(x) for x in set(inp_str)}
print ("Occurrence of all characters in GeeksforGeeks is :\n "+ str(outpt))  


# 10. Generate and print another tuple whose values are even numbers in the given tuple
# (1,2,3,4,5,6,7,8,9,10).

tp = (1,2,3,4,5,6,7,8,9,10)
li = list()
for i in tp:
    if i%2==0:
        li.append(i)
tp2 = tuple(li)
print(tp2)
