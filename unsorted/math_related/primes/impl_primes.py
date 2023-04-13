import itertools
import time
from functools import lru_cache

from utils_local.timeitt import timeitt


@timeitt(1)
# @lru_cache
def get_primes(bound: int) -> list[int]:
    candidates = [False, False] + ([True] * (bound - 1))
    for idx, candidate in enumerate(candidates):
        if candidate:
            for i in range(idx * 2, len(candidates), idx):
                candidates[i] = False
    return [idx for idx, candidate in enumerate(candidates) if candidate]


@timeitt(1)
def get_from_gen(count: int) -> list[int]:
    gen = gen_primes()
    return [next(gen) for _ in range(count)]


def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.

    composites = {}

    candidate = 2

    while True:
        # if (candidate % 2 == 0) or (candidate in composites):
        if candidate not in composites:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield candidate
            composites[candidate * candidate] = [candidate]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in composites[candidate]:
                composites.setdefault(p + candidate, []).append(p)
            del composites[candidate]

        candidate += 1


if __name__ == '__main__':
    primes = get_primes(1_000_000)
    print(len(primes))
    print(primes[-1])

    primes_from_gen = get_from_gen(78498)
    print(len(primes_from_gen))
    print(primes_from_gen[-1])
