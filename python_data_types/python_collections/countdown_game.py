import re


def check_solution(chosen: [int], target: int, operation: str) -> bool:
    if set([int(s) for s in re.findall(r'\b\d+\b', operation)]) - set(chosen):
        print('Wrong number used, please retry')
        return False
    try:
        if eval(operation) == target:
            print('Congrats !')
            return True
        else:
            print('Not quite, try again')
    except (NameError, SyntaxError) as e:
        print(f'{e}\nTry again...')
        return False

    return False


def main():
    numbig = int(input("How many big numbers do you want ? (0-4)\n"))
    big = [25, 50, 75, 100]
    small = list(range(1, 10)) * 2
    print(small)

    target = r.choice(range(100, 1000))
    chosen = r.sample(big, k=numbig) + r.sample(small, k=6 - numbig)  # Initialize the number list with the big ones

    print(chosen);
    print(target);  # Display the numbers and the target for the player

    while 1:
        try:
            operation = input('Provide your solition:\t')
            print(f'{operation=}')
            if operation == 'quit':
                break  # A non-system way to end the game
            if check_solution(chosen, target, operation):
                break
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
    # test = [100,7,3,2,3,1]
    # target = 900
    # solution = '100*3**2'
    # check_colution(test, target, solution)
