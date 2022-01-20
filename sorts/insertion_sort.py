from utils.random_array import random_array


def sort(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > x:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = x
    return lst


if __name__ == '__main__':
    arr = random_array(1, 100, 100)
    s_arr = sorted(arr)

    assert s_arr == sort(arr)
