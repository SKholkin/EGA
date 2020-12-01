import random
from common import hamming_distance
import numpy as np


# random mating/ stochastic mating
def panmixia(population, amount=None):
    population = np.array(population)
    if amount is None:
        amount = len(population) / 10
    return np.random.choice(population, amount)


# check is it working
def PosAssMating(population, criterio, amount=None):
    if amount is None:
        amount = int(len(population) / 10)
    criterio_array = [criterio[vector] for vector in population]
    sum_criterio = sum(criterio_array)
    prob_array = [iter_cr / sum_criterio for iter_cr in criterio_array]
    return np.random.choice(population, amount, prob_array)


# check is it working
def NegAssMating(population, criterio, amount=None):
    if amount is None:
        amount = int(len(population) / 10)
    pop_criterio_array = [criterio[vector] for vector in population]
    sum_criterio = sum(pop_criterio_array)
    high_prob_array = []
    for iter_criterio in pop_criterio_array:
        high_prob_array.append(iter_criterio / sum_criterio)

    low_pop_criterio_array = [1 / x for x in pop_criterio_array]
    sum_reverse_criterio = sum(low_pop_criterio_array)
    low_prob_array = []
    for iter_criterio_reverse in low_pop_criterio_array:
        low_pop_criterio_array.append(iter_criterio_reverse / sum_reverse_criterio)

    high_cr_half = np.random.choice(population, int(amount / 2), high_prob_array)
    low_cr_half = np.random.choice(population, int(amount / 2), low_prob_array)
    output = []
    for i in range(len(high_cr_half)):
        output.append(high_cr_half[i])
        output.append(low_cr_half[i])
    return np.array(output)


def inbreeding(population, amount=None, mode='k'):
    raise NotImplementedError('Inbreeding not implemeted')
    if mode == 'k':
        inbreeding_k(population, amount)
    elif mode == 'dual':
        inbreeding_dual(population, amount)
    else:
        raise AttributeError('Wrong inbreeding mode selection')


def inbreeding_k(population, amount):
    pass


def inbreeding_dual(population, amount):
    population = np.array(population)
    chosen = np.random.choice(population, int(amount / 2))
    mean = sum(population)
    for first_parent in chosen:
        pass