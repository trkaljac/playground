import fractions


fraction_input = input("Fraction: ").split('/')
numerator = int(fraction_input[0])
denominator = int(fraction_input[1])

try:
    fraction = fractions.Fraction(numerator, denominator)
    percentage = fraction * 100
    print(f"{fraction} is equal to {percentage:.2f}%")
except (ValueError, ZeroDivisionError):
    print("Invalid fraction input")




if  fraction == fractions.Fraction(4, 4):
    print("F")
elif fraction == fractions.Fraction(0, 4):
    print("E")
