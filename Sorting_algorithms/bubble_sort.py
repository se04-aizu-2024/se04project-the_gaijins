import time

# bubble sort of one dimensional array


def bubble_sort(arr, drawData, timeTick):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # print(arr)
                drawData(arr)
                time.sleep(timeTick)

    # return arr

# import time

# def bubble_sort(arr, drawData, timeTick):
#     n = len(arr)
#     update_count = 0
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 update_count += 1
#                 if update_count % 10 == 0:  # Update the canvas every 10 swaps
#                     drawData(arr, ['green' if x == j or x == j+1 else 'red' for x in range(len(arr))])
#                     time.sleep(1)
#     drawData(arr, ['green' for x in range(len(arr))])