from collections import defaultdict

MAX_UNICODE = 0x10FFFF

unicode_bloats = defaultdict(dict)
for i in range(MAX_UNICODE):
    if len(chr(i)) != len(chr(i).lower()):
        unicode_bloats['lower'].update({i: chr(i)})
    if len(chr(i)) != len(chr(i).upper()):
        unicode_bloats['upper'].update({i: chr(i)})

print(f"{unicode_bloats['lower']}")
print(f"{unicode_bloats['upper']}")

# print(chr(0x10FFFF))
