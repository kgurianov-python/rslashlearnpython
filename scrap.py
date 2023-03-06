def valid_parentheses(test: str) -> (bool, int):
    test_stack = []
    pdict = {'(': ")", "[": "]", "{": "}", '<': '>'}
    counter = 0
    for candidate in test:
        counter += 1
        if candidate in pdict:
            test_stack.append(pdict[candidate])
        elif candidate in pdict.values() and (len(test_stack) == 0 or test_stack.pop() != candidate):
            return False, counter

    return len(test_stack) == 0, counter


print(f'{valid_parentheses("a (valid) string")=}')
print(f'{valid_parentheses("an (invalid) string(")=}')
print(f'{valid_parentheses("[a (valid) string]")=}')
print(f'{valid_parentheses("an ([invalid) string]")=}')
print(f'{valid_parentheses("]an invalid string")=}')
print(f'{valid_parentheses("[an (invalid]) string")=}')
print(f'{valid_parentheses("[a (valid)] string")=}')
print(f'{valid_parentheses("[((}{an  invalid)}]) string")=}')
print(f'{valid_parentheses("<valid/>")=}')
print(f'{valid_parentheses("(((invalid))")=}')
print(f'{valid_parentheses("((invalid)))")=}')
print(f'{valid_parentheses("([())invalid))])")=}')

