import numpy as np


def breeding(population, config, criterio):
    result = panmixia(population, config.breeding.get('ratio', None) * len(population))
    result = list(result)
    return [list(i) for i in result]


def panmixia(population, amount=None):
    population = np.array(population)
    if amount is None:
        amount = len(population) / 10
    return random_choice(population, amount)


def random_choice(population, amount, prob_array=None):
    if prob_array is None:
        prob_array = [1 / len(population) for i in range(len(population))]
    mapping_array = np.arange(len(population))
    result = []
    mapping_array = np.random.choice(mapping_array, size=int(amount), p=prob_array, replace=False)
    for i in mapping_array:
        result.append(population[i])
    return result
