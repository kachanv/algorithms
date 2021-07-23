from sort_quick import partition


# O(n) since the pivot element is selected randomly
def select_quick(arr: list, p: int, r: int, i: int) -> int:
    # base case of recursion
    if p == r:
        return arr[p]
    # use def partition from quicksort algorithm, find out pivot el. and swap el. in arr
    q = partition(arr, p, r)
    # calc qty elements < q
    k = q - p
    # check pivot element, maybe its i
    if i == k:
        return arr[q]
    # find out in left part of arr
    elif i < k:
        return select_quick(arr, p, q - 1, i)
    # find out in right part of arr
    else:
        return select_quick(arr, q + 1, r, i - k)
