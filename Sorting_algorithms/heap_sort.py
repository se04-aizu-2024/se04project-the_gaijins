import time

# heap sort of one dimensional array


def heapify(arr, n, i, drawData, timeTick):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        colorArray = ["green" if x == i or x == largest else "red" for x in range(len(arr))]
        drawData(arr, colorArray=colorArray)
        time.sleep(timeTick)
        heapify(arr, n, largest, drawData, timeTick)


def heap_sort(arr, drawData, timeTick):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, drawData, timeTick)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]

        colorArray = ["green" if x == i or x == 0 else "red" for x in range(len(arr))]
        drawData(arr, colorArray=colorArray)
        time.sleep(timeTick)
        heapify(arr, i, 0, drawData, timeTick)

    return arr
