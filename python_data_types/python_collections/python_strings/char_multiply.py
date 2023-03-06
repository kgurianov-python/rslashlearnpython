def vertical_strings(string):
    """takes a string and prints each letter on new line repeating each letter for length of index+1"""
    for idx, char in enumerate(string, 1):
        print(char * idx)


vertical_strings('hello')
