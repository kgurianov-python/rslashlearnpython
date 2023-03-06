def throw_something(val: int) -> None:
    if val < 10:
        raise ValueError
    elif val < 100:
        raise ValueError("Value too low")
    else:
        return


try:
    throw_something(99)
except ValueError as e:
    raise

# throw_something(99)
