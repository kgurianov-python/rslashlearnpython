import pandas as pd

RANGES = [0, 2, 5, 10, 20, 30, 40]


def replace_with_range(val):
    if val <= RANGES[0]:
        return f"{RANGES[0]} and below"

    for i in range(1, len(RANGES)):
        if RANGES[i - 1] < val <= RANGES[i]:
            return f"{RANGES[i - 1]}-{RANGES[i]}"

    return f"{RANGES[-1]}+"


s = pd.DataFrame({"values": [-10, 0, 120, 30.4, 20.4, 30, 20, 120, 100, 10, 30, 10, 2, 1, 1, 45, 30]})
# values = set(s[0].tolist())
# for val in values:
#     s = s.replace(val, replace_with_range(val))

# print(s)

s['ranges'] = s.apply(lambda row: replace_with_range(row['values']), axis=1)

print(s)



