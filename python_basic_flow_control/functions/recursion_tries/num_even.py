import logging

log_format = '%(asctime)s [%(name)s]  [%(levelname)s] : %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
logger = logging.getLogger('logger')


def get_number():
    while True:
        number = int(input('Enter a number greater than 2'))
        if number <= 2:
            print('greater than two!')
            continue
        return number


def find_less_two(number, count):
    if number < 2:
        return count
    else:
        count += 1
        return find_less_two(number / 2, count)


def find_less_two_new(number: int) -> int:
    if number < 2:
        return 0

    return 1 + find_less_two_new(number / 2)


def main():
    start = get_number()
    res = find_less_two_new(start)
    print(f"{res=}")

    counter = 0
    print(find_less_two(start, counter))


if __name__ == '__main__':
    main()
