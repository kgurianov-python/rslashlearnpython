def sieve_of_sums(size: int, fragments: tuple[int] = (3, 5)):
    result = [False] * (size + 1)
    for fragment in fragments:
        result[fragment] = True

    for idx in range(min(fragments), size + 1):
        if result[idx]:
            for fragment in fragments:
                try:
                    result[idx + fragment] = True
                except IndexError:
                    continue

    return [idx for idx, val in enumerate(result) if val]


def main():
    print(sieve_of_sums(100))


if __name__ == '__main__':
    main()
