import time


def timeitt(f):
    def whatever_we_want_to_return(*args, **kwargs):
        start = time.perf_counter()
        result = f(*args, **kwargs)
        delta = time.perf_counter() - start
        print(f"{f.__name__} executions time: {delta:.8f}")
        return result

    return whatever_we_want_to_return


@timeitt
def do_func(n):
    return [i for i in range(n)]


if __name__ == '__main__':
    res = do_func(1000000)
