# O(n)
def max_subarray_kadane(arr: list) -> list:
    cur_sum, cur_min, cur_max = 0, 0, 0 # var for current values
    best_sum, best_min, best_max = float('-inf'), 0, 0 # buffer var for result_values

    for i, n in enumerate(arr): # iter arr
        cur_sum += n
        cur_max = i

        if cur_sum > best_sum: # if current values > buffer result values => update result values
            best_max = cur_max
            best_min = cur_min
            best_sum = cur_sum

        if cur_sum <= 0: # if current sum values <= drop current values
            cur_sum = 0
            cur_min = i + 1
            cur_max = i + 1

    return [best_min, best_max , best_sum]