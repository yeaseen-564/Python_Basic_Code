# # for loop basic code :
# for _ in range (10):
#     print(_)

prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"Total: {total}")

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")


numbers = [5, 2, 5, 2, 5]
for y in numbers:
    output = ""
    for x in range(y):
        output += "x"
    print(output)


