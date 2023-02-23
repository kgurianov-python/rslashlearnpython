def sort_list(list):
    if len(list) < 2:
        return list
    pivot = random.choice(list)
    less,equals,greater = [],[],[]
    for item in list:
        if item < pivot:
            minors.append(item)
        elif item == pivot:
            equals.append(item)
        else:
            older.append(item)
    return sort_list(smaller) + equals +sort_list(greater)