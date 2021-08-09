# given an array of integers, return indices of the two numbers such that they add up to a specific "sum"
# O(n)
def search_two_sum(arr: list, sum: int) -> list:
    hash_map = {}
    for i in range(len(arr)):
        remainder = sum - arr[i]
        if remainder in hash_map:
            return [hash_map[remainder], i]
        hash_map[arr[i]] = i
