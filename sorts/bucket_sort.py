import random

from sorts import bubble_sort


def sort(lst, k):
    buckets = [[] for _ in range(k)]
    m = max(lst) + 1
    for i in lst:
        buckets[int(k * i / m)].append(i)
    out = []
    for bucket in buckets:
        out += bubble_sort.sort(bucket)
    return out


if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(100)]
    s_arr = sorted(arr)
    assert sort(arr, 5) == s_arr
