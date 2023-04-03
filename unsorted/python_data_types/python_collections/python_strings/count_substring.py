superstring = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
superstring = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
substring = "the"


def count_substring(super: str, sub: str) -> int:
    idx = 0
    count = 0
    while idx < len(super) - len(sub):
        if super[idx:idx + len(sub)] == sub:
            count += 1
        idx += 1
    return count

# superstring = "bobobobobobo"
substring = "text"

print(count_substring(superstring, substring))


print(*(superstring[i:] for i in range(len(substring))), sep='\n')

print(*zip(*(superstring[i:] for i in range(len(substring)))), sep='\n')

print(*(''.join(candidate) for candidate in zip(*(superstring[i:] for i in range(len(substring))))), sep='\n')