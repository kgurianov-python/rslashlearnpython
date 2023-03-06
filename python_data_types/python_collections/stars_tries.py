def chunked(iterable, n):
    return zip(*[iter(iterable)] * n)


def main():
    nums = list(range(20))
    print(f'Packed: {chunked(nums, 10)}')
    print(f'Unpacked:')
    print(*chunked(nums, 10), sep="\r\n")


if __name__ == '__main__':
    main()
