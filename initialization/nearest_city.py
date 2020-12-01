from initialization.common import is_already_chosen, choose_first_city, complete_roundabout, calculate_total_dist, find_index_by_city


def find_candidate(index, route, weight_matrix):
    min_dist = 10000
    min_dist_index = -1
    for i in range(len(weight_matrix)):
        if not is_already_chosen(i, route) and weight_matrix[index][i] < min_dist:
            min_dist = weight_matrix[index][i]
            min_dist_index = i
    return min_dist_index

def shift_after_index(index, vector):
    vector.append(-1)
    for i in range(len(vector) - 1, index + 1, -1):
        vector[i] = vector[i - 1]
    vector[index + 1] = -1


def nearest_city_method(weight_matrix):
    result = []
    choose_first_city(result, len(weight_matrix))
    for i in range(len(weight_matrix) - 1):
        candidates = []
        print(f'\niter: {i}')
        for i in range(len(result)):
            candidate = find_candidate(result[i], result, weight_matrix)
            if candidate < 0:
                raise Exception('Wrong candidate choice')
            candidates.append({'from': result[i], 'to': candidate, 'dist': weight_matrix[result[i]][candidate]})
        print(f'Pairs: {candidates}')
        min_dist = 10000
        min_dist_candidate = None
        for candidate in candidates:
            if candidate['dist'] < min_dist:
                min_dist = candidate['dist']
                min_dist_candidate = candidate
        print(f'Chosen Pair: {min_dist_candidate}')
        shift_after_index(find_index_by_city(min_dist_candidate['from'], result), result)
        result[find_index_by_city(min_dist_candidate['from'], result) + 1] = min_dist_candidate['to']
        print(f'Current route: {result} Current dist: {calculate_total_dist(result, weight_matrix)}')
    complete_roundabout(result)
    print(f'\nTotal\nRoute:{result}\nRoute Length: {calculate_total_dist(result, weight_matrix)}')
    return result


#if __name__ == '__main__':
#    random.seed(5)
#    weight_matrix = create_weight_matrix(size=5, symmetric=True)
#    print_weight_matrix(weight_matrix)
#    result = nearest_city_method(weight_matrix)
