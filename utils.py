import random


def create_weigth_matrix_from_file(path):
    matr = []
    with open(path, 'r') as w_matr_file:
        length = w_matr_file.readline().split()[0]
        matr_lines = w_matr_file.readlines()
        for i in range(len(matr_lines)):
            line = []
            for j in range(len(matr_lines[i].split())):
                if matr_lines[i].split()[j].isdigit():
                    line.append(int(matr_lines[i].split()[j]))
            matr.append(line)
    return matr


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
        for i in range(size):
            w_matr[i][i] = 0
    return w_matr


def print_weight_matrix(weight_matrix):
    print('Weight Matrix')
    for i in range(len(weight_matrix)):
        print(weight_matrix[i])


def write_matr_into_file(matr, filename):
    with open(filename, 'w+') as file:
        file.write(str(len(matr)))
        for i in range(len(matr)):
            file.write('\n')
            for j in range(len(matr)):
                file.write(str(matr[i][j]) + ' ')


# maybe do separate util for creation weight matrices
# for launching from console
# if __name__ == '__main__':
#    length = 10
#    matr = create_weight_matrix(15, max_weight=20)
#    write_matr_into_file(matr, 'configs/15len_matr.txt')
#    matr = create_weigth_matrix_from_file('configs/15len_matr.txt')
#    pass