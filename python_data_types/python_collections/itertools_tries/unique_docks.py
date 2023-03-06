import random
from itertools import product
from typing import Collection


# Config
# doc = f'[NOUN-1] [VERB-1] [NOUN-2].'

NAMES = [
    "Adam", "Bryan", "Caroline", "David", "Ethan", "Frank",
    "Gary", "Harvey", "Ian", "Julian", "Kevin", "Liam",
    "Michael", "Nathan", "Oscar", "Paul", "Quincy", "Ryan",
    "Steven", "Thomas", "Uriah", "Vincent", "Will"
]

VERBS = [
    "greeted", "kicked", "punched", "talked to"
]


def get_actions(name_pairs: Collection, verbs: Collection) -> product:
    return product(name_pairs, verbs)


def get_actions_formatted(actions: Collection) -> list[str]:
    return [f'{action[0][0]} {action[1]} {action[0][1]}' for action in actions]


def print_actions(name_pairs):
    # print(f"{len(list(name_pairs))}")
    actions = get_actions(name_pairs, VERBS)
    print(*actions, sep='\n')
    actions_formatted = list(get_actions_formatted(actions))
    print(f"\n{len(actions_formatted)=}")
    print(*random.sample(actions_formatted, 10), sep='\n')


def main():
    name_pairs_coms = itertools_tries.combinations(NAMES, 2)
    print_actions(name_pairs_coms)

    name_pairs_perms = itertools_tries.permutations(NAMES, 2)
    print_actions(name_pairs_perms)


if __name__ == '__main__':
    main()
