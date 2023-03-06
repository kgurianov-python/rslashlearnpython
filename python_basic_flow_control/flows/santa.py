def main():
    houses = [[0, 0]]
    santa_x, santa_y = houses[0]
    directions = "<<>>^>A^v<^vvv^^^<^><<>^^<^<^<vvvv>>><<"
    print(f'Total directions: {len(directions)}')
    for direction in directions:
        match direction:
            case '^':
                santa_y += 1
            case '>':
                santa_x += 1
            case '<':
                santa_x -= 1
            case 'v':
                santa_y -= 1
            case _:
                print('Incorrect direction')
                continue

        santa_location = [santa_x, santa_y]
        if santa_location not in houses:
            houses.append(santa_location)

        print(f'Move: [{direction}]\nVisited: {houses=}')

    print(len(houses))


if __name__ == '__main__':
    main()
