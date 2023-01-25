import fractions

while user_input := input('Enter a float : ').strip():
    output = fractions.Fraction(f'{user_input}\t\n')
    print(output)