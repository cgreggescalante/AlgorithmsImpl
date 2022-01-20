import random


def random_array(low: int, high: int, length: int) -> list[int]:
    return [random.randint(low, high) for _ in range(length)]
