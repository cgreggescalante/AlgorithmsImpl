import random


def sort(lst):
    for start in range(0, len(lst) - 1):
        item = lst[start]

        pos = start
        for i in range(start + 1, len(lst)):
            if lst[i] < item:
                pos += 1

        if pos == start:
            continue

        while item == lst[pos]:
            pos += 1

        lst[pos], item = item, lst[pos]

        while pos != start:
            pos = start
            for i in range(start + 1, len(lst)):
                if lst[i] < item:
                    pos += 1

            while item == lst[pos]:
                pos += 1
            lst[pos], item = item, lst[pos]

    return lst


if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(100)]
    s_arr = sorted(arr)
    assert s_arr == sort(arr)
