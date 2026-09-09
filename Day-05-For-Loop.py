# Day 5 — for Loop
# 🟢 Easy

# Question 1:
# Print the numbers from 1 to 10 using a for loop.
# for i in range(1,11):
#     print(i) 

# Question 2:
# Take a number n as input and print the numbers from 1 to n.
# n=int(input("Enter any value : "))
# for i in range(1,n+1):
#     print(i)

# Question 3:
# Print all even numbers from 1 to 20 using a for loop.
# for i in range(1,21):
#     if(i%2==0):
#         print(i) 

# Question 4:
# Print all odd numbers from 1 to 20 using a for loop.
# for i in range(1,21):
#     if(i%2!=0):
#         print(i)

# Question 5:
# Take a number as input and print its multiplication table from 1 to 10.
# n=int(input("Enter any number : "))
# for i in range(1,11):
#     print(i*n) 

# 🟡 Medium

# Question 6:
# Take a number n as input and calculate the sum of all numbers from 1 to n.
# n=int(input("Enter any number : "))
# sum=0
# for i in range(1,n+1):
#     sum=i+sum
# print(sum)

# Question 7:
# Take a number n as input and calculate the sum of all even numbers from 1 to n.
# n=int(input("Enter any number : "))
# sum=0
# for i in range(1,n+1):
#     if(i%2==0):
#         sum=i+sum
# print(sum)

# Question 8:
# Take a number n as input and print all numbers between 1 and n that are divisible by 3.
# n=int(input("Enter any number : "))
# sum=0
# for i in range(1,n+1):
#     if(i%3==0):
#         print(i)

# Question 9:
# Take a string as input and print each character on a separate line using a for loop.
# inp=input("Enter a string value : ")
# for i in inp:
#     print(i)

# Question 10:
# Take a string as input and count the number of vowels (a, e, i, o, u) in it using a for loop.
# vow=["a","e","i","o","u"]
# str=input("Enter a string : ")
# count=0
# for i in str :
#     if(i in vow ):
#         count=count+1
# print(count) 

# Question 11:
# Take a number as input and calculate its factorial using a for loop.
# n=int(input("Enter any number : "))
# prod=1
# for i in range(1,n+1):
#     prod=i*prod
# print("Factorial of the number you entered is",prod)

# Question 12:
# Take a number n as input and print the following pattern:
# *
# **
# ***
# ****
# *****
# n=int(input("Enter any value :"))
# for i in range(1,n+1):                          #rows
#     for j in range(1,i+1):                      #starts
#         print("*",end="")
#     print()                                     #move to next row