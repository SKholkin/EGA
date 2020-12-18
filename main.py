from initialization.init import launch_init
from utils import create_weight_matrix, print_weight_matrix, prepare_logging, \
    configure_logging, Averagemeter, get_argparser, check_for_copies
from config import EGAConfig, create_config
from breed.breeding_from_population import breeding
from crossover.launcher import launch_crossover
from ordercoding import decode, encode
from mutation.laucher import launch_mutation
from selection.launcher import launch_selection
from scheduler import create_scheduler
import numpy as np
import sys
import random


class EGA_state:
    def add(self, name_and_value):
        setattr(self, name_and_value[0], name_and_value[1])


# ToDo: hash __call__ or maybe use an array of criterios along with population
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
        return 1 /  output


# ToDo: implement freeze of some aprt of codings at the end of evolution
#  (hypopheticaly should be more stable local minima)
#   also try to calculate time spendings on sorting or another parts of algo
def main_worker(config: EGAConfig):
    ega_state = EGA_state()
    criterio = Criterio(config.weight_matrix)
    scheduler = create_scheduler(ega_state, config)
    start_pop = launch_init(config)
    population = [encode(x) for x in start_pop]
    ega_state.add(('gen_overlap', config.get('gen_overlap', 0.5)))

    for i in range(config.get('max_iter', 10000)):
        ega_state.add(('pop_amount', len(population)))

        population = evolution_cycle(population, config, criterio, ega_state)

        print(f'iter: {i}')
        ega_state.add(('max_criterio', 1 / criterio(max(population, key=criterio))))
        ega_state.add(('mean_criterio', sum([1 / criterio(vector) for vector in population]) / len(population)))
        mean_criterio_averagemetr.update(ega_state.mean_criterio)
        tb_logger.add_scalar('max_criterio', ega_state.max_criterio, i)
        tb_logger.add_scalar('mean_criterio', mean_criterio_averagemetr.value, i)
        tb_logger.add_scalar('gen_overlap', ega_state.gen_overlap, i)
        print(f'Max criterio: {ega_state.max_criterio}')
        print(f'Mean criterio: {ega_state.mean_criterio}')
        print(f'Gen overlap: {ega_state.gen_overlap}')

        if config.get('scheduler', {}).get('mean_or_max', 'max') == 'mean':
            scheduler.step(mean_criterio_averagemetr.value)
        else:
            scheduler.step(ega_state.max_criterio)

        if ega_state.gen_overlap < 0.01:
            return


def evolution_cycle(population, config, criterio, ega_state):
    to_breed = breeding(population, config, criterio)
    descendants = launch_crossover(to_breed, config)
    # mutated individuals already fit in descendants
    descendants = launch_mutation(descendants, config)
    elite_ones = []

    if config.get('selection', {}).get('elite_ratio', None) is not None and config.get('selection', {}).get('elite_ratio', 0) * ega_state.pop_amount >= 1:
        # ToDo: maybe switch to more optimizated algo instead of full sorting
        inc_sorted_idx = np.argsort([criterio(vector) for vector in population])
        for i in range(1, int(config.get('selection', {}).get('elite_ratio', None) * ega_state.pop_amount + 1)):
            elite_ones.append(population[inc_sorted_idx[-i]])
        inc_sorted_idx = inc_sorted_idx[
                         0 - (int(config.get('selection', {}).get('elite_ratio', 0) * ega_state.pop_amount)):]
        population = [population[x] for x in range(len(population)) if x not in inc_sorted_idx]

    amount_of_out_desc = int(ega_state.gen_overlap * ega_state.pop_amount)
    amount_of_out_pop = int((1 - ega_state.gen_overlap) * ega_state.pop_amount) - len(elite_ones)
    if amount_of_out_desc > len(descendants):
        return descendants
    final_desc = launch_selection(descendants, criterio, config, amount_of_out_desc)
    final_pop = launch_selection(population, criterio, config, amount_of_out_pop)

    return final_pop + final_desc + elite_ones


if __name__ == '__main__':
    parser = get_argparser()
    random.seed(10)
    args = parser.parse_args(args=sys.argv[1:])
    tb_logger = configure_logging(args, log_dir=args.logdir)
    mean_criterio_averagemetr = Averagemeter()
    config = create_config(args.config)
    main_worker(config)
