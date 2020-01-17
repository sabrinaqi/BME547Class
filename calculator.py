# calculator.py

def add(x,y):
    z = x+y # this is a local variable, so z is not defined anywhere else in the code  
    return z
def subtract(x,y):
    z = x-y
    return z
def multiply(x,y):
    z = x*y
    return z
def divide(x,y):
    z = x/y
    return z

x = input("Enter a letter, where a = add, s = subtract, m = multiply, and d = divide: ")
y = input("Enter a number: ")
y_num = float(y)
z = input("Enter another number: ")
z_num = float(z)
print("You entered {}".format(x))

if x == "a":
    z = add(y_num,z_num)
    print("{}+{} = {}".format(y_num,z_num,z))
elif x =="s":
    z = subtract(y_num,z_num)
    print("{}-{} = {}".format(y_num,z_num,z))
elif x == "m":
    z = multiply(y_num,z_num)
    print("{}*{} = {}".format(y_num,z_num,z))
elif x == "d":
    z = divide(y_num,z_num)
    print("{}/{} = {}".format(y_num,z_num,z))
else:
    print("The {} command is not recognized.".format(x))

print("Done")