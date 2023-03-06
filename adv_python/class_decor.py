from collections import defaultdict


def track_changes(original_class):
    original_class.attrs = defaultdict(str)
    orig_set_attr = original_class.__setattr__
    orig_del_attr = original_class.__delattr__

    def __setattr__(self, name, value):
        if self.attrs[name] == 'INIT':
            self.attrs[name] = 'MOD'
        else:
            self.attrs[name] = 'INIT'

        orig_set_attr(self, name, value)

    def __delattr__(self, name):
        self.attrs[name] = 'DEL'
        orig_del_attr(self, name)

    def get_all_changes(self):
        return self.attrs

    def get_changes(self, name):
        return self.attrs[name]

    original_class.__setattr__ = __setattr__
    original_class.__delattr__ = __delattr__
    original_class.get_changes = get_changes
    original_class.get_all_changes = get_all_changes
    return original_class


@track_changes
class TheTest:
    pass


the_test = TheTest()
the_test.name = "John"
the_test.lastname = "Doe"
the_test.address = "Milky way"
the_test.name = "Jake"

print(f"{the_test.get_changes('name_last')=}")
print(f"{the_test.get_changes('name')=}")
del the_test.lastname
print(f"{the_test.get_all_changes()=}")
