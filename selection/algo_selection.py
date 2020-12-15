from selection.helper import Linear
from utils import print_weight_matrix
from ordercoding import decode

# input: descendats
# output: prob array

def proportional(descendats, criterio, func=None):
    if func is None:
        func = Linear(1, 0)
    sum_criterio = sum(func(criterio(vector)) for vector in descendats)
    prob_array = []
    for desc in descendats:
        prob_array.append(func(criterio(desc)) / sum_criterio)
    return prob_array


# ToDo: check is it working
def ranking(descendtans, criterio, n_plus=None, n_minus=None):
    if n_plus is None or n_minus is None:
        n_minus = 0
        n_plus = len(descendtans) / 10
    linear = Linear(n_plus - n_minus, n_minus)
    sorted_desc = sorted(descendtans, key=lambda x: criterio(x))
    prob_array = []
    for i in range(len(sorted_desc)):
        prob_array.append(linear(i) / len(descendtans))
    return prob_array