import itertools
from typing import Collection


def matrixTranspose(L):
    m = len(L)
    n = len(L[0])
    transpose = [[0] * m] * n
    i = 0
    while i < m:
        j = 0
        while (j < n):
            element = L[i][j]
            print(element)
            transpose[j][i] = element
            j = j + 1
        print(transpose)
        i = i + 1

    return transpose


def do_transpose(arr: Collection[Collection[int]]) -> Collection[Collection[int]]:
    return [[row[i] if i < len(row) else None for row in arr] for i in range(len(max(arr, key=len)))]


matrixTranspose([[3, 10, 5], [2, 4, 11]])

print(*do_transpose([[3, 10, 5], [2, 4, 11]]), sep='\n')

print(*itertools.zip_longest(*[[3, 10, 5], [2, 4, 11], [2, 4, 55, 100]]), sep='\n')
