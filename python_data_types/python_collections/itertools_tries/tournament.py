from python_data_types.python_collections import itertools_tries

players = ['player1', 'player2', 'player3', 'player4']


def main():
    # games = itertools.permutations(players, 2)
    games = itertools_tries.combinations(players, 2)
    for game in games:
        print(f'{game}')


if __name__ == '__main__':
    main()
