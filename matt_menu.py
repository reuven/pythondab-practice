def menu(*args):
    options = '/'.join(sorted(args)
    while s:= input('Enter a choice {options}:').strip():
        if s in args:
            return s
        print(f'{s} is not in {args}')
        
        
if __name__ == '__main__':
    user_input = menu('a', 'b', 'c')
    print(f'You chose {user_input}.')
    