import random


def sort_list(list):
    if len(list) < 2:
        return list
    pivot = random.choice(list)
    less,equals,greater = [],[],[]
    for item in list:
        if item < pivot:
            less.append(item)
        elif item == pivot:
            equals.append(item)
        else:
            greater.append(item)
    return sort_list(less) + equals +sort_list(greater)