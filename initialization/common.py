import random


def calculate_total_dist(vector, weight_matrix):
    route_length = 0
    for i in range(len(vector) - 1):
        route_length += weight_matrix[vector[i]][vector[i + 1]]
    return route_length


def is_already_chosen(index, vector):
    for i in range(len(vector)):
        if vector[i] == index:
            return True
    return False


def choose_first_city(vector, max_numb):
    vector.append(random.randrange(max_numb))


def complete_roundabout(vector):
    vector.append(vector[0])

def find_index_by_city(city, vector):
    for i in range(len(vector)):
        if vector[i] == city:
            return i
    return None

