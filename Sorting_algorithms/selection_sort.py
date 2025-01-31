import time

# selection sort of one dimensional array


def selection_sort(arr, drawData, timeTick):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        colorArray = ["green" if x == i or x == min_idx else "red" for x in range(len(arr))]
        drawData(arr, colorArray=colorArray)
        time.sleep(timeTick)
    return arr
