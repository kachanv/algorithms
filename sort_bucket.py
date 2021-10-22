from sort_insertion import sort_insertion


# sort elements in [0,1)
# O(n) true if some conditions are met
def sort_bucket(arr: list, bucket_qty: int) -> list:
    bucket = [[] for i in range(bucket_qty)]

    for j in arr:  # put array elements in different buckets
        i_b = int(10 * j)
        bucket[i_b].append(j)

    for i in range(bucket_qty):  # sort elements in any bucket by insertion sort
        bucket[i] = sort_insertion(bucket[i])

    k = 0
    for i in range(bucket_qty):  # union the result
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr