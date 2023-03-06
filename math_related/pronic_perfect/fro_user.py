import math

get_num = 0

def is_perfect(get_num):
    sum1 = 0
    for val in range(1, get_num):
        if get_num % val == 0:
            sum1 = sum1 + val

    if sum1 == get_num:
        return True
    else:
        return False


def is_pronic(get_num):
    if get_num % 2:  # equivalent to if (num % 2) == 1:
        return False

    i = 0  # function argument i is reassigned
    while i <= math.isqrt(get_num) + 1:
        if get_num == (i * (i + 1)):
            return True
            i += 1
        else:
            return False


def main():
    print([i for i in range(1000) if is_pronic(i)])
    print([i for i in range(1000) if is_perfect(i)])


if __name__ == '__main__':
    main()