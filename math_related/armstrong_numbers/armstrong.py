"""
https://www.reddit.com/r/learnpython/comments/11xajyr/need_help_with_a_question_from_a_model_exam/

Need help with a question from a model exam.

The question is: write a function sumcube(L) to test if an element from list L is equal to the sum of the cubes of its digits ie it is an "Armstrong Number". Print such numbers in the list. If L contains [67, 153, 311, 96, 370, 405, 371, 955, 407]. Then, the function should print [153, 370, 371, 407].

Here's my incorrect code which i wrote in the exam. I obviously spent some time on it before i came here for help.

L = [67, 153, 311, 96, 370, 405, 371, 955, 407]
def sumcube(L):
    A = []
    y = 0
    for i in L:
        for j in i:
            x = j ** j ** j
            y = y + x
            if y == i:
                A.append(y)
            else:
                continue
    print("The armstrong numbers are:", A)
sumcube(L)
My teacher did tell me that you can't iterate an integer so he told me to come with another solution.
"""

L = [67, 153, 311, 96, 370, 405, 371, 955, 407]


def split_digits(value: int) -> [int]:
    """Split the value into individual digits.
    - divmod() the value by 10 to receive the inegrer dicition result and the remainder
    - the remainder of the divmod() call will be the digit.
    - repeat until lat decimal (the divition result is zero)
    """
    result = []
    while value > 0:
        value, remainder = divmod(value, 10)
        result.append(remainder)
    return result


def is_armstrong(value: int) -> int:
    """Check if the number is an armstrong number
    - receive an array of digits from plit_digits() function,
    - use map() function to apply lambda to create a list of cubes from the list of digits
    - use sim() function to calculate the sum of cubes
    - compare the sum of cubes with the original value
    """
    return value == sum(map(lambda x: x ** 3, split_digits(value)))


if __name__ == '__main__':
    print(list(filter(is_armstrong, L)))
