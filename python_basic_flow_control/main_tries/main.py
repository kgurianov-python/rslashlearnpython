import os

import secondary

print(f'{secondary.TEST_CONSTANT}')
print(f'The value of {__name__=} in {os.path.basename(__file__)}')


def main():
    print(f'Main function in {os.path.basename(__file__)}')


if __name__ == '__main__':
    print(f'The file {os.path.basename(__file__)} has been executed directly')
    main()
