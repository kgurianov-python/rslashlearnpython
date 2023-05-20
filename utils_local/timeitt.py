"""
Time counter decorator
"""
import logging
import time
# log_format = '%(name)s : %(levelname)s : %(asctime)s - %(message)s'
# # logging.basicConfig(level=logging.DEBUG, format=log_format)
logger = logging.getLogger('timeit')


def timeitt(runs: int = 100):
    def decorator(f):
        def wrapper(*args, **kwargs):
            stats = []
            for _ in range(runs):
                start = time.perf_counter()
                result = f(*args, **kwargs)
                end = time.perf_counter()
                stats.append(end - start)
            logger.debug(f"{f.__name__} | {runs} runs | AVG run time: {sum(stats) / runs:.8f}")
            return result

        return wrapper

    return decorator
