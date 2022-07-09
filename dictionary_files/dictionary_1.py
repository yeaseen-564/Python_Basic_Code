phone = input("Phone: ")
digits_mapping = {"1": "one", "2": "two", "3": "three", "4": "four"}
output = ""
for characters in phone:
    output += digits_mapping.get(characters, "null") + " "
print(output)
