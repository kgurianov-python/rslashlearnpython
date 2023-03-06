import string
from collections import deque

tests = ["A nut for a jar of tuna",
         "Was it a car or a cat I saw",
         "Hannah",
         "Step on no pets",
         "Not a palindrome"]


def do_test_palindrome(value: str) -> (bool, int):
    test_deque = deque(remove_non_letters(value))
    length = len(test_deque)
    while len(test_deque) > 1:
        if test_deque.popleft() != test_deque.pop():
            return False, length
    return True, length


def remove_non_letters(value: str) -> list[str]:
    return [c for c in value.lower() if c in string.ascii_lowercase]


for test in tests:
    result, str_len = do_test_palindrome(test)
    print(f"\nPalindrome candidate length is : {str_len}")
    print(f"\"{test}\" is {'' if result else 'not '}a palindrome")
