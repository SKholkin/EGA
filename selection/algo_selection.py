from selection.helper import Linear
from utils import print_weight_matrix
from ordercoding import decode

# input: descendats
# output: prob array

# Пропорциональная схема селекции
def proportional(descendats, criterio, func=None):
    sum_criterio = sum(criterio(vector) for vector in descendats)
    prob_array = []
    for desc in descendats:
        prob_array.append(criterio(desc) / sum_criterio)
    return prob_array


def ranking(descendtans, criterio, n_plus=None, n_minus=None):
    if n_plus is None or n_minus is None:
        n_minus = 0
        n_plus = len(descendtans) / 10
    linear = Linear(n_plus - n_minus, n_minus)
    sorted_desc = sorted(descendtans, key=lambda x: criterio(x))
    prob_array = []
    # n_k = (n_plus - n_minus) * i / (len(descendtans))
    # p_k = n_k / len(descendtans)
    for i in range(len(sorted_desc)):
        prob_array.append(linear(i) / len(descendtans))
    return prob_array
