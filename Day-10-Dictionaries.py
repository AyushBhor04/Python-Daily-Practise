# Day 10 — Dictionaries
# 🟢 Easy

# Question 1:
# Create a dictionary containing a student's name, age, and course. Print the dictionary.
# dict={
#     "name":["Ayush","Varun","Pranav"],
#     "age":[12,23,45],
#     "course":["ML","Sw","AI"]
# }
# print(dict)

# Question 2:
# Create a dictionary containing 5 key-value pairs and print each key separately.
# dict={
#     "name":"Ayush",
#     "age":23,
#     "course":"ML",
#     "city":"Navi Mumbai",
#     "Salary":250000
# }
# print(dict.keys())

# Question 3:
# Take a dictionary and print all its values.
# dict={
#     "name":"Ayush",
#     "age":23,
#     "course":"ML",
#     "city":"Navi Mumbai",
#     "Salary":250000
# }
# print(dict.values())

# Question 4:
# Take a dictionary and search for a key entered by the user. Print whether the key exists or not.
# dict = {
#     "name": "Ayush",
#     "age": 23,
#     "course": "ML",
#     "city": "Navi Mumbai",
#     "Salary": 250000
# }
# key = input("Enter the key to search: ")
# if key in dict:
#     print("Key exists")
# else:
#     print("Key does not exist")

# Question 5:
# Create a dictionary and add a new key-value pair to it.
# dict={
#     "name":"Ayush",
#     "age":23,
#     "course":"ML",
#     "city":"Navi Mumbai",
#     "Salary":250000
# }
# dict.update({"Gender":"male"})
# print(dict)

# 🟡 Medium

# Question 6:
# Create a dictionary containing student names and their marks. Print the marks of a student whose name is entered by the user.
# students = {
#     "Ayush": 90,
#     "Pranav": 98,
#     "Varun": 92
# }
# name = input("Enter a student's name: ")
# if name in students:
#     print("Marks:", students[name])
# else:
#     print("Student not found")

# Question 7:
# Take a dictionary of products and their prices. Find the total price of all the products.
# Question 7
# products = {
#     "Laptop": 50000,
#     "Mouse": 1000,
#     "Keyboard": 2000,
#     "Monitor": 15000
# }
# total = 0
# for price in products.values():
#     total += price
# print(total)

# Question 8:
# Take a dictionary containing numbers as keys and their values. Print all key-value pairs using a for loop.
# Question 8
# numbers = {
#     1: 10,
#     2: 20,
#     3: 30,
#     4: 40
# }
# for key, value in numbers.items():
#     print(key, value)

# Question 9:
# Take a dictionary of students and their marks. Find the student who has the highest marks.
# Question 9
# students = {
#     "Ayush": 85,
#     "Pranav": 92,
#     "Varun": 88,
#     "Rahul": 79
# }
# highest = 0
# student = ""
# for name, marks in students.items():
#     if marks > highest:
#         highest = marks
#         student = name
# print(student, highest)

# Question 10:
# Take a dictionary and count how many key-value pairs it contains.
# Question 10
# students = {
#     "Ayush": 85,
#     "Pranav": 92,
#     "Varun": 88,
#     "Rahul": 79
# }
# print(len(students))

# Question 11:
# Take two dictionaries and combine them into a single dictionary.
# Question 11
# dict1 = {
#     "name": "Ayush",
#     "age": 23
# }
# dict2 = {
#     "city": "Navi Mumbai",
#     "course": "ML"
# }
# dict1.update(dict2)
# print(dict1)

# Question 12:
# Take a dictionary of student names and marks. Create a new dictionary containing only students who scored 60 or more.
# Question 12
# students = {
#     "Ayush": 85,
#     "Pranav": 55,
#     "Varun": 72,
#     "Rahul": 48,
#     "Sneha": 91
# }
# passed = {}
# for name, marks in students.items():
#     if marks >= 60:
#         passed[name] = marks
# print(passed)