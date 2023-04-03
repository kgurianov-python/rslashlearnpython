from itertools import product, combinations, zip_longest

arr1 = [3, 5, 6, 15, 19, 21]
arr2 = [1, 2, 7, 8, 11, 12, 17, 18, 20]


def merge(list1, list2):
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    return result + list1[i:] + list2[j:]


print(merge(arr1, arr2))

print(f"{list(product(arr1, arr2))=}")
print({min(x, y) for x, y in product(arr1, arr2)})

print(f"{list(zip_longest(arr1, arr2))=}")
