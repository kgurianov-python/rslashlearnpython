from python_data_types.python_collections import itertools_tries


def main():
    # values = 'Julia, Lucas, Mia'
    comb_list = itertools_tries.combinations(range(4), r=2)
    print("Combinations:")
    for comb in comb_list:
        print(comb)

    perm_list = itertools_tries.permutations(range(4), r=2)
    print("Permutations:")
    for perm in perm_list:
        print(perm)


if __name__ == '__main__':
    main()
