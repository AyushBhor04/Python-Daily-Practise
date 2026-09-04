# Day 3 — Conditional Statements
# 🟢 Easy

# Question 1:
# Take a number as input and check whether it is positive or negative.
# num=int(input("Enter any number : "))
# if(num<0):
#     print(num,"is negative")
# else:
#     print(num,"is positive")

# Question 2:
# Take a number as input and check whether it is even or odd.
# num=int(input("Enter any number : "))
# if(num%2==0):
#     print(num,"is even")
# else:
#     print(num,"is odd")

# Question 3:
# Take a person's age as input and check whether they are eligible to vote.
# Voting age: 18.
# age=int(input("Enter your age : "))
# if(age<18):
#     print(age,"is NOT eligible to vote")
# else:
#     print(age,"is eligible to vote")

# Question 4:
# Take two numbers as input and print which number is greater.
# a=int(input("Enter any number : "))
# b=int(input("Enter any number : "))
# if(a>b):
#     print(a,"is greater than",b)
# else:
#     print(b,"is greater than",a)

# Question 5:
# Take a number as input and check whether it is zero or not.
# num=int(input("Enter any number : "))
# if(num==0):
#     print(num,"is ZERO")
# else:
#     print(num,"is NON-ZERO")

# 🟡 Medium

# Question 6:
# Take three numbers as input and print the greatest number.
# x=int(input("Enter any number : "))
# y=int(input("Enter any number : "))
# z=int(input("Enter any number : "))
# if(x>y and x>z):
#     print(x,"is the greatest")
# elif(y>x and y>z):
#     print(y,"is the greatest")
# else:
#     print(z,"is the greatest")

# Question 7:
# Take a student's marks as input and print:
# "Pass" if marks are 40 or above
# "Fail" if marks are below 40
# marks=int(input("Enter your marks :"))
# if(marks>=40):
#     print("PASS")
# else:
#     print("FAIL")

# Question 8:
# Take marks as input and print the grade:
# 90–100 → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# Below 60 → F
# print("MARKS SHOULD BE IN THE RANGE 1-100")
# marks=int(input("Enter your marks :"))
# if(marks>=90 and marks<=100):
#     print("A")
# elif(marks>=80 and marks<=89):
#     print("B")
# elif(marks>=70 and marks<=79):
#     print("C")
# elif(marks>=60 and marks<=69):
#     print("D")
# elif(marks<60):
#     print("F")

# Question 9:
# Take a number as input and check whether it is divisible by both 5 and 10.
# num=int(input("Enter any number : "))
# if(num%2==0 and num%5==0):
#     print("Divisible by both 2 and 5")
# else:
#     print("Not divisible by both 2 and 5")

# Question 10:
# Take a person's age as input and classify them as:
# Below 13 → Child
# 13–19 → Teenager
# 20–59 → Adult
# 60 or above → Senior Citizen
# age=int(input("Enter your age :"))
# if(age<13):
#     print("CHILD")
# elif(age>=13 and age<=19):
#     print("TEENAGER")
# elif(age>=20 and age<=59):
#     print("ADULT")
# elif(age>=60):
#     print("SENIOR CITIZEN")

# Question 11:
# Take three numbers as input and print the smallest number.
# x=int(input("Enter any number : "))
# y=int(input("Enter any number : "))
# z=int(input("Enter any number : "))
# if(x<y and x<z):
#     print(x,"is the smallest")
# elif(y<x and y<z):
#     print(y,"is the smallest")
# else:
#     print(z,"is the smallest")

# Question 12:
# Take a year as input and check whether it is a leap year or not.
# year = int(input("Enter a year: "))
# if year % 400 == 0:
#     print("Leap year")
# elif year % 100 == 0:
#     print("Not a leap year")
# elif year % 4 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")