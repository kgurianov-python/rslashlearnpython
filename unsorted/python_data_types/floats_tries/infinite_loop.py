def main():
    val = 0.50
    while val != 0:
        coin = float(input("Insert coin:\t"))
        val -= coin
        print(val)


if __name__ == '__main__':
    main()
