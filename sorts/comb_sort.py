import time

from utils.random_array import random_array


def sort(lst):
    """
    2.138609520008322 for 5000 elements
    """
    k = 1.3
    gap = int(len(lst) / k)
    done = False
    while not done:
        if gap <= 1:
            gap = 1
            done = True
        for i in range(0, len(lst) - gap, gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                done = False
        gap = int(gap / k)
    return lst


if __name__ == '__main__':
    repeat = 10
    s = 0
    for _ in range(repeat):
        arr = random_array(1, 1000, 5000)
        start = time.perf_counter()
        sort(arr)
        s += time.perf_counter() - start
    print(s / repeat)
