from  common.create_test_data import create_arr_for_sort

def sort_insertion(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while arr[i] > key and i >= 0:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr

arr = create_arr_for_sort()

print(sort_insertion(arr))

