# Mike's exercise 1 - MD5 hash of a user input string

import hashlib

my_string = input("Please enter a string to get MD5 has from: ").strip()

my_bytestring = my_string.encode() # from string to bytestring

my_hash =  hashlib.md5(my_bytestring).hexdigest()

print(my_hash)
#print(f"The INPUT was: {my_string}")
#print(f"The MD5 hash is ==>  {my_hash}")