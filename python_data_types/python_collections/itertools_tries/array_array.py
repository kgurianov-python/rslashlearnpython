import dis

import numpy
import numpy as np


def exchange_indiv(pop1, pop2, prob):
    """
    Exchanges rows between two np arrays

    Parameters:
    pop1 : np array
    pop2: np array
    prob: int
        probability of exchange

    Returns:
    altered np arrays
    """

    assert len(pop1) == len(pop2)
    prob_array = np.random.binomial(1, prob, size=len(pop1))
    for i, p in enumerate(prob_array):
        if p:
            pop1[i], pop2[i] = pop2[i], pop1[i]
    return pop1, pop2


# x = np.array([list([1, 2, 3]) for i in range(4)])
# y = np.array([list([4, 5, 6]) for i in range(4)])
x = np.zeros(4, dtype=list)
y = np.zeros(4, dtype=list)
for i in range(4):
    x[i] = [1, 2, 3]
#
for i in range(4):
    y[i] = [4, 5, 6]


def swap(x, y):
    for i in range(4):
        print(f"{id(x[i])=}, {x[i]=}, {id(y[i])=} {y[i]=}")
        print(f"{id(x[i]) == id(y[i])=}")
        print(f"{x[i] == y[i]=}")
        print(f"{x[i] is y[i]=}")
        tmp = y[i]
        y[i] = x[i]
        x[i] = tmp
        print(f"{id(x[i])=}, {x[i]=}, {id(y[i])=} {y[i]=}\n")
    return x, y


# x, y = swap(x, y)

print(f"{x=}")
print(f"{y=}")

pop1, pop2 = exchange_indiv(x, y, 0.5)

print(f"{pop1=}")
print(f"{pop2=}")

