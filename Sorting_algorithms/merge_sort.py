import time
# # merge sort of one dimensional array

# def merge_sort(arr, drawData, timeTick):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         L = arr[:mid]
#         R = arr[mid:]
        
#         merge_sort(L, drawData, timeTick)
#         merge_sort(R, drawData, timeTick)
        
#         i = j = k = 0
        
#         while i < len(L) and j < len(R):
#             # drawData(arr)
#             # time.sleep(timeTick)
#             if L[i] < R[j]:
#                 arr[k] = L[i]

#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 # drawData(arr)
#                 # time.sleep(timeTick)

#                 j += 1
#             k += 1
        
#         while i < len(L):
#             drawData(arr)
#             time.sleep(timeTick)
#             arr[k] = L[i]

#             i += 1
#             k += 1
        
#         while j < len(R):
#             arr[k] = R[j]
#             # drawData(arr)
#             # time.sleep(timeTick)

#             j += 1
#             k += 1
#     return arr

def merge_sort(arr, drawData, timeTick):
    mergesort(arr, 0, len(arr)-1, drawData, timeTick)

def mergesort(arr, left, right, drawData, timeTick):
    if left < right:
        m = (left+right)//2
        mergesort(arr, left, m, drawData, timeTick)
        mergesort(arr, m+1, right, drawData, timeTick)
 
        j = m+1
        if arr[m] <= arr[m+1]:
            return
 
        while left <= m and j <= right:
            drawData(arr)
            time.sleep(timeTick)
            if arr[left] <= arr[j]:
                left += 1
            else:
                drawData(arr)
                time.sleep(timeTick)
                temp = arr[j]
                 
                # storing the smaller element in temp variable
                i = j
                while i != left:
                    arr[i] = arr[i-1]
                    drawData(arr)
                    time.sleep(timeTick)
                    i -= 1
                 
                # this while loop will shift all the elements one step
                # to right to make the place empty for the temp variable
                # upon reaching the desired location i.e. left, the
                # temp value will be inserted into that location.
                # this process is much like insertion sort
                arr[left] = temp
 
                drawData(arr)
                time.sleep(timeTick)
                left += 1
                m += 1
                j += 1


