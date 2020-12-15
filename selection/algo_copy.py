import numpy as np


def roulette(prob_array, amount):
    chosen_idx = np.random.choice(len(prob_array), amount, p=prob_array, replace=False)
    return chosen_idx