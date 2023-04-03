from math import isqrt

def is_perfect(get_num):
    sum1 = 0
    for val in range(1, (get_num // 2)+1):
        if get_num % val == 0:
            sum1 = sum1 + val

    if sum1 == get_num:
        return True
    else:
        return False

# noinspection PyMissingOrEmptyDocstring
def is_pronic(num: int) -> bool:
    if num % 2:
        return False
    high = isqrt(num) + 1
    while (val := (high - 1) * high) >= num:
        if val == num:
            return True
        high -= 1
    return False


# noinspection PyMissingOrEmptyDocstring
def main():
    while (test_num := int(input('Please enter an integer number to test or "-1" to quit: '))) != -1:
        if test_num < -1:
            print(f'"{test_num}" is not a positive number. Please try again')
            continue
        result = is_pronic(test_num)
        print(f"{test_num} is {'not ' if not result else ''}a pronic number.")

    return 'Thanks for playing!'


if __name__ == '__main__':
    # main()
    print([i for i in range(1000) if is_perfect(i)])