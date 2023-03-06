EXITS = ['q', 'e', 'quit', 'exit']


def is_even(test: str):
    int_val = int(test)
    if int_val < 0:
        raise ValueError(f"Value must be positive. Provided value: '{test}'")
        return
    return not int_val % 2


def main():
    while (user_input := input(f"Please enter a positive number or {EXITS} to quit: ")).lower() not in EXITS:
        try:
            result = is_even(user_input)
            print(f"Value {user_input} is {'even' if result else 'odd'}")
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    main()
