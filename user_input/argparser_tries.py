import argparse

DEFAULT_FIBO_NUMBER = 10


def fibonacci(idx: int) -> int:
    """ A very simple fibonacci """
    result = [0, 1]
    if idx < 2:
        return result[idx]
    for _ in range(2, idx + 1):
        result = result[1], result[1] + result[0]
    return result[1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--all-trams', '-at', action='store_true')
    group.add_argument('--stops', '-s', action='store_true')
    group.add_argument('--disruptions', '-dis', action='store_true')
    group.add_argument('--directions', '-dir', action='store_true')

    another_group = parser.add_mutually_exclusive_group()
    another_group.add_argument('--route', '-r', type=int)
    another_group.add_argument('--all-trams', '-at', action='store_true')

    args = parser.parse_args()
    print(parser.parse_args())
    print(fibonacci(int(args.number)))
