# Day 6 — while Loop
# 🟢 Easy

# Question 1:
# Print the numbers from 1 to 10 using a while loop.
# n=1
# while n<11:
#     print(n)
#     n+=1

# Question 2:
# Take a number n as input and print the numbers from 1 to n.
# n=int(input("Enter any number : "))
# num=1
# while num<=n:
#     print(num)
#     num+=1

# Question 3:
# Print all even numbers from 1 to 20 using a while loop.
# print("Even numbers from 1 to 20")
# n=1
# while n<=20:
#     if (n%2==0):
#         print (n)
#     n=n+1

# Question 4:
# Print all odd numbers from 1 to 20 using a while loop.
# print("Odd numbers from 1 to 20")
# n=1
# while n<=20:
#     if (n%2!=0):
#         print (n)
#     n=n+1

# Question 5:
# Take a number as input and print its multiplication table from 1 to 10.
# num=int(input("Enter any number : "))
# n=1
# while(n<=10):
#     print(num,"X",n,"=",n*num)
#     n=n+1

# 🟡 Medium

# Question 6:
# Take a number n as input and calculate the sum of all numbers from 1 to n.
# num=int(input("Enter any number :"))
# sum=0
# n=1
# while n<=num:
#     sum=sum+n
#     n=n+1
# print("The sum is : ",sum)

# Question 7:
# Take a number n as input and calculate the sum of all even numbers from 1 to n.
# num=int(input("Enter any number :"))
# sum=0
# n=1
# while n<=num:
#     if(n%2==0):
#         sum=sum+n
#     n=n+1
# print("The sum is : ",sum)

# Question 8:
# Take a number as input and print its digits one by one using a while loop.
# num = int(input("Enter a number: "))
# while num > 0:
#     digit = num % 10
#     print(digit)
#     num = num // 10

# Question 9:
# Take a number as input and count how many digits it contains.
# num = int(input("Enter a number: "))
# count = 0
# while num > 0:
#     count += 1
#     num = num // 10
# print("Number of digits:", count)

# Question 10:
# Take a number as input and calculate the sum of its digits.
# num = int(input("Enter a number: "))
# total = 0
# while num > 0:
#     digit = num % 10
#     total += digit
#     num = num // 10
# print("Sum:", total)

# Question 11:
# Take a number as input and reverse the number using a while loop.
# num = int(input("Enter a number: "))
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# print("Reverse:", reverse)

# Question 12:
# Take a number as input and check whether it is a palindrome number.
# num = int(input("Enter a number: "))
# original = num
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not a palindrome")