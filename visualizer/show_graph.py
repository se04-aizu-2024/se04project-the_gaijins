import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import time
from tkinter import *
from tkinter import ttk
import random
from Sorting_algorithms import *

# start_visualizer(arr, sorting_algorithm_type, interval)

# sorting_algorithm_type
#     - bubble sort: "Bubble Sort"
#     - heap sort: "Heap Sort"
#     - insert sort: "Insert Sort"
#     - merge sort: "Merge Sort"
#     - quick sort: "Quick Sort"
#     - radix sort: "Radix Sort"
#     - selection sort: "Selection Sort"



def start_visualizer(root, array, sorting_algorithm_type, interval):
    global timeTick
    global newWindow
    global canvas

    newWindow = Toplevel(root)
    newWindow.title("Sorting Algorithm Visualizer")
    newWindow.geometry("900x600+200+80")
    newWindow.config(bg="black")

    mainlabel = Label(
        newWindow, text=sorting_algorithm_type + " Visualizer", font=("arial", 20, "bold"), bg="black", fg="white"
    )
    mainlabel.place(x=10, y=10)

    canvas = Canvas(newWindow, width=870, height=450, bg="white")
    canvas.place(x=10, y=70)

    timeTick = interval
    startAlgorithm(array, sorting_algorithm_type)


Algorithms = {
    "Bubble Sort": bubble_sort,
    "Heap Sort": heap_sort,
    "Insert Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Radix Sort": radix_sort,
    "Selection Sort": selection_sort,
}


def drawData(array, *args, **kwargs):
    global canvas
    canvas.delete("all")

    # print(kwargs)

    colorArray = kwargs.get("colorArray") or ["red" for x in range(len(array))]

    c_height = 450
    c_width = 870
    x_width = c_width / (len(array) + 1)
    offset = 10
    spacing = 10
    normalizedData = [i / max(array) for i in array]
    # print(array)
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 400
        x1 = (i + 1) * x_width
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i] or "red")
        canvas.create_text(x0 + 2, y0, anchor=S, text=str(array[i]))
    newWindow.update()


def startAlgorithm(array, passed_algorithm):
    drawData(array)
    time.sleep(1.5)

    Algorithms[passed_algorithm](array, drawData, timeTick)
