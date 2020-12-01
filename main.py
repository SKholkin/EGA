import numpy as np


class Criterio:
    def __init__(self, route_matr):
        self.route_matr = route_matr

    def __call__(self, vector, *args, **kwargs):
        vector = list(vector)
        output = 0
        for i in range(len(vector) - 1):
            output += self.route_matr[vector[i], vector[i + 1]]
        output += self.route_matr[vector[i + 1], vector[0]]
        return output


def main_worker():
    # initializtion(start population)
    # cycle part begin
    # make some pretendents (reproduction/breeding)
    # mutations
    #
    pass


def evolution_cycle(popualtion, max_iter=1000):
    amount = int(len(popualtion) / 100)
    for i in range(max_iter):
        to_breed = choose_parents(population, amount)
        pretendents = breed(to_breed)
    pass


if __name__ == '__main__':
    pass
