import time

from utils.random_array import random_array


def sort(lst):
    """
    2.1921504700090737 for 5000 elements
    """
    for i in range(len(lst) // 2 + 1):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        for j in range(len(lst) - 1, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
    return lst


def sort1(lst):
    """
    1.792197269987082 for 5000 elements
    """
    for i in range(len(lst) // 2 + 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        for j in range(len(lst) - 1 - i, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
    return lst


def sort2(lst):
    """
    1.334287100005895 for 5000 elements
    """
    for i in range(len(lst) // 2 + 1):
        swapped = False
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                swapped = True
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if not swapped:
            break
        for j in range(len(lst) - 1 - i, 0, -1):
            if lst[j] < lst[j - 1]:
                swapped = True
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
        if not swapped:
            break
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
