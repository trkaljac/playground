import fractions
import math

fraction_input = input("Fraction: ").split('/')
numerator = int(fraction_input[0])
denominator = int(fraction_input[1])
percentage = (numerator / denominator) * 100
percentage = f"{percentage:.0f}%"

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(percentage)
try:
    ...
except ValueError:
    ...
except ZeroDivisionError:
    ...



