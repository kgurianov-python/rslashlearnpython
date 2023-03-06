from .constants import MAX_SIZE


def create_array(size: int = MAX_SIZE) -> list[int]:
    return [0] * size


def main():
    temp = create_array()
    print(f'{temp}')


if __name__ == '__main__':
    main()
