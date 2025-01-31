import time

# quick sort of one dimensional array


def quick_sort(arr, drawData, timeTick):
    quicksort(arr, 0, len(arr) - 1, drawData, timeTick)


def partition(arr, low, high, drawData, timeTick):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            colorArray = ["green" if x == i or x == j else "red" for x in range(len(arr))]
            drawData(arr, colorArray=colorArray)
            time.sleep(timeTick)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    colorArray = ["green" if x == i + 1 or x == high else "red" for x in range(len(arr))]
    drawData(arr, colorArray=colorArray)
    time.sleep(timeTick)
    return i + 1


def quicksort(arr, low, high, drawData, timeTick):
    if low < high:
        pi = partition(arr, low, high, drawData, timeTick)
        quicksort(arr, low, pi - 1, drawData, timeTick)
        quicksort(arr, pi + 1, high, drawData, timeTick)
    return arr
