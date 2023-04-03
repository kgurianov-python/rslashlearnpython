try:
    raise ValueError('test')
except Exception as E:
    print(E)