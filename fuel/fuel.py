import fractions

fractionInput=input("Fraction: ").split('/')
numerator = int(fractionInput[0])
denominator = int(fractionInput[1])

try:
    if not input.isnumeric():
        input = fractions.Fraction(input)
except (ValueError,ZeroDivisionError):
    print(input + " is not a number")

if fraction == fractions.Fraction(1, 2):
    print("50%")
elif fraction == fractions.Fraction(1, 4):
    print("25%")
elif fraction == fractions.Fraction(3, 4):
    print("75%")
elif fraction == fractions.Fraction(4, 4):
    print("F")
elif fraction == fractions.Fraction(0, 4):
    print("E")
