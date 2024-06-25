def heapify(array: list[int], i: int):
    left = 2*(i+1)-1
    right = 2*(i+1)
    max = i

    if (left < len(array)) and (array[left] > array[i]):
        max = left
    
    if (right < len(array)) and (array[right] > array[max]):
        max = right

    if max != i:
        array[i], array[max] = array[max], array[i]
        heapify(array, max)

def build_max_heap(array: list[int]):
    for i in range(len(array)//2-1, -1, -1):
        heapify(array, i)

def heapsort(array: list[int]):
    output = []
    print("Initial Array:", array)
    print()
    build_max_heap(array)
    for i in range(len(array)-1, -1, -1):
        print("Current Heap:", array)
        array[0], array[i] = array[i], array[0]
        output.insert(0, array.pop(-1))
        heapify(array, 0)
        print("Output Array:", output)
        print()

    print()
    print("Final Array:", output)
    return output