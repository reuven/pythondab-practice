# Mike Seidel - Modules Exercise #1 String character type counts

import string

totals = {'lower': 0, 
          'upper': 0, 
          'digits': 0,
          'punctuation': 0}

my_string = input("Please enter a string to analyze: ").strip()

my_string = my_string.replace(" ", "") # squash spaces that were messing with totals

for one_char in my_string:
    
    if one_char in string.ascii_lowercase:
        totals["lower"] += 1

    elif one_char in string.ascii_uppercase:
        totals["upper"] += 1

    elif one_char in string.digits:
        totals["digits"] += 1

    elif one_char in string.punctuation:
        totals["punctuation"] += 1

    else:
        print(f"Unknown: {one_char}")
    
for k, v in totals.items():
    print(f"{k} : {v}")