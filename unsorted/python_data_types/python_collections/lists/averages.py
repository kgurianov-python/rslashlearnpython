from statistics import mean

test = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

test = [int(item) for item in test]
print(mean(test))

sum = 0
counter = 0
for item in test:
    sum += item
    counter += 1

print(f"{counter=}")
print(sum/counter)
print(mean(test))


total = 0
for idx, height in enumerate(test, start=1):
    total += int(height)
average = total / idx

print(average)