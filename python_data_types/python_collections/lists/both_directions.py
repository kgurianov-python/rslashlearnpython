from typing import Iterable

list1 = ('a', 'b', 'c', 'd')
list2 = ('e', 'f', 'g', 'h')
list3 = ('h', 'j', 'k', 'l')
list4 = ('m', 'n', 'o', 'p', 'q')
list5 = ('r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

bigList = [list1, list2, list3, list4, list5]


def traverse_mirror2(items: Iterable):
    mid = len(items) // 2 + len(items) % 2
    result = []
    for i in range(mid):
        result.append(items[i])
        if items[-(i + 1)] != items[i]:
            result.append(items[-(i + 1)])
    return result


def traverse_mirror(items: Iterable):
    low = 0
    high = len(items) - 1
    result = []
    while low <= high:
        if low != high:
            result.append(items[low])
            result.append(items[high])
        else:
            result.append(items[low])
        low += 1
        high -= 1
    return result


def main():
    for small_list in bigList:
        print(f'Mirror 1: {traverse_mirror(small_list)}')

    for small_list in bigList:
        print(f'Mirror 2: {traverse_mirror2(small_list)}')


if __name__ == '__main__':
    main()
