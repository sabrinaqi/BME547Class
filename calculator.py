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

x = input("Enter a letter: ")
print("You entered {}".format(x))

if x == "a":
    z = add(47,7)
    print("{}+{} = {}".format(47,7,z))
elif x =="b":
    z = subtract(47,7)
    print("{}-{} = {}".format(47,7,z))
elif x == "c":
    z = multiply(47,7)
    print("{}*{} = {}".format(47,7,z))
elif x == "d":
    z = divide(47,7)
    print("{}/{} = {}".format(47,7,z))
else:
    print("The {} command is not recognized.".format(x))

print("Done")

"CHANGES"
"MORE CHANGES PART 2"
