##### import libraries #####
import numpy as np

##### Variables #####
chain_list = []  # Holds the length and grade values


def get_variables():
    ln = int(input('Length of chain (48in, 60in, 72in): '))  # length of chain
    gr = str(input('Grade of chain (80 or 100 steel): '))  # Grade of chain
    chain_list.append([ln, gr])


def matrix():  # Solves the system of linear equations
    a = np.array([[-0.231, 0.2857, 0], [-0.308, -0.429, 0.3846], [-0.923, -0.857, -0.923]])
    b = np.array([[0], [0], [-270]])

    c = np.dot(np.linalg.inv(a), b)
    print(c)


def start():
    full = ''
    while full != 'y':
        get_variables()
        full = str(input('Are you finished adding chain values? (y/n): '))
        print(chain_list)
    for x in chain_list:
        h = x[0]
    print(h)


def main():
    start()


if __name__ == '__main__':
    main()
