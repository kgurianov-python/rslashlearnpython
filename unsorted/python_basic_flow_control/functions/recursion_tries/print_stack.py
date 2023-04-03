import traceback


def countdown(value: int) -> None:
    if value <= 0:
        raise Exception("reached the bottom")
    print(value)
    countdown(value - 1)


def main():
    try:
        countdown(3)
    except Exception as ex:
        tb = traceback.TracebackException.from_exception(ex, capture_locals=True)
        print("".join(tb.format()))


if __name__ == '__main__':
    main()
