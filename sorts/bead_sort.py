from typing import Iterable


def sort(lst: Iterable[int]) -> list[int]:
    m = max(lst)
    arr = []
    for elm in lst:
        arr.append([1] * elm + [0] * (m - elm))
    for _ in range(len(arr)):
        for col in range(m):
            for row in range(len(arr) - 1):
                if arr[row][col] == 1 and arr[row + 1][col] == 0:
                    arr[row][col], arr[row + 1][col] = arr[row + 1][col], arr[row][col]
    return [sum(a) for a in arr]


if __name__ == '__main__':
    arr = [1, 5, 9, 2, 8, 3, 7]
    assert sort(arr) == sorted(arr)
