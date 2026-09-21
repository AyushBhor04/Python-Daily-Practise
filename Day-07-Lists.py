# Day 7 — Lists
# 🟢 Easy

# Question 1:
# Create a list of 5 numbers and print the list.
# lis=[1,2,3,4,5]
# print(lis)

# Question 2:
# Take 5 numbers as input, store them in a list, and print the list.
# lis=list(input("Enter integer values : "))
# print(lis)

# Question 3:
# Create a list of numbers and print the first and last elements.
# lis=[1,2,3,4,5]
# print(lis[0])
# print(lis[-1])

# Question 4:
# Take a list of numbers and find its length.
# lis=[1,2,3,4,5,6,7,89]
# print("The length of the sting is : ",len(lis))

# Question 5:
# Take a list of numbers and print each element one by one using a loop.
# lis=[1,3,7,8,7,3,1,25,63,13]
# for i in lis:
#     print(i)
#     i=i+1

# 🟡 Medium

# Question 6:
# Take a list of numbers and calculate the sum of all its elements.
# lis=[1,3,7,8,7,3,1,25,63,13]
# sum=0
# for i in lis:
#     sum=sum+i
#     i=i+1
# print(sum)
# OR
# print(sum(lis))

# Question 7:
# Take a list of numbers and find the largest and smallest element.
# lis=[1,3,7,8,7,3,1,25,63,13]
# print(max(lis))
# print(min(lis))

# Question 8:
# Take a list of numbers and count how many even and odd numbers it contains.
# lis=[1,2,3,4,5,6,7,8,9]
# even=0
# for i in lis:
#     if i%2==0:
#         even+=1
#     i+=1
# print("Total number of even numbers : ",even)
# print("Total number of odd numbers : ",len(lis)-even)

# Question 9:
# Take a list of numbers and search for a number entered by the user. Print whether the number exists in the list or not.
# lis=[1,3,7,8,7,3,1,25,63,13]
# num=int(input("Enter any number : "))
# for i in lis:
#     if i==num:
#         print("Number entered exists")
#         break  
#     i=i+1    
# else:
#     print("Number does not exist")

# Question 10:
# Take a list of numbers and create a new list containing only the positive numbers.
# lis_1=[1,-3,7,-8,-7,3,1,25,-63,13]
# lis_2=[]
# for i in lis_1:
#     if i>=0:
#         lis_2.append(i)
#     i=i+1
# print(lis_2)

# Question 11:
# Take a list of numbers and reverse the list without using the reverse() method.
# lis = [1, -3, 7, -8, -7, 3, 1, 25, -63, 13]
# i = len(lis) - 1
# while i >= 0:
#     print(lis[i])
#     i = i - 1

# Question 12:
# Take a list of numbers and remove all duplicate elements, keeping only unique values.
# lis = [1, 2, 3, 2, 4, 1, 5, 3, 6]
# lis = list(set(lis))
# print(lis)