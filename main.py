from initialization.init import launch_init
from utils import create_weight_matrix, print_weight_matrix
from config import EGAConfig
from breed.selection_from_population import selection


# TODO: test this
class Criterio:
    def __init__(self, weight_matrix):
        self.weight_matrix = weight_matrix

    def __call__(self, vector, *args, **kwargs):
        vector = list(vector)
        output = 0
        for i in range(len(vector) - 1):
            output += self.weight_matrix[vector[i], vector[i + 1]]
        output += self.weight_matrix[vector[i + 1], vector[0]]
        return output


def main_worker(config: EGAConfig):
    criterio = Criterio(config.weight_matrix)
    start_pop = launch_init(config)
    population = start_pop
    next_gen_pretendents = selection(population, criterio, config)
    # initializtion(start population)
    # cycle part begin
    # make some pretendents (reproduction/breeding)
    # mutations
    #
    pass


# def evolution_cycle(popualtion, max_iter=1000):
#    amount = int(len(popualtion) / 100)
#    for i in range(max_iter):
#        to_breed = choose_parents(population, amount)
#        pretendents = breed(to_breed)
#    pass


if __name__ == '__main__':
    config = EGAConfig()
    config.length = 10
    config.weight_matrix = create_weight_matrix(config.length, max_weight=20, symmetric=True)
    config.initialization.algorithm = 'random'
    config.initialization.amount = 15
    main_worker(config)
