from initialization.init import launch_init
from utils import create_weight_matrix, print_weight_matrix
from config import EGAConfig, create_config
from breed.selection_from_population import selection
from crossover.launcher import launch_crossover
from ordercoding import decode, encode


# TODO: test this
class Criterio:
    def __init__(self, weight_matrix):
        self.weight_matrix = weight_matrix

    def __call__(self, vector, *args, **kwargs):
        vector = list(vector)
        output = 0
        for i in range(len(vector) - 1):
            output += self.weight_matrix[vector[i]][vector[i + 1]]
        output += self.weight_matrix[vector[i + 1]][vector[0]]
        return output


def main_worker(config: EGAConfig):
    criterio = Criterio(config.weight_matrix)
    start_pop = launch_init(config)
    population = [encode(x) for x in start_pop]

    print(population)
    next_gen_parents = selection(population, config, criterio)
    # initializtion(start population)
    # cycle part begin
    # make some pretendents (reproduction/breeding)
    # mutations
    #
    pass


def evolution_cycle(popualtion, config, criterio, max_iter=1000):
    for i in range(max_iter):
        to_breed = selection(popualtion, config, criterio)
        descendants = launch_crossover(to_breed, config)
        # mutation
        # get mutated descendatns
    pass


if __name__ == '__main__':
    config = create_config('configs/base_config.json')
    main_worker(config)
