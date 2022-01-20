import time

from utils.random_array import random_array


def sort(lst):
    k = max(lst)
    count = [0 for _ in range(k + 1)]
    output = [0 for _ in range(len(lst))]
    for i in lst:
        count[i] += 1
    for i in range(1, k + 1):
        count[i] += count[i - 1]
    for i in range(len(lst) - 1, -1, -1):
        count[lst[i]] -= 1
        output[count[lst[i]]] = lst[i]
    return output


if __name__ == '__main__':
    repeat = 10
    s = 0
    for _ in range(repeat):
        arr = random_array(1, 100000, 500000)
        start = time.perf_counter()
        sort(arr)
        s += time.perf_counter() - start
    print(s / repeat)
