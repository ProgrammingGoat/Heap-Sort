def heapify(array: list[int], i: int):
    left = 2*i
    right = 2*i+1
    max = i

    if (left <= len(array)) and (array[left] > array[i]):
        max = left
    
    if (right <= len(array)) and (array[right] > array[max]):
        max = right

    if max != i:
        array[i], array[max] = array[max], array[i]
        heapify(array, max)