import operator

items = [('1937', 'Technetium'), ('1907', 'Lutetium'), ('1923', 'Hafnium'), ('1925', 'Rhenium'), ('1940', 'Astatine'),
         ('1939', 'Francium'), ('1913', 'Protactinium'), ('1940', 'Neptunium'), ('1940', 'Plutonium')]


items.sort()
# s = sorted(s, key = operator.itemgetter(1, 2))
print(*items, sep='\n')