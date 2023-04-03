import random


def check_answer(value: int, user_response: int) -> str:
    delta = value - user_response
    if delta == 0:
        return f"You choice was: {user_response}. Right on point!"
    elif delta > 0:
        direction = "higher"  # if delta is positive, the user guess is lower, so user should try higher number
    else:
        direction = "lower"  # if delta is positive, the user guess is lower, so user should try higher number

    delta = abs(delta) // 10
    match delta:
        case 0:  # delta is less than 10
            result = f"You choice was: {user_response}. You are very close, go {direction}"
        case 1:  # delta is between 10 and 20
            result = f"You choice was: {user_response}. You are getting closer, go {direction}"
        case 2 | 3 | 4:
            result = f"You choice was: {user_response}. You are still quite far, go {direction}"
        case _:
            result = f"You choice was: {user_response}. Not even close, go {direction}"
    return result


VALUE = 80
for i in (0, 5, 10, 20, 30, 40, 50, 60):
    print(check_answer(VALUE, VALUE - i))
    print(check_answer(VALUE, VALUE + i))
