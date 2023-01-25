"""
Mike's menu.py for the modules lessons

"""
import sys


def menu(*args):
    while True:
        my_input = input(f"Enter your choice from {args}: ").strip()

        if not my_input:
            break

        if my_input in args:
            return my_input
        else:
            print(f'Your choice is not in the list: {my_input}')


if __name__ == '__main__':
    choice = menu(*sys.argv[1:])
    print(f'Your choice was -->  {choice}')
