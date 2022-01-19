import random


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
    arr = [1, 6, 2, 7, 8, 5, 1, 3]
    assert sort(arr.copy()) == sorted(arr)
