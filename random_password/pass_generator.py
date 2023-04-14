"""
https://twitter.com/RealBenjizo/status/1646857541664555008

Day 39: Password Generator

Create a function called generate_password that generates any
length of password for the user. The password should have a random
mix of uppercase letters, lowercase letters, numbers, and
punctuation symbols. The function should ask the user how strong
they want the password to be. The user should pick from weak,
strong, or very strong. If the user picks "weak," the function
should generate a 5-character long password. If the user picks
"strong," generate an 8-character password, and if they pick "very
strong," generate a 12-character password.
"""
import random
import string
from enum import Enum
from typing import Collection, Hashable

DEFAULT_REQUIREMENTS = [string.ascii_uppercase, string.ascii_lowercase, string.punctuation]


class Strength(Enum):
    WEAK = 5
    STRONG = 8
    VERY_STRONG = 12


def generate_password(strength: Strength, required: Collection[Hashable] = None) -> str:
    limits = {}
    if not required:
        required = DEFAULT_REQUIREMENTS.copy()

    # randomize the spread between required character sets, make sure each appears at least once
    while len(required) > 1:
        limits[required.pop()] = random.randint(1, strength.value - len(required) - sum(limits.values()))
    limits[required.pop()] = strength.value - sum(limits.values())

    # candidates = [random.choices(key, k=value) for key, value in limits.items()]
    password_array = [char for required_sample in [random.choices(key, k=value) for key, value in limits.items()] for
                      char in required_sample]
    random.shuffle(password_array)
    return "".join(password_array)


if __name__ == '__main__':
    print(f"{generate_password(Strength.WEAK) = }")
    print(f"{generate_password(Strength.STRONG) = }")
    print(f"{generate_password(Strength.VERY_STRONG) = }")
    required_chars = ['ABC-XYZ', '1', '&']
    print(f"{generate_password(Strength.WEAK, required_chars.copy()) = }")
    print(f"{generate_password(Strength.STRONG, required_chars.copy()) = }")
    print(f"{generate_password(Strength.VERY_STRONG, required_chars.copy()) = }")
