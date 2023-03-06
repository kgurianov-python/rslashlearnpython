import time


def timeitt(runs: int = 10):
    def decorator(f):
        def wrapper(*args, **kwargs):
            stats = []
            for _ in range(runs):
                start = time.perf_counter()
                result = f(*args, **kwargs)
                stats.append(time.perf_counter() - start)

            print(f"{f.__name__} Runs: {runs}; average executions time: {sum(stats) / runs:.8f}")
            return result

        return wrapper

    return decorator


@timeitt(runs=1)
def do_find(secret: str, guess: str) -> (int, int):
    cows, bulls = 0, 0

    for idx, char in enumerate(guess):
        is_bull = False
        secret_index = 0
        while secret_index < len(secret) and secret_index >= 0:
            secret_index = secret.find(char, secret_index)
            if secret_index < 0:
                break
            print(secret_index)
            if idx == secret_index:
                is_bull = True

        if is_bull:
            bulls += 1
        else:
            cows += 1
    return cows, bulls


@timeitt()
def do_bruteforce(secret: str, guess: str) -> (int, int):
    cows, bulls = 0, 0
    for g_idx, g_char in enumerate(guess):
        for s_idx, s_char in enumerate(secret):
            if g_char == s_char:
                if g_idx == s_idx:
                    bulls += 1
                else:
                    cows += 1
    return cows, bulls


secret = 'terraform'
guess = 'terra'

print(do_bruteforce(secret, guess))
print(do_find(secret, guess))
