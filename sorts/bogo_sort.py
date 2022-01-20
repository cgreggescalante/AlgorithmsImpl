import random

from utils.random_array import random_array


def sort(lst):
    while True:
        done = True
        for i, a in enumerate(lst[:-1]):
            if a > lst[i + 1]:
                done = False
        if done:
            return lst
        random.shuffle(lst)


if __name__ == '__main__':
    arr = random_array(1, 100, 100)
    s_arr = sorted(arr)
    assert sort(arr.copy()) == s_arr
