def logical_example(a: int):
    result: str = None
    if a == 2:
        result = 'even'
    elif a == 1:
        next
    elif a == 3:
        result = 'odd'

    return result


if __name__ == '__main__':
    a = input(f'Please enter a number or \'q\' to quit')
    while a != 'q':
        print(f'The result for {int(a)} in {logical_example(int(a))}')
        a = input(f'Please enter a number or \'q\' to quit')
