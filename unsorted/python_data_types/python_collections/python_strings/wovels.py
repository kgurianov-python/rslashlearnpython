import logging

log_format = '%(name)s : %(levelname)s : %(asctime)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
logger = logging.getLogger('logger')

VOWELS = 'aeiou'


def main():
    word = input(f'Enter a word to search:\t')
    stack = set()
    for character in VOWELS:
        if character in word.lower():
            stack.add(character)
    print(f'List of vowels given in the given word is: {stack},\nStack length: {len(stack)}')


if __name__ == '__main__':
    main()
