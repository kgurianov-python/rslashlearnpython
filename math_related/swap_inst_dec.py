import math

test = 12.5648797
print(test*10)
print(test*100)
print(test*1000)
print(test*10000)
print(test*1000000)
print(test*10000000)


dec_part, int_part = math.modf(test)
print(int_part, dec_part)
int_part = int(int_part)


def reverse_number(in_val: int) -> int:
    result = 0
    while in_val > 0:
        in_val, rem = divmod(in_val, 10)
        result = result * 10 + rem
    return result


print(reverse_number(int(int_part)))
print(reverse_number(int(dec_part * 10 ** 2)))


res = reverse_number(int(dec_part * 10 ** 2)) + reverse_number(int(int_part)) / (10 ** (
            math.floor(math.log10(int(int_part))) + 1))
print(res)
