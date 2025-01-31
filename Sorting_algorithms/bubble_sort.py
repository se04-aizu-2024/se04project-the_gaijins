import time

# bubble sort of one dimensional array


def bubble_sort(arr, drawData, timeTick):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # print(arr)
                colorArray = ["green" if x == j or x == j + 1 else "red" for x in range(len(arr))]
                drawData(arr, colorArray=colorArray)
                time.sleep(timeTick)

