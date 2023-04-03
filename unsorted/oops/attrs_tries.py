import attr


class no_attrs:
    a: int = 0
    b: str = ''
    c: list[int] = []


@attr.s
class with_attrs:
    a: int = 0
    b: str = ''
    c: list[int] = []


print(*list(dir(no_attrs)), sep='\n')
print(*list(dir(with_attrs)), sep='\n')
