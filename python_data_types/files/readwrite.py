import re
in_file_name = 'input.txt'
out_file_name = 'output.txt'

with open(in_file_name, "r") as in_file:
    with open(out_file_name, "w") as out_file:
        lines_counter = 0
        for line in in_file:
            out_file.write(f'{lines_counter:03} {line.replace(" ", "-")}')
            lines_counter += 1


# for convenience, we create a collection of character we want to count
# the collection can be expanded to add/exlude additional characters
characters = ('e', 'g')
chars_all_regex = f'[{"".join(characters)}]'  # resulted regexp is [eg]

# create a dictionary with keys from chars collecton with initial value set to 0
counters = dict.fromkeys(characters, 0)
counter_all_map = 0
counter_all_regexp = 0

with open(in_file_name, "r") as in_file:
    for line in in_file:
        for character in characters:
            # convert the scanned line to lowercase, and count the chars in a line
            # the add the count to the dictionary
            counters[character] += line.lower().count(character)

        # Instead of a for-loop, feed the count function to map
        counter_all_map += sum(map(line.lower().count, characters))

        # Using regex to search ignoring characters case
        counter_all_regexp += len(re.findall(chars_all_regex, line, re.IGNORECASE))

print(f'By letter: {counters}, Sum: {sum(counters.values())}')
print(f'Count using map: {counter_all_map}')
print(f'Count using regexp: {counter_all_regexp}')