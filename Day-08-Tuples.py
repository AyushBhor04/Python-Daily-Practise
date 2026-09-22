# Day 8 — Tuples
# 🟢 Easy

# Question 1:
# Create a tuple containing 5 numbers and print the tuple.
# tup=(1,2,3,4,5)
# print(tup)

# Question 2:
# Create a tuple containing different data types and print each element.
# tup=(1,1.65,"Ayush",True)
# print(tup)

# Question 3:
# Take a tuple and print its first and last elements.
# tup=(1,2,3,4,5)
# print("First element :",tup[0])
# print("Last element :",tup[-1])

# Question 4:
# Take a tuple as input and find its length.
# tup=tuple(input("Enter a tuple : ").split())
# print(len(tup))

# Question 5:
# Take a tuple of numbers and print each element using a for loop.
# tup=tuple(input("Enter a tuple of numbers : "))
# for i in tup:
#     print(i)

# 🟡 Medium

# Question 6:
# Take a tuple of numbers and calculate the sum of all its elements.
# tup=(1,2,3,4,55,66,77,99,12)
# print("Sum of element :",sum(tup))

# Question 7:
# Take a tuple of numbers and find the largest and smallest elements.
# tup=(1,2,3,4,55,66,77,99,12)
# print("Max element :",max(tup))
# print("Min element :",min(tup))

# Question 8:
# Take a tuple and search for an element entered by the user. Print whether it exists or not.
# tup = (1, 2, 3, 4, 55, 66, 77, 99, 12)
# num = int(input("Enter the number to be searched: "))
# if num in tup:
#     print("Element exists")
# else:
#     print("Element does not exist")

# Question 9:
# Take a tuple containing repeated elements and count how many times a particular element appears.
# tup=(1,2,3,4,55,66,77,99,12)
# num=int(input("Enter the number whose occurence is to be found : "))
# print(tup.count(num))

# Question 10:
# Take a tuple of numbers and create a new tuple containing only the even numbers.
# tup=(1,2,3,4,55,66,77,99,12)
# tup_new=[]
# for i in tup:
#     if i%2==0:
#         tup_new.append(i)
# tup_new=tuple(tup_new)
# print(tup_new)

# Question 11:
# Take a tuple and reverse it using slicing.
# tup=(1,2,3,4,55,66,77,99,12)
# print(tup[::-1])

# Question 12:
# Take a tuple containing numbers and convert it into a list. Then add a new number to the list and convert it back into a tuple.
# tup=(1,2,3,4,55,66,77,99,12)
# tup=list(tup)
# tup.append(4)
# tup=tuple(tup)
# print(tup)
# print(type(tup))