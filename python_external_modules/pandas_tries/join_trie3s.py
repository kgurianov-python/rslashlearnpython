import pandas as pd

prices = [20, 10, 30]
items = ['red', "green", "blue"]
price_info = pd.DataFrame(list(zip(items, prices)), columns=['Name', 'Price']).set_index('Name')

quantities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bom_parts = ['red', "green", "blue", 'red', "green", "blue", 'red', "green", "blue"]
bom = pd.DataFrame(list(zip(bom_parts, quantities)), columns=['Name', 'Quantity'])
print(bom)
