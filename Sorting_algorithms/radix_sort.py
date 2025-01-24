import time

#  radix sort of one dimensional array

def counting_sort(arr, exp, drawData, timeTick):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i-1]
    
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]

        count[index % 10] -= 1
        i -= 1
    
    for i in range(n):
        arr[i] = output[i]
        drawData(arr)
        time.sleep(timeTick)
    
    return arr

def radix_sort(arr, drawData, timeTick):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp, drawData, timeTick)
        exp *= 10
    return arr
