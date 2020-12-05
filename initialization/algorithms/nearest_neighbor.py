from initialization.common import is_already_chosen, calculate_total_dist, complete_roundabout, choose_first_city


def choose_neighbor(vector, weight_matrix):
    min_dist = 10000
    min_dist_index = -1
    for i in range(len(weight_matrix[0])):
        if not is_already_chosen(i, vector) and weight_matrix[vector[len(vector) - 1]][i] < min_dist:
            min_dist = weight_matrix[vector[len(vector) - 1]][i]
            min_dist_index = i
    return min_dist_index


def nearest_neighbor_method(weight_matrix, length=None, first_city=None, verbose=False):
    if length is None:
        length = len(weight_matrix)
    result = []
    if first_city is None:
        choose_first_city(result, length)
    else:
        result.append(first_city)
    for i in range(1, length):
        if verbose:
            print(f'\niter: {i}')
        result.append(choose_neighbor(result, weight_matrix))
    complete_roundabout(result)
    if verbose:
        print(f'\nIn total\nRoute: {result}  Route length: {calculate_total_dist(result, weight_matrix)}')
    return result
