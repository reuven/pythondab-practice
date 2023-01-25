# Mike's float to fraction 

import fractions

my_input = input("Please enter a float to convert to a fraction: ").strip()

my_float = float(my_input)

my_fraction = fractions.Fraction(my_float)

print(f"The fraction is: {my_fraction.numerator} / {my_fraction.denominator}")

# Matt's comment : very nice