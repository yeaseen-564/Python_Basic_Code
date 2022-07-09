# Calculation with loop from (1 - [n-1]):
input_n=int(input("Please enter an integer to calculate : "))
result=0
for i in range (input_n+1):
    result=result+i
    print(i)    
print("You ans is : ", result)
