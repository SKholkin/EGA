import numpy as np
import math
import random

# Одноточечный кроссовер
def single_point_crossover(parent1, parent2):
    separator = random.randint(1, len(parent1) - 1)
    return [parent1[:separator] + parent2[separator:]] + [parent2[:separator] + parent1[separator:]]

# Двуточечный кроссовер
def double_point_crossover(parent1, parent2):
    separators = list(np.random.randint(1, len(parent1) - 1, size=2))
    return [parent1[: separators[0]] + parent2[separators[0]:separators[1]] + [parent1[separators[1]:]]] + \
           [parent2[: separators[0]] + parent1[separators[0]:separators[1]] + [parent2[separators[1]:]]]

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
