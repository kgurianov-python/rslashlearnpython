import random

binary = (0, 1)
rando_size = 4
max_value = rando_size * max(binary)

rando = random.choices(binary, k=rando_size)


def roll(rando):
    state = sum(rando)
    if state == 0:
        return rando, "All negative!"
    elif state == max_value:
        return rando, "All positive!"
    else:
        return rando, f"{state} positive, {rando_size - state} negative"


print(*roll(rando))
