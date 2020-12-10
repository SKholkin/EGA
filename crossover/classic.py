import numpy as np
import math
import random


def single_point_crossover(parent1, parent2):
    separator = random.randint(1, len(parent1) - 1)
    return [parent1[:separator] + parent2[separator:]] + [parent2[:separator] + parent1[separator:]]


def double_point_crossover(parent1, parent2):
    separators = list(np.random.randint(1, len(parent1) - 1, size=2))
    return [parent1[: separators[0]] + parent2[separators[0]:separators[1]] + [parent1[separators[1]:]]] + \
           [parent2[: separators[0]] + parent1[separators[0]:separators[1]] + [parent2[separators[1]:]]]


# ToDo: check is it working if not well... OK
def n_point_crossover(parent1, parent2, n=1, output=1):
    separators = [0]
    separators += list(np.sort(np.random.randint(1, len(parent1) - 1, size=n)))
    separators += [len(parent1)]
    print(separators)
    if output > math.pow(2, n):
        raise AttributeError('Output value is bigger than possible! Please check output value')
    big_comb_list = add_to_gen([], separators, 0, parent1, parent2)
    combinations = []
    for i in range(0, math.pow(2, n)):
        combinations.append(big_comb_list[len(parent1) * i: len(parent1) * (i + 1)])
    sample = np.random.randint(0, math.pow(2, n), size=output)
    output = []
    for i in sample:
        output.append(combinations[i])
    return output


def add_to_gen(gen, separators, i, parent1, parent2):
    if i + 1 < len(separators):
        gen_1 = gen.copy()
        gen_2 = gen.copy()
        gen_1 += parent1[separators[i]:separators[i + 1]]
        gen_2 += parent2[separators[i]:separators[i + 1]]
        gen_output_1 = add_to_gen(gen_1, separators, i + 1, parent1, parent2)
        gen_output_2 = add_to_gen(gen_2, separators, i + 1, parent1, parent2)
        gen_output = gen_output_1 + gen_output_2
        return gen_output
    else:
        return gen


if __name__ == '__main__':
    parent1 = [3, 4, 1, 2, 1]
    parent2 = [2, 1, 3, 2, 1]
    n_point_crossover(parent1, parent2, n=1, output=2)
