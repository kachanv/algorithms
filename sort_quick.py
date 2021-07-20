from random import randint


def partition(arr: list, p: int, r: int) -> int:
    f = randint(p, r)  # get random ind from p to r by "support element" (aka SE)
    arr[f], arr[r] = arr[r], arr[f]  # swap random el. with last el.

    x = arr[r]  # value of last element (SE)
    i = p - 1  # border of elements less then x

    for j in range(p, r):  # swap element <= SE
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]  # insert SE after border

    return i + 1  # return index of SE


# O(n*lg(n)) for the middle case
def sort_quick(arr: list, p: int, r: int) -> list:
    if p < r:  # recursion stop condition
        q = partition(arr, p, r)  # find SE & sort
        sort_quick(arr, p, q - 1)  # recursion for left part about SE
        sort_quick(arr, q + 1, r)  # recursion for right part about SE

    return arr
