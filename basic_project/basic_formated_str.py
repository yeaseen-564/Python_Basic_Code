first = "Yeaseen"
last = "Ahmed"
message = first + " [ " + last + " ] is a coder"
# Here by using {} you can formate any String :
message_1 = f"{first} [ {last} ] is a coder"
print(message)
print(message_1.upper())
print(message_1.lower())
print(len(message_1))
print(message.find("Y"))
print(message.replace("Yeaseen", "yeaseen"))
print("Python" in message)
print(f"Hi I am {first} {last}")
