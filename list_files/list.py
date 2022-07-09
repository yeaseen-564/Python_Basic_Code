# # Use of len() to know the number of any input,for EXAMPLE! run it:
# saarc = ["Bangladesh", "Nepal", "Afghanistan", "Bhutan", "Pakistan", "India", "Srbijanka"]
# #
# #
# # saarc[1] = "yy"
# #
# #
# print(saarc, " , Number of country is : ", len(saarc))
# print(saarc[0:3])
# print(saarc[4:-1])
#
# # Finding the largest number:
# numbers = [4, 4, 34, 43, 342, 3423, 234, 4, 324, 3, 423, 45, 5454, 554, 545, 454]
#
# max_n = numbers[0]
# for number in numbers:
#     if number > max_n:
#         max_n = number
# print(max_n)

# Two-dimensional list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0][0] = 45
print(matrix[1][1])
print(matrix[0][2])
print(matrix[0][0])
#
print('-=-=-=-=')
for row in matrix:
    for item in row:
        print(item)

# # Removing duplicates:
# numbers = [4, 5, 7, 8, 6, 4, 5, 45, 45, 34, 4, 4, 3, 23, 4, 6, 76, 7, 5, 4, 3, 23, 2, 0]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)


# numbers = [1, 2, 3, 44, 44, 3, 2, 4, 6, 7, 5, 4, 4, 23, 45, 4, 4, 5, 6, 7, 8, 3, 45, ]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
#         uniques.sort()
# print(uniques)
