# O(lg(n))
def max_heapify(arr: list, i: int, heap_size: int) -> list:  # binary-heap test conditions for a node "i" in binary-heap "arr" with len "heap_size"
    left = 2 * i + 1  # if the binary-heap is packed into an list then "i" node leafs start with "2 * i + 1"
    right = 2 * i + 2

    if left < heap_size and arr[left] > arr[i]:  # compare left leaf with node
        max = left
    else:
        max = i

    if right < heap_size and arr[right] > arr[max]:  # compare right leaf with node
        max = right

    if max != i:
        arr[i], arr[max] = arr[max], arr[i]  # find max and swap with node
        max_heapify(arr, max, heap_size)

    return arr


# O(n)
def build_binary_max_heap(arr: list) -> list:  # build binary-heap from list
    heap_size = len(arr)
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(arr, i, heap_size)

    return arr


# O(n*lg(n))
def sort_heap(arr: list) -> list:
    heap_size = len(arr)
    build_binary_max_heap(arr)  # build binary-heap

    for i in range(len(arr) - 1, 0, -1):  # 1-st element binary-heap - greatest forever
        arr[i], arr[0] = arr[0], arr[i]  # swap 1-st (greatest) el. with i el.
        heap_size -= 1
        max_heapify(arr, 0, heap_size)  # place swap-element to new correct position

    return arr
