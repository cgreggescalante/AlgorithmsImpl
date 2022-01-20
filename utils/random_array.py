import random


def random_array(a, b, length):
    return [random.randint(a, b) for _ in range(length)]
