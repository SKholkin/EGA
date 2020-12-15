def encode(coding: list):
    normal_order = [i for i in range(len(coding))]
    order_coding = []
    for i in range(len(coding)):
        order_coding.append(normal_order[coding[i]])
        normal_order[coding[i]] = -1
        for j in range(coding[i], len(coding)):
            normal_order[j] -= 1
    return order_coding


def decode(order_coding):
    normal_order_rev = [i for i in range(len(order_coding))]
    coding = []
    for i in range(len(order_coding)):
        coding.append(normal_order_rev[order_coding[i]])
        for j in range(order_coding[i], len(order_coding) - 1):
            normal_order_rev[j] = normal_order_rev[j + 1]
    return coding


def check_condition(coding):
    for i in range(len(coding)):
        if coding[i] > len(coding) - i - 1:
            return False
    return True


def upper_boundary(place, coding_length):
    return coding_length - place - 1
