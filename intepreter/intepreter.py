intepreter = input("Expression: ")
x,y,z = intepreter.split(" ")

x = float(x)
z = float(z)

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "/":
    print(x / z)
elif y == "*":
    print(x * z)
else:
    print("Wrong input")