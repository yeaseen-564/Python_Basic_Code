customer = {
    "name": "Yeaseen",
    "age": "16",
    "is_verified": True
}

print(customer["name"])
print(customer.get("birthdate"))
# print(customer["class"])

customer["name"] = "Yeaseen Ahmed"
print(customer["name"])
