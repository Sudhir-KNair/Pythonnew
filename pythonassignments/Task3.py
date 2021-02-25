# 1. Create a list of 10 elements of four different data types like int, string, complex and float.

a=[4,"abc",3.4,3.5j,6,"bcd",10,6.7]


# 2. Create a list of size 5 and execute the slicing structure
l = [5, 10, 20, 30, 40]
print(l)
print(l[2:4])

# 3. Write a program to get the sum and multiply of all the items in a given list.

def multiplylist(multlist):
    result = 1
    for x in multlist:
        result = result * x
    return result

list1 = [2,3,4]
print(multiplylist(list1))

# def sumlist(slist):
#     result = 0
#     for x in slist:
#         result = result + x
#     return result

# list2 = [2,3,4]
# print(sumlist(list2))

list2 = [2,3,4]
print(sum(list2))

# 4. Find the largest and smallest number from a given list.

lst = [10,20,40,50,9]
print("maxlist : ",max(lst))
print("minlist : ",min(lst))

# 5. Create a new list which contains the specified numbers after removing the even numbers from a
# predefined list.

num = [10,20,12,7,8,9,20]
num = [x for x in num if x%2!=0]
print(num)

# 6. Create a list of elements such that it contains the squares of the first and last 5 elements between
# 1 and30 (both included).

def printValues():
	l = list()
	for i in range(1,31):
		l.append(i**2)
	print(l[:5]+l[-5:])

printValues()

# 7. Write a program to replace the last element in a list with another list.
# Sample input: [1,3,5,7,9,10], [2,4,6,8]
# Expected output: [1,3,5,7,9,2,4,6,8]

num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]
num1[-1:] = num2
print(num1)

# 8. Create a new dictionary by concatenating the following two dictionaries:
# Sample input: a={1:10,2:20} b={3:30,4:40}
# Expected output: {1:10,2:20,3:30,4:40}

a={1:10,2:20} 
b={3:30,4:40}
c ={}
for i in (a,b): c.update(i)
print(c)

# 9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
# and n(both 1 and n included).
# Sample input: n=5
# Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}

a = int(input("enter number: "))
d = dict()

for x in range(1,a+1):
    d[x] = x*x
print(d)

# 10. Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string.
# Sample input: 34,67,55,33,12,98
# Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)

# inp = [34,67,55,33,12,98]
# list = inp.split(",")
# tuple = tuple(list)
# print(list)
# print(tuple)

inpnumbers = input("Input numbers : ")
list = inpnumbers.split(",")
tuple = tuple(list)
print(list)
print(tuple)