# O(n*lg(n))
def sort_merge(arr: list) -> list:
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        i, j, k = 0, 0, 0 # i-left counter, j-right counter, k- main unit counter

        sort_merge(left)  # recursion work because list is mutable type
        sort_merge(right) # row 8-9 divide & union part of solution

        while i < len(left) and j < len(right):
            if left[i] <= right[j]: # left[i] >= right[j] - arr will be sorting desc
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left): # row 20-28 add sorted rest to main list
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
