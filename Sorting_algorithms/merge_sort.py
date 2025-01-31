import time

# merge sort of one dimensional array


def merge_sort(arr, drawData, timeTick):
    mergesort(arr, 0, len(arr) - 1, drawData, timeTick)


def mergesort(arr, left, right, drawData, timeTick):
    if left < right:
        m = (left + right) // 2
        mergesort(arr, left, m, drawData, timeTick)
        mergesort(arr, m + 1, right, drawData, timeTick)

        j = m + 1
        if arr[m] <= arr[m + 1]:
            return

        while left <= m and j <= right:
            colorArray = ["green" if x == left or x == j else "red" for x in range(len(arr))]
            drawData(arr, colorArray=colorArray)
            time.sleep(timeTick)
            if arr[left] <= arr[j]:
                left += 1
            else:
                # colorArray = ["green" if x == j else "red" for x in range(len(arr))]
                drawData(arr, colorArray=colorArray)
                time.sleep(timeTick)
                temp = arr[j]

                # storing the smaller element in temp variable
                i = j
                while i != left:
                    arr[i] = arr[i - 1]
                    colorArray = ["green" if x == i or x == left else "red" for x in range(len(arr))]
                    drawData(arr, colorArray=colorArray)
                    time.sleep(timeTick)
                    i -= 1

                # this while loop will shift all the elements one step
                # to right to make the place empty for the temp variable
                # upon reaching the desired location i.e. left, the
                # temp value will be inserted into that location.
                # this process is much like insertion sort
                arr[left] = temp

                # colorArray = ["green" if x == left else "red" for x in range(len(arr))]
                drawData(arr, colorArray=colorArray)
                time.sleep(timeTick)
                left += 1
                m += 1
                j += 1


# def merge_sort(data, drawData, timeTick):
#     merge_sort_algo(data, 0, len(data), drawData, timeTick)

# def merge_sort_algo(data, left, right, drawData, timeTick):
#     if left < right:
#         middle = (left + right) // 2
#         merge_sort_algo(data, left, middle, drawData, timeTick)
#         merge_sort_algo(data, middle + 1, right, drawData, timeTick)
#         merge(data, left, middle, right, drawData, timeTick)

# def merge(data, left, middle, right, drawData, timeTick):

#     drawData(data, colorArray(len(data), left, middle, right))
#     time.sleep(timeTick)

#     leftpart = data[left:middle + 1]
#     rightpart = data[middle + 1: right + 1]

#     leftIdx = rightIdx = 0

#     for dataIdx in range(left, right):
#         if leftIdx < len(leftpart) and rightIdx < len(rightpart):
#             if leftpart[leftIdx] <= rightpart[rightIdx]:
#                 data[dataIdx] = leftpart[leftIdx]
#                 leftIdx += 1
#             else:
#                 data[dataIdx] = rightpart[rightIdx]
#                 rightIdx += 1
#         elif leftIdx < len(leftpart):
#             data[dataIdx] = leftpart[leftIdx]
#             leftIdx += 1
#         else:
#             data[dataIdx] = rightpart[rightIdx]
#             rightIdx += 1

#     drawData(data, colorArray = ["green" if x >= left and x <= right else "red" for x in range(len(data))])
#     time.sleep(timeTick)

# def colorArray(length, left, middle, right):
#     colorArray = []

#     for i in range(length):
#         if left <= i and i <= right:
#             if left <= i and i <= middle:
#                 colorArray.append("red")
#             else:
#                 colorArray.append("green")
#         else:
#             colorArray.append("green")
#     return colorArray