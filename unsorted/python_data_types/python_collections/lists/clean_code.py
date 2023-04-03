import random


def sort_list(values):
    if len(values) <= 1:
        return values
    pivot = random.choice(values)
    less, greater = [], []
    for item in values:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            greater.append(item)
    pivot_count = len(values) - (len(less) + len(greater))
    return sort_list(less) + [pivot] * pivot_count + sort_list(greater)


test = [5, 9, 3, 2, 2, 8, 8, 4, 1, 8, 1, 2, 3, 5, 6, 1, 8, 1]
print(sort_list(test))


