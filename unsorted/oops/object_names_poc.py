class TestObject:
    field: str

    def __init__(self, field: str):
        self.field = field

    def __str__(self):
        return f'{self.field}'

    def __repr__(self):
        return self.__str__()


def main():

    object_var = TestObject('Unique String')
    another_object_var = object_var

    print(f'{object_var=}')
    print(f'{another_object_var=}')

    another_object_var.field='Another unique string after update'

    print(f'{object_var=}')
    print(f'{another_object_var=}')



if __name__ == '__main__':
    main()
