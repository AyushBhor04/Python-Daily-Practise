# Day 4 — Strings
# 🟢 Easy

# Question 1:
# Take a string as input and print its length.
# str=input("Enter a string : ")
# print("Length of the entered string is : ",len(str))

# Question 2:
# Take the user's name as input and print it in uppercase.
# name=input("Enter user's name : ")
# print("Name in uppercase : ",name.upper())

# Question 3:
# Take the user's name as input and print it in lowercase.
# name=input("Enter user's name : ")
# print("Name in lowercase : ",name.lower())

# Question 4:
# Take a string as input and print its first character and last character.
# name=input("Enter your name : ")
# print("First character : ",name[0])
# print("Last character : ",name[-1])

# Question 5:
# Take a string as input and count how many times the letter "a" appears in it.
# name=input("Enter a string : ")
# print("Number of occurences : ",name.count("a"))

# 🟡 Medium

# Question 6:
# Take a string as input and check whether it starts with "A".
# name = input("Enter a string : ")
# print(name.startswith("A"))

# Question 7:
# Take a string as input and check whether it ends with "ing".
# name = input("Enter a string : ")
# print(name.endswith("ing"))

# Question 8:
# Take a sentence as input and count the number of spaces in it.
# name = input("Enter a string : ")
# print("The count of spaces in the string is : ",name.count(" "))

# Question 9:
# Take a string as input and reverse it.
# str=input("Enter a string value : ")
# print("The reverse of the entered string is : ",str[::-1])

# Question 10:
# Take a string as input and check whether it is a palindrome.
# str=input("Enter a string value : ")
# if(str==str[::-1]):
#     print("String is Palindrome")
# else:
#     print("Not Palindrome")

# Question 11:
# Take the user's full name as input and print the number of characters in the name, excluding spaces.
# name = input("Enter your full name : ")
# name = name.replace(" ", "")
# print("Number of characters : ", len(name))

# Question 12:
# Take a sentence as input and replace every space " " with a hyphen "-".
# sent=input("Enter a sentence : ")
# print(sent.replace(" ","-"))