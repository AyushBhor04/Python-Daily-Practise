# Day 11 — Functions
# 🟢 Easy

# Question 1:
# Create a function that prints "Hello, World!".
# def welcome ():
#     print("Hello, World!")
# welcome()

# Question 2:
# Create a function that takes a name as an argument and prints a greeting message.
# def welcome (person):
#     print("Hello, ",person)
# name=input("Enter your name : ")
# welcome(name)

# Question 3:
# Create a function that takes two numbers and prints their sum.
# def add(x,y):
#     print("Addition result : ",x+y)
# a=int(input("Enter any number : "))
# b=int(input("Enter any number : "))
# add(a,b)

# Question 4:
# Create a function that takes a number and prints whether it is even or odd.
# def parity(x):
#     if(x%2==0):
#         print("Entered number is even")
#     else:
#         print("Entered number is odd")
# num=int(input("Enter any number : "))
# parity(num)

# Question 5:
# Create a function that takes a number and returns its square.
# def square(x):
#     print("Square of the entered value is : ",x**2)
# num=int(input("Enter any number : "))
# square(num)

# 🟡 Medium

# Question 6:
# Create a function that takes two numbers and returns the larger number.
# def larger(x,y):
#     if(a>b):
#         print("A is greater",x)
#     else:
#         print("B is greater",y)
# a=int(input("Enter any number : "))
# b=int(input("Enter any number : "))
# larger(a,b)

# Question 7:
# Create a function that takes three numbers and returns their average.
# def avg(a,b,c):
#     print("The average of the three values is : ",(a+b+c)/3)
# a=int(input("Enter any number : "))
# b=int(input("Enter any number : "))
# c=int(input("Enter any number : "))
# avg(a,b,c)

# Question 8:
# Create a function that takes a list of numbers and returns the sum of all elements.
# def calculate_sum(lis):
#     return sum(lis)
# list_1 = list(map(int, input("Enter a list of values: ").split()))
# print("The sum of elements in the list is:", calculate_sum(list_1))

# Question 9:
# Create a function that takes a list of numbers and returns the largest number.
# def largest(lis):
#     return max(lis)
# list_1 = list(map(int, input("Enter a list of values: ").split()))
# print("The largest of elements in the list is:", largest(list_1))

# Question 10:
# Create a function that takes a string and returns the number of vowels in it.
# vow = ["a", "e", "i", "o", "u"]
# def vowel(strs):
#     count = 0
#     for i in range(len(strs)):
#         if strs[i].lower() in vow:
#             count += 1

#     print("The number of vowels in the entered string are:", count)
# str_1 = input("Enter any string: ")
# vowel(str_1)

# Question 11:
# Create a function that takes a number and returns its factorial.
# def fact(n):
#     prod=1
#     for i in range(1,n+1):
#         prod=prod*i
#     return prod
# num=int(input("Enter any number : "))
# ans=fact(num)
# print(ans) 

# Question 12:
# Create a function that takes a list of numbers and returns a new list containing only the even numbers
# def even(lis_2):
#     new_list = []
#     for i in lis_2:
#         if i % 2 == 0:
#             new_list.append(i)
#     return new_list
# lis_1 = list(map(int, input("Enter values for a list: ").split()))
# ans = even(lis_1)
# print(ans)