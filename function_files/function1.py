# Global and Local function:
def func(x):
    # here x = 20,Global
    print("Global function is : ",x)
    x=10
    #  here x = 10,Local
    print("Local function is : ",x)

x=20
# here x = 20
print(x)
func(x)
