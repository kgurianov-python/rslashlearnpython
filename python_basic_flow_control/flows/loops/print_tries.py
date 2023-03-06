def evens(max: int = 10) -> str:
    i = 0
    while i <= max - 1:
        if i % 2 == 0:
            print(i, end=(","))
        i += 1


def main():
    max_num = 20
    evens_list = [str(i) for i in range(max_num) if i % 2 == 0]
    evens_str = f"\'{','.join(evens_list)}\'"
    print(evens_str)

    evens(max_num)


if __name__ == '__main__':
    main()
