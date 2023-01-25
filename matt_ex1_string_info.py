import string

while user_say := input('Enter some text : ').strip():

    counts = {'digits':0, 'uppercase_letters':0, 'lowercase_letters':0, 'punctuation':0}

    for one_string in user_say:
        if one_string in string.digits:
            counts['digits'] += 1
        elif one_string in string.ascii_uppercase:
            counts['uppercase_letters'] += 1
        elif one_string in string.ascii_lowercase:
            counts['lowercase_letters'] += 1
        elif one_string in string.punctuation:
            counts['punctuation'] += 1
        else:
            print(f'Unknown character: {one_string}.')

    for key, value in counts.items():
        print(f'{key}: {counts[key]}')