def condition(item):
    pass
    if item:
        print(item, end=' ')
        return False
    else:
        print(item, end='.')
        return True


x = 'Python'
y = tuple(reversed(x.partition('m')))

print(all(condition(z) for z in y))
