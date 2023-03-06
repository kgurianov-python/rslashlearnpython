'''
· You have a box that has a length and width in inches. These lengths and widths are not restricted to be in whole numbers (e.g, the length could be 11.2 inches)

· You want to put trim around the box, but the local hardware store only sells trim in 12” segments.

· A 12” segment of trim costs $1.88. "

Calculates the cost of the trim

Calculate the amount of $$ you lost because you could not buy the trim in increments other than 12” segments
'''

TRIM_SHIP_UNIT_SIZE_INCHES = 12
TRIM_PRICE_PER_UNIT_USD = 1.88


def main():
    box_length = float(input(f'Box length: '))
    box_width = float(input(f'Box width: '))

    box_perimetr = (box_length + box_width) * 2

    trim_whole_units, remainder = divmod(box_perimetr, TRIM_SHIP_UNIT_SIZE_INCHES)

    trim_units_to_buy = int(trim_whole_units + (1 if int(remainder) > 0 else 0))
    trim_cost = trim_units_to_buy * TRIM_PRICE_PER_UNIT_USD

    trim_waste = trim_units_to_buy * TRIM_SHIP_UNIT_SIZE_INCHES - box_perimetr
    trim_waste_cost = (trim_waste / TRIM_SHIP_UNIT_SIZE_INCHES) * TRIM_PRICE_PER_UNIT_USD

    print(f'With length of {box_length}" and width of {box_width}", the box perimetr is: {box_perimetr:.2f}"')

    print(f"You will need to buy {trim_units_to_buy} trim {'segments' if trim_units_to_buy > 1 else 'segment'}")
    print(f"At a price of ${TRIM_PRICE_PER_UNIT_USD} per {TRIM_SHIP_UNIT_SIZE_INCHES}\" it will cost you ${trim_cost:.2f}")

    print(f"With {round(trim_waste, 2)}\" of trim wasted, the waste cost is ${round(trim_waste_cost, 2)}")


if __name__ == '__main__':
    main()
