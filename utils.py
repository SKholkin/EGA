import random


def create_weight_matrix(size, max_weight=10, symmetric=True):
    w_matr = []
    if not symmetric:
        for i in range(size):
            w_matr.append([])
            for j in range(size):
                w_matr[i].append(random.randrange(1, max_weight))
    else:
        for i in range(size):
            w_matr.append([])
            for j in range(size):
                w_matr[i].append(-1)
        for i in range(size):
            for j in range(size):
                if w_matr[i][j] <= 0:
                    w_matr[i][j] = w_matr[j][i] = random.randrange(1, max_weight)
    return w_matr


def print_weight_matrix(weight_matrix):
    print('Weight Matrix')
    for i in range(len(weight_matrix)):
        print(weight_matrix[i])

