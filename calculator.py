# calculator.py

def add(x,y):
    z = x+y # this is a local variable, so z is not defined anywhere else in the code
    print("{} + {} = {}".format(x,y,z))    
    return z
def subtract(x,y):
    z = x-y
    print("{}-{}={}".format(x,y,z))
    return z
def multiply(x,y):
    z = x*y
    print("{}*{}={}".format(x,y,z))
    return z

x = input("Enter a letter: ")
print("You entered {}".format(x))
print("This is a line of code.")

if x == "a":
    d = add(100,250)
    if d>100:
        print("This number is too high.")
elif x =="b":
    x = 20
    y = -3
    z = subtract(x,y)
    print("{}-{} = {}".format(x,y,z))
elif x == "c":
    x = 34
    y = 32
    z = multiply(x,y)
    print("{}*{} = {}".format(x,y,z))
else:
    print("The {} command is not recognized.".format(x))

print("Done")