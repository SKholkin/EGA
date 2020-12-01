from initialization.common import is_already_chosen, calculate_total_dist, complete_roundabout, choose_first_city

def choose_neighbor(vector, weight_matrix):
    min_dist = 10000
    min_dist_index = -1
    for i in range(len(weight_matrix[0])):
        if not is_already_chosen(i, vector) and weight_matrix[vector[len(vector) - 1]][i] < min_dist:
            min_dist = weight_matrix[vector[len(vector) - 1]][i]
            min_dist_index = i
    print(f'Nearest neighbor: {min_dist_index}  Dist: {weight_matrix[vector[len(vector) - 1]][min_dist_index]}')
    return min_dist_index


def nearest_neighbor_method(weight_matrix):
    result = []
    choose_first_city(result, len(weight_matrix))
    for i in range(1, len(weight_matrix)):
        print(f'\niter: {i}')
        result.append(choose_neighbor(result, weight_matrix))
        print(f'Already visited: {result}\nCurrent Total Dist: {calculate_total_dist(result, weight_matrix)}')
    complete_roundabout(result)
    print(f'\nIn total\nRoute: {result}  Route length: {calculate_total_dist(result, weight_matrix)}')
    return result


#if __name__ == '__main__':
#    random.seed(5)
#    weight_matrix = create_weight_matrix(size=5, symmetric=True)
#    print_weight_matrix(weight_matrix)
#    result = nearest_neighbor_method(weight_matrix)
