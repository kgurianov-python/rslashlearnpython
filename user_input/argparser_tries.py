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
    usage = " -n <number> - Fibonacci number"
    parser = argparse.ArgumentParser('Test', usage, 'Accepts argument when called from CLI')
    parser.add_argument('-n', '--number', required=True)
    args = parser.parse_args()
    print(fibonacci(int(args.number)))
