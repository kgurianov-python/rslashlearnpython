func = lambda x: x + 5

dict = {
    "operations": [
        {'id': "10", 'status': 'ACTIVE'},
        {'id': "20", 'status': 'INACTIVE'},
        {'id': "30", 'status': 'ACTIVE'},
        {'id': "40", 'status': 'INACTIVE'},
        {'id': "10", 'status': 'ACTIVE'},
    ]
}


def f(d): return d['status'] == 'ACTIVE'


res = filter(lambda d: d['status'] == 'ACTIVE', dict['operations'])
print(*res)
