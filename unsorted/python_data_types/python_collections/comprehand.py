index = 10
print(f"The {index}th element of a list comrehension '[i for i in range(0, 100, 5)]' is: {[i for i in range(0, 100, 5)][index]}")
print(f"The element with key {index} of a dictionary comrehension '{{i:i for i in range(0, 100, 5)}}' is: { {i: str(i) for i in range(0, 100, 5)}[index] }")

index = 10
print(f"The {index}th element of a generator 'tuple(i for i in range(0, 100, 5))' is: {tuple((i for i in range(0, 100, 5)))[index]}")