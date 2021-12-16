import random

# Метод Монте-Карло
def random_init_method(length, *args):
    output = [i for i in range(length)]
    return random.sample(output, len(output))
