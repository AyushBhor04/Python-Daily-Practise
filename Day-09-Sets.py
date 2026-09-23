# Day 9 — Sets
# 🟢 Easy

# Question 1:
# Create a set containing 5 numbers and print the set.
# sets={1,2,3,4,5,4,5}
# print(sets)
# print(type(sets))

# Question 2:
# Take 5 numbers as input, store them in a set, and print the set.
# sets=set(input("Enter integer values for set : "))
# print(sets)

# Question 3:
# Create a set and add a new element to it.
# sets={1,2,3,4,4,5}
# print(sets)
# sets.add(6)
# print(sets)

# Question 4:
# Create a set and remove an element entered by the user.
# sets={1,2,3,4,4,5}
# print(sets)
# num=int(input("Enter the value to be removed : "))
# sets.remove(num)
# print("Set after removal : ",sets)

# Question 5:
# Take a set and check whether a particular element exists in it.
# sets={1,2,3,4,4,5}
# print(sets)
# num=int(input("Enter the value to be checked : "))
# if num in sets:
#     print("Number exists")
# else:
#     print("Number doesnt exist")

# 🟡 Medium

# Question 6:
# Take two sets of numbers and find their union.
# a={1,2,3,4,5}
# b={4,5,6,7,8,9}
# result=a.union(b)
# print(result)

# Question 7:
# Take two sets of numbers and find their intersection.
# a={1,2,3,4,5}
# b={4,5,6,7,8,9}
# result=a.intersection(b)
# print(result)

# Question 8:
# Take two sets of numbers and find the elements that are present in the first set but not in the second set.
# a={1,2,3,4,5}
# b={4,5,6,7,8,9}
# result=a-b
# print(result)

# Question 9:
# Take a list containing duplicate numbers and convert it into a set to remove the duplicates.
# lists=list(input("Enter values with duplicates in a list : ").split())
# print(lists)
# lists=set(lists)
# print(lists)
# print(type(lists))

# Question 10:
# Take two sets and check whether they are equal.
# a={1,2,3,4}
# b={1,2,3,4}
# c={3,4,5,1,1}
# if(a==c):
#     print("Equal")
# else:
#     print("Not Equal")

# Question 11:
# Take a set of numbers and print each element using a for loop.
# sets=set(input("Enter values for a set : ").split())
# for i in sets:
#     print(i)

# Question 12:
# Take two sets of numbers and find all the elements that are present in either set but not in both sets.
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# result = a ^ b      #symmetric difference
# print(result)