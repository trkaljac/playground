import fractions

input("Fraction: ").split('/')

try:
    if not input.isnumeric():
        input = fractions.Fraction(input)
except ValueError:
    print(input + " is not a number")
except ZeroDivisionError:
    pass