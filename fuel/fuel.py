import fractions

input("Fraction: ")

try:
    if not input.isnumeric():
        input = fractions.Fraction(input)
except ValueError:
    throw ValueError(myinput + " is not a number")
except ZeroDivisionError:
    pass