"""
Time counter decorator
"""
import copy
import time


def timeitt(runs: int = 100):
    def decorator(f):
        def wrapper(*args, **kwargs):
            stats = []
            for _ in range(runs):
                data = copy.deepcopy(args[0])
                start = time.perf_counter()
                result = f(data, *args[1:], **kwargs)
                end = time.perf_counter()
                stats.append(end - start)
            print(f"{f.__name__} | {runs} runs | AVG run time: {sum(stats) / runs:.8f}")
            return result

        return wrapper

    return decorator
