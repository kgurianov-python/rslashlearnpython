"""
Builds the route on a rid based or directional instructions in for of
'N/n' for North, 'S/s' for South, 'E/e' for East, 'W/w' for West
"""
from typing import Collection

GRID_SIZE = 12



def get_next_pos(start: (int, int), direction: str, distance: int = 1) -> (int, int):
    """
    Generates a sinle new coordinate based on the starting psitina and a direction to move to
    in form of 'N/n' for North, 'S/s' for South, 'E/e' for East, 'W/w' for West

    :param start: Starting coordinates
    :type start: tuple(int, int)
    :param direction: a string containing a single character direction fo calculate next coordinate
    :type direction: str
    :param distance: distance to go in the direction with default set to 1 (for future development)
    :type distance: int
    :return: new coordinate
    :rtype: tuple(int, int)
    """
    pos_h, pos_v = start
    match direction.upper():
        case 'N':
            pos_v += distance
        case 'S':
            pos_v -= distance
        case 'E':
            pos_h += distance
        case 'W':
            pos_h -= distance
        case _:
            raise ValueError(f"Value [{direction}] is invalid direction")
    if (pos_v not in range(GRID_SIZE)) or (pos_h not in range(GRID_SIZE)):
        raise IndexError(f"Coordinates ({pos_v}, {pos_h}) are outside of the grid.")

    return pos_h, pos_v


def build_route(start: (int, int), route: Collection[str]) -> (int, int):
    """
    A generator to return a list of coordinates based on the route as a collection of directions

    :param start: Starting position
    :type start: tuple(int, int)
    :param route: A collection od directions, e.g. EeEEnNNNWwwWSssss
    :type route: Collection[str]
    """
    current_position = start
    yield current_position
    for step in route:
        current_position = get_next_pos(current_position, *step)
        yield current_position


def build_map(coords: [(int, int)],
              route_marker: str = '*') -> Collection[Collection[str]]:
    """
    Build the grid with the route plotted.

    :param coords: Coordinates to plot on map
    :type coords: list[tuple(int, int)]
    :param route_marker: A symbol to place on map to mark the route
    :type route_marker: str
    :return: printable grid with route
    :rtype: str
    """

    result = [['.'] * GRID_SIZE for _ in range(GRID_SIZE)]
    for pos_h, pos_v in coords:
        result[pos_v][pos_h] = route_marker
    return result


def print_grid_field(grid: Collection[Collection[str]],
                     joiner: str = '',
                     width: int = 4) -> str:
    """
    Generate the printable grid with the route plotted.
    :param grid: Te grid to transform
    :type grid: Collection[Collection[str]]
    :param joiner: a string to connect grid cells
    :type joiner: str
    :param width: a string to connect grid cells
    :type width: str
    :return: String with new line chars to separate grid rows
    :rtype: str
    """
    printable_grid = [[''] + [str(i) for i in range(GRID_SIZE)]]
    printable_grid.extend([[str(i)] + row for i, row in enumerate(grid)])

    return '\n'.join([joiner.join([cell.center(width) for cell in row]) for row in printable_grid[::-1]])


def main() -> None:
    """
    Just the executor
    """
    route = "nnnnnwnnnnneeeeeeeeeeessssssssswwwnnnwwwsswwnnnnnnee"
    start = (1, 0)
    coordinates = list(build_route(start, route))
    print(print_grid_field(build_map(coordinates)))
    print(*coordinates, sep='\n')


if __name__ == '__main__':
    main()
