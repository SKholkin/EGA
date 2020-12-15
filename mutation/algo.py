import numpy as np
from ordercoding import upper_boundary


def saltation(descendant, gen_mutations):
    descendant = descendant.copy()
    to_mutate = np.sort(np.random.choice(len(descendant), size=gen_mutations, replace=False))
    for i in to_mutate:
        new_value = np.random.randint(upper_boundary(i, len(descendant)) + 1)
        descendant[i] = new_value
    return descendant
