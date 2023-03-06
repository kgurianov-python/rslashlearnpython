def pad_zero(in_string: str) -> str:
    values_list = in_string.split()
    padded_values = [f"{item:>02}" for item in values_list]
    return ' '.join(padded_values)


test = "1 11 12 13"
print(pad_zero(test))
test = "1 2 3 4 5 6 7 8 9 10 11 12 13"
print(pad_zero(test))
