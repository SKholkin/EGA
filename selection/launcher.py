from selection.algo_selection import proportional, ranking
from selection.algo_copy import roulette


def launch_selection(descendants, criterio, config, amount_of_out):
    if config.get('algorithm', None) == 'ranking':
        raise NotImplementedError("ranking selection algorithm isn't check yet")
    else:
        # ToDo: implement func choice
        prob_array = proportional(descendants, criterio)
    chosen_idx = roulette(prob_array, amount_of_out)
    output = [descendants[i] for i in chosen_idx]
    return output
