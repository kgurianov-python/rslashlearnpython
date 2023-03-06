import random


def main():
    max_size = 10
    rand_place = random.randint(0, max_size - 1)
    tst_tuple = (0,) * rand_place + \
                (1,) + \
                (0,) * (max_size - rand_place - 1)

    print(f'Length: {len(tst_tuple)}\n{tst_tuple=}')

    tst = (0,) + (1,) + (0,)
    print(f'{tst=}')

if __name__ == '__main__':
    main()
