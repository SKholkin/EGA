from initialization.algorithms.nearest_city import nearest_city_method
from initialization.algorithms.nearest_neighbor import nearest_neighbor_method
from initialization.algorithms.random_init import random_init_method
import random


def launch_init(config):
    if config.initialization.algorithm == 'nearest_city':
        return launch_by_alg(nearest_city_method, config.initialization.amount,
                             config.length, config.weight_matrix)
    elif config.initialization.algorithm == 'nearest_neighbor':
        return launch_by_alg(nearest_neighbor_method, config.initialization.amount,
                             config.length, config.weight_matrix)
    else:
        return launch_by_alg(random_init_method, config.initialization.amount,
                             config.length, config.weight_matrix)


def launch_by_alg(alg, amount, length, weight_matrix):
    first_cities = [i for i in range(length)]
    first_cities = random.sample(first_cities, len(first_cities))
    output = []
    for i in range(amount):
        try:
            if i < length and not alg == random_init_method:
                output.append(alg(weight_matrix, length=length, first_city=first_cities[i]))
            else:
                output.append(random_init_method(length))
        except:
            raise ValueError('Check algorithm you launch')
    return output
