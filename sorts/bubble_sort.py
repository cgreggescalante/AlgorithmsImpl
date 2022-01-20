import time

from utils.random_array import random_array


def sort(lst):
    """
    2.1533379399974364 for 5000 elements
    """
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
    return lst


def sort1(lst):
    """
    1.37956524999463 for 5000 elements
    """
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
    return lst


def sort2(lst):
    """
    1.3715944900002797 for 5000 elements
    """
    for i in range(len(lst)):
        swapped = False
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
                swapped = True
        if not swapped:
            return lst
    return lst


if __name__ == '__main__':
    repeat = 10
    s = 0
    for _ in range(repeat):
        arr = random_array(1, 1000, 5000)
        start = time.perf_counter()
        sort2(arr)
        s += time.perf_counter() - start
    print(s / repeat)
