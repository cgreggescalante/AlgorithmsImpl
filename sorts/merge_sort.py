from utils.random_array import random_array


def sort(lst):
    if len(lst) <= 1:
        return lst

    m = len(lst) // 2
    a = sort(lst[:m])
    b = sort(lst[m:])
    arr = []
    while a and b:
        if a[0] < b[0]:
            arr.append(a.pop(0))
        else:
            arr.append(b.pop(0))
    arr.extend(a)
    arr.extend(b)
    return arr


if __name__ == '__main__':
    arr = random_array(1, 100, 100)
    s_arr = sorted(arr)
    assert s_arr == sort(arr)
