import random


def sort(lst):
    i = 0
    while i < len(lst):
        if i == 0 or lst[i] >= lst[i - 1]:
            i += 1
        else:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
    return lst


if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(100)]
    s_arr = sorted(arr)
    assert sort(arr) == s_arr
