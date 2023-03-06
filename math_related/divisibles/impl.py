def filter_multiples(nums):
    result = []
    for num in nums:
        if (num % 3 != 0) and (num % 5 != 0) and (num % 8 != 0):
            result.append(num)

    return result


def clean_multiples(nums: list[int]):
    for num in nums[::-1]:
        if (num % 3 == 0) or (num % 5 == 0) or (num % 8 == 0):
            nums.remove(num)


def main():
    numbers = list(range(100))
    print(filter_multiples(numbers))
    clean_multiples(numbers)
    print(numbers)


if __name__ == '__main__':
    main()
