import fractions
import math


fraction_input = input("Fraction: ").split('/')
numerator = int(fraction_input[0])
denominator = int(fraction_input[1])
print((numerator/denominator)* 100)

try:
      fraction = fractions.Fraction(numerator, denominator)
except (ValueError, ZeroDivisionError):
    print("Invalid fraction input")

