expression = input("Expression: ")
x,y,z = expression.split(" ")

x = float(x)
z = float(z)

if y == "+":
    print(round(x + z,1))
elif y == "-":
    print(x - z)
elif y == "/":
    print(x / z)
elif y == "*":
    print (x * z)
else:
    print("Please use +, -, *, or /.")
