import hashlib

while user_say := input('Enter some text : ').strip():
    m = hashlib.md5()
    m.update(b'{user_say}')
    output = m.hexdigest()
    print(output)