from utils.random_array import random_array


def sort(lst):
    done = False
    while not done:
        done = True
        for i in range(1, len(lst) - 1, 2):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                done = False
        for i in range(0, len(lst) - 1, 2):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                done = False
    return lst


if __name__ == '__main__':
    arr = random_array(1, 100, 100)
    s_arr = sorted(arr)
    assert s_arr == sort(arr)
