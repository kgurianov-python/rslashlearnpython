def factorial(n: int) -> int:
    result = 1
    if 0 <= n < 2:
        return result

    for i in range(2, n+1):
        result *= i

    return result


print(factorial(10))
