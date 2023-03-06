import random
from typing import Collection, Union

numeric = Union[int, float]

GRADE_RANK = {'B': 90, 'C': 80, 'D': 70, 'F': 60}


def get_avg(vals: Collection[int]) -> float:
    return sum(vals) / len(vals)


def get_grade(val: numeric) -> str:
    for grade, boundary in reversed(sorted(GRADE_RANK.items())):
        if val < boundary:
            return grade
    return 'A'

grades = random.sample(range(50, 101), 5)
print(grades)
for grade in grades:
    print(f"{grade} : {get_grade(grade)}")


print(get_avg(grades))

print(f"{get_grade(get_avg(grades))=}")
