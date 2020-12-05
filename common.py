import json


def hamming_distance(vector1, vector2):
    h = 0
    for i in range(len(vector1)):
        if not vector1[i] == vector2[i]:
            h += 1
    return h

