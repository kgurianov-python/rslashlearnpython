"""
https://www.reddit.com/r/learnpython/comments/11w27th/ask_anything_monday_weekly_thread/jd0lat2/?context=3

Hi, I’m working through the UoH python mooc and have reached the last exercise in part 5 and I’m a bit stumped

The question wants to take an input from the user that is the number of layers on a square that is output. The following outputs would be for 2, 3 and 4 as the input

BBB
BAB
BBB


CCCCC
CBBBC
CBABC
CBBBC
CCCCC


DDDDDDD
DCCCCCD
DCBBBCD
DCBABCD
DCBBBCD
DCCCCCD
DDDDDDD
"""

import string
from typing import Collection


def get_printable_maze(maze: list[list[str]]) -> str:
    return '\n'.join([''.join(row) for row in maze])


def build_maze(depth: int, filler: Collection[str] = string.ascii_uppercase) -> list[list[str]]:
    """Fill the top and bottom triangles", rotate the matrix ad to it again"""

    def fill_top_and_bottom():
        """Fill the top and bottom triangles"""
        for i in range(0, depth):
            result[maze_mid - i][maze_mid - i:maze_mid + i + 1] = filler[i] * (i * 2 + 1)
            result[maze_mid + i][maze_mid - i:maze_mid + i + 1] = filler[i] * (i * 2 + 1)

    maze_len = depth * 2 - 1
    maze_mid = (maze_len // 2)
    result = [[' '] * maze_len for _ in range(maze_len)]
    fill_top_and_bottom()

    result = list(map(list, zip(*result)))  # transpose first time
    fill_top_and_bottom()

    return result


if __name__ == '__main__':
    maze_size = 6
    print(*build_maze(maze_size), sep='\n')
    print(f"\nFilled with English ABC:\n{get_printable_maze(build_maze(maze_size))}")
    print(f"\nFilled with custom chars:\n{get_printable_maze(build_maze(maze_size, filler='*#$@*@#$'))}")
