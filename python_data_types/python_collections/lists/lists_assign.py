import numpy as np

the_list = np.array([False] * 100)
indices = list(range(0, 100, 5))
print(indices)
the_list[indices] = True
print(the_list.tolist())
