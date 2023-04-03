keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]


test_dict = {key: value for key, value in zip(keys, values)}
print(test_dict)

print(*test_dict.items())
