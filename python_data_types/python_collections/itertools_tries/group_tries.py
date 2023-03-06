import itertools

bytes = [1,2,3,4,6,8,10,5,7,2,2,2,2,2,2,2,2,2,3]
for key, group in itertools.groupby(bytes, lambda x: x % 2):
    print(key, list(group))