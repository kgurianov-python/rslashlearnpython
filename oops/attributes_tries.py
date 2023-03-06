class P:
    value: int = 4

p = P()
p.value = 5

print(f"{p.value}")
print("value" in vars(p))  # True
print(f"{vars(p)=}")