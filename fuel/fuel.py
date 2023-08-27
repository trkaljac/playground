import fractions
import math


fraction_input = input("Fraction: ").split('/')
numerator = int(fraction_input[0])
denominator = int(fraction_input[1])
percentage = (numerator / denominator) * 100
print(f"{percentage:.0f}%")

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("E")

try:
      fraction = fractions.Fraction(numerator, denominator)
except (ValueError, ZeroDivisionError):
      pass



