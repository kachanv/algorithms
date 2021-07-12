# O(n)
# finding the maximum subarray that intersects the midpoint
def max_cross_subarray(arr: list, low: int, mid: int, high: int) -> list:
    main_sum = 0
    left_sum = arr[mid]
    left_max = mid
    for n in range(mid, low - 1, -1):
        main_sum += arr[n]
        if main_sum > left_sum:
            left_sum = main_sum
            left_max = n

    main_sum = 0
    right_sum = arr[mid + 1]
    right_max = mid + 1
    for m in range(mid + 1, high + 1):
        main_sum += arr[m]
        if main_sum > right_sum:
            right_sum = main_sum
            right_max = m

    return [left_max, right_max, left_sum + right_sum]

# O(n*lg(n))
def max_subarray_recursion(arr: list, low: int, high: int) -> list:
    if high == low:  # only 1 element in arr
        return [low, high, arr[low]]
    else:
        mid = (low + high) // 2  # midpoint find
        left_low, left_high, left_sum = max_subarray_recursion(arr, low,
                                                               mid)  # calling recursion on the left half of the array
        right_low, right_high, right_sum = max_subarray_recursion(arr, mid + 1,
                                                                  high)  # calling recursion on the right half of the array

        cross_low, cross_high, cross_sum = max_cross_subarray(arr, low, mid,
                                                              high)  # finding the maximum subarray that intersects the midpoint

    if left_sum >= right_sum and left_sum >= cross_sum:
        return [left_low, left_high, left_sum]
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return [right_low, right_high, right_sum]
    else:
        return [cross_low, cross_high, cross_sum]
