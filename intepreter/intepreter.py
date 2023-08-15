intepreter = input("Expression: ")
x, y, z = intepreter.split(" ")
x = float(x)
z = float(z)
if y == ("+"):
    print(x+z)