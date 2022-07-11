numbers = [1, 3, 2, 6, 5, 4]
print(numbers)

# Knowing the index:
print(">>> To know the index:")
print("Index of 6 is", numbers.index(6))
print("Index of 2 is", numbers.index(2))

# Sorting the li:
print(">>> Sorting the li:")
numbers.sort()
print(numbers)

# Reverse print:
print(">>> Printing in reverse:")
numbers.reverse()
print(numbers)

# adding any item in the li:
print(">>> Adding any item in the List:")
numbers.append(77)
print(numbers)

# Removing any item from the li:
print(">>> Removing any item from the li:")
numbers.remove(77)
print(numbers)

# Use of the pop function:
print(">>> Use of the pop function:")
print("-=-=-=-")
numbers.pop()
print(numbers)

numbers.pop(0)
print(numbers)
print("-=-=-=-")

# Clearing all the items from the li:
print(">>> Clearing all the items from the li:")
numbers.clear()
print(numbers)


# command = ""
# while command != "0":
#     # Here 0  is a str
#     _input = input(">>> ")
#     if _input == "1":
#         # Here 1 is a str
#         print("You passed 0 argument")
#     elif _input == "0":
#         # here 0 is a str
#         break
#     else:
#         print("???")
