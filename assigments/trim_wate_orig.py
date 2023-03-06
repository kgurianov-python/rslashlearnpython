import math


def main():
    # Asks user for input about the parameters of the box.
    # L should be = to 99 W should be equal to 7.2
    L = float(input("What is the length of the box in inches: "))

    W = float(input("What is the width of the box in inches: "))

    perimeter = 2 * L + 2 * W

    print("It appears, your box has a perimeter of :", perimeter)

    x = int(perimeter / 11.2)
    y = float(perimeter / 11.2)
    print("You will need to buy:", x, end=' trim boards')

    cost = round(x * 1.88, 2)
    print(" This will cost: $", cost)

    actual = 12 * x
    waste = actual - perimeter
    print(f"{waste}")

if __name__ == '__main__':
    main()