"""
https://www.reddit.com/r/learnpython/comments/12r2672/how_to_calculate_the_most_amount_of_overlap/

How to calculate the most amount of overlap between 2 or 3 lists?
Hi all,

I'm a beginner in python and I am using it to help answer a question about a hobby of mine. Basically, there are 15
deck lists in a collectible card game that I play (MTG). Each deck list has a list of cards that I've curated of only
cards that I am missing and need to buy.

What I want to do is calculate which combination of 2 or 3 decks provide the most overlap of cards (e.g. I need to
buy the LEAST amount of cards).

For example (using animals as an example instead of card names):

DeckA = ['cat,'dog','mouse']

DeckB = ['cat,'dog','mouse','gorilla']

DeckC = ['cat,'coyote','bear']

...

DeckZ = ['cat,'dolphin','tuna'] The code should look at the intersection of A and B, A and C, B and C, Z and A,
Z and B, etc...(all possible unique combinations between X number of lists) and calculate which combination of two
decks and three decks, provide for the MOST intersection (e.g. I would have to buy the least number of cards to get
the most decks operational).

Can someone help me with the logic/psuedo code/basic python of how to achieve this in python? I sat staring at my
screen for an hour and my brain hurts trying to figure out how to compute this in python.
"""
from typing import Collection


def get_min_dec(*args, expected: Collection = None) -> dict[str:Collection]:
    expected = set().union(*args) if expected is None else set(expected)

    def min_res(left, right):
        if len(left['remainder']) == len(right['remainder']):
            return min(left, right, key=lambda t: len(t['decks']))
        else:
            return min(left, right, key=lambda t: len(t['remainder']))

    # exit condition - we stop recursion when args list is exhausted or when the expected set length reaches 0
    if not args or (len(expected) <= 0):
        return {'decks': (), 'remainder': expected}

    curr_val = {'decks': args, 'remainder': expected}

    for idx, arg in enumerate(args):
        res = get_min_dec(*(args[:idx] + args[idx + 1:]), expected=set(expected) - set(arg))
        if len(res['remainder']) < len(expected):
            res['decks'] += arg,

        curr_val = min_res(curr_val, res)
    return curr_val


def test_result(*args, build_deck=None):
    res = get_min_dec(*args, expected=build_deck)
    print(f"\nBest decks to form {build_deck if build_deck is not None else 'all'} cards for target deck.")
    print(f"Calculated result: {res = }")
    if res['decks']:
        print("Decks list:")
        print(*res['decks'], sep="\n")


if __name__ == '__main__':
    deck_a = ['cat', 'dog', 'mouse', 'zebra']
    deck_b = ['cat', 'dog', 'mouse', 'gorilla']
    deck_c = ['cat', 'coyote', 'bear']
    deck_d = ['coyote', 'mouse', 'gorilla', 'zebra']

    test_result(deck_a, deck_b, deck_c, deck_d, build_deck=['koala', 'piggy'])

    test_result(deck_a, deck_b, deck_c, deck_d, build_deck=['cat', 'dog', 'mouse', 'gorilla', 'koala', 'piggy'])

    test_result(deck_a, deck_b, deck_c, deck_d, build_deck=['cat', 'dog', 'mouse', 'gorilla'])

    test_result(deck_a, deck_b, deck_c, deck_d, build_deck=['cat', 'coyote', 'gorilla'])

    test_result(deck_a, deck_b, deck_c, deck_d)
