upper_chars = 'loremtext'

test = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"

upped = ''.join([char.upper() if char in upper_chars else char for char in test])
print(upped)
