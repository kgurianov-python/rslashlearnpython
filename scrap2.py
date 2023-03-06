


def main():
    def fill_row(x): return x * 2 - 1

    rows = int(input("Enter the number of rows: "))
    base = fill_row(rows)

    for num in range(rows, 0, -1):
        row_str = 'X' * fill_row(num)
        print(row_str.center(base))


main()
