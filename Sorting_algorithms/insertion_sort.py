import time

# insertion sort for one dimensional array


def insertion_sort(arr, drawData, timeTick):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            colorArray = ["green" if x == j or x == j + 1 else "red" for x in range(len(arr))]
            drawData(arr, colorArray=colorArray)
            time.sleep(timeTick)
            j -= 1
        arr[j + 1] = key
    return arr
