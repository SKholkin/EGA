from initialization.init import launch_init
from utils import Averagemeter, get_argparser
from config import EGAConfig, create_config
from breed.breeding_from_population import breeding
from crossover.launcher import launch_crossover
from ordercoding import decode, encode
from mutation.laucher import launch_mutation
from selection.launcher import launch_selection
import numpy as np
import sys
import random


class EGA_state:
    def add(self, name_and_value):
        setattr(self, name_and_value[0], name_and_value[1])


class Criterio:
    def __init__(self, weight_matrix):
        self.weight_matrix = weight_matrix

    def __call__(self, vector, order_coding=True, *args, **kwargs):
        vector = vector.copy()
        output = 0
        if order_coding:
            vector = decode(vector)
        for i in range(len(vector) - 1):
            output += self.weight_matrix[vector[i]][vector[i + 1]]
        output += self.weight_matrix[vector[i + 1]][vector[0]]
        return 1 / output


def main_worker(config: EGAConfig):
    ega_state = EGA_state()
    criterio = Criterio(config.weight_matrix)
    # Генерация начальной популяции
    start_pop = launch_init(config)
    population = [encode(x) for x in start_pop]
    ega_state.add(('gen_overlap', config.get('gen_overlap', 0.5)))

    for i in range(config.get('max_iter', 10000)):
        ega_state.add(('pop_amount', len(population)))

        population = evolution_cycle(population, config, criterio, ega_state)
        #print(population)

        print(f'iter: {i}')
        ega_state.add(('max_criterio', 1 / criterio(max(population, key=criterio))))
        ega_state.add(('mean_criterio', sum([1 / criterio(vector) for vector in population]) / len(population)))
        mean_criterio_averagemetr.update(ega_state.mean_criterio)
        print(f'Минимальная длина пути: {ega_state.max_criterio}')
        print(f'Средняя длина пути по популяции: {ega_state.mean_criterio}')


def evolution_cycle(population, config, criterio, ega_state):
    # Воспроизводство
    to_breed = breeding(population, config, criterio)
    # Кроссовер
    descendants = launch_crossover(to_breed, config)
    # Мутация
    descendants = launch_mutation(descendants, config)
    elite_ones = []

    # Выбор части элитных особей
    if config.get('selection', {}).get('elite_ratio', None) is not None and config.get('selection', {}).get('elite_ratio', 0) * ega_state.pop_amount >= 1:
        inc_sorted_idx = np.argsort([criterio(vector) for vector in population])
        for i in range(1, int(config.get('selection', {}).get('elite_ratio', None) * ega_state.pop_amount + 1)):
            elite_ones.append(population[inc_sorted_idx[-i]])
        inc_sorted_idx = inc_sorted_idx[
                         0 - (int(config.get('selection', {}).get('elite_ratio', 0) * ega_state.pop_amount)):]
        population = [population[x] for x in range(len(population)) if x not in inc_sorted_idx]

    amount_of_out_desc = int(ega_state.gen_overlap * ega_state.pop_amount)
    amount_of_out_pop = int((1 - ega_state.gen_overlap) * ega_state.pop_amount) - len(elite_ones)
    final_desc = launch_selection(descendants, criterio, config, amount_of_out_desc)
    final_pop = launch_selection(population, criterio, config, amount_of_out_pop)

    return final_pop + final_desc + elite_ones


if __name__ == '__main__':
    parser = get_argparser()
    random.seed(10)
    np.random.seed(0)
    args = parser.parse_args(args=sys.argv[1:])
    mean_criterio_averagemetr = Averagemeter()
    config = create_config(args.config)
    main_worker(config)
