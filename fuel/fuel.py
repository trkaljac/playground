import fractions

fractionInput=input("Fraction: ").split('/')
numerator = int(fraction_input[0])
denominator = int(fraction_input[1])

try:
    if not input.isnumeric():
        input = fractions.Fraction(input)
except (ValueError,ZeroDivisionError):
    print(input + " is not a number")

if input == 1/2 :
    print("50%")
if input == 1/4:
    print("25%")
if input == 3/4:
    print("75%")
if input == 4/4:
    print("F")
if input == 0/4:
    print("E")
