import random
from python_data_types.python_collections import groupby

NUMBER_OF_EXPERIMENTS = 10000
DICE_SIDES = 10
ROLLS_PER_EXPERIMENT = 10
OUTPUT_RESULTS = 10


def rising_rolls(max_rolls: int = ROLLS_PER_EXPERIMENT, dice_sides: int = DICE_SIDES) -> list[int]:
    if ROLLS_PER_EXPERIMENT > DICE_SIDES:
        raise ValueError("We can not have more rising rolls than dice sides!")

    result = [last_roll := random.randint(1, dice_sides)]
    while last_roll < (last_roll := random.randint(1, dice_sides)) and (len(result) < max_rolls):
        result.append(last_roll)
    return result


def main():
    results = [rising_rolls() for _ in range(NUMBER_OF_EXPERIMENTS)]
    results.sort(key=len, reverse=True)

    results_stats = {k: list(g) for k, g in groupby(results, key=len)}
    stats_aggregated_str = (f"Number of raising rolls: {key}, Success count:{len(value)}" for key, value in
                            sorted(results_stats.items(), reverse=True))

    rolls_log_str = (f'Rolls: {log}, Count: {len(log)}' for log in results[:OUTPUT_RESULTS])

    print(f"Number of experiments: {NUMBER_OF_EXPERIMENTS}\n"
          f"Expected number of raising Rolls: {ROLLS_PER_EXPERIMENT}\n"
          f"Dice size: {DICE_SIDES}\n")

    print(*stats_aggregated_str, sep='\n')

    print(f'\nTop {OUTPUT_RESULTS} results:')
    print(*rolls_log_str, sep="\n")


if __name__ == '__main__':
    main()
