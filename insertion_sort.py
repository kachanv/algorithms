# O(n^2)
def insertion_sort(arr: list) -> list:
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while arr[i] > key and i >= 0:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr
