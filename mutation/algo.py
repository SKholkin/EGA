import numpy as np
from ordercoding import upper_boundary

# Сальтация (gen_mutations=1 точечная метация)
def saltation(descendant, gen_mutations):
    descendant = descendant.copy()
    # случайная генерация с повтором
    to_mutate = np.sort(np.random.choice(len(descendant), size=gen_mutations, replace=False))
    for i in to_mutate:
        new_value = np.random.randint(upper_boundary(i, len(descendant)) + 1)
        descendant[i] = new_value
    return descendant
