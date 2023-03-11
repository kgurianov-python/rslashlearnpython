"""
https://www.reddit.com/r/learnpython/comments/11malxp/coin_change_problem/
so we are doing a variation of the coin change problem, but insted of returning the number of possible ways, we want to return a list with all the possible changes.
the functino was needed to be generator.
for example

for x in change_gen(5,[1,2,3]): print(x)
[1,1,1,1,1]
[1,1,1,2]
[1,1,3]
[2,3]
"""
from typing import Any, Generator


def coin_change(coins: [int], target: int) -> Generator[list[int], Any, None]:
    if target < 0:
        return []
    if target == 0:
        return [[]]
    all_combos = []
    for idx, coin in enumerate(coins):
        for combination in coin_change(coins[idx:], target - coin):
            combination.append(coin)
            all_combos.append(combination)

    # yield all_combos
    # return all_combos
    return (one for one in all_combos)


combos = coin_change([1, 2, 3], 5)
print(f"{combos = }")
# print(next(combos))
print(*combos, sep='\n')


def change_gen_r(amount, coins):
    """
    this one is by https://www.reddit.com/user/pgpndw/
    """
    if amount != 0:
        for ind, coin in enumerate(coins):
            if amount >= coin:
                changes = change_gen_r(amount - coin, coins[ind:])
                for change in changes:
                    res = [coin] + change
                    yield res

    else:
        yield []


# Wrapper to ensure that the coins are
# unique and in descending order of value
def change_gen(amount, coins):
    yield from change_gen_r(amount, sorted(set(coins), reverse=True))


combos = change_gen_r(5, [1, 2, 3])
print(f"{combos = }")
print(*combos, sep='\n')
