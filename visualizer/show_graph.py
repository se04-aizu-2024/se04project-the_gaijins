import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
#     - miracle sort: "Do we need this Sort"
#     - quick sort: "Quick Sort"
#     - radix sort: "Radix Sort"
#     - selection sort: "Selection Sort"

# passed_algorithm = "Selection Sort"

def start_visualizer(array, sorting_algorithm_type, interval):
    global timeTick 
    timeTick = interval
    startAlgorithm(array, sorting_algorithm_type)

Algorithms = {
    "Bubble Sort" : bubble_sort,
    "Heap Sort" : heap_sort,
    "Insert Sort" : insertion_sort,
    "Merge Sort" : merge_sort,
    "Quick Sort" : quick_sort,
    "Radix Sort" : radix_sort,
    "Selection Sort" : selection_sort,
}

root = Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry("900x600+200+80")
root.config(bg='black')

array = [random.randint(1, 100) for i in range(50)]

mainlabel = Label(root, text="Sorting Algorithm Visualizer", font=('arial', 20, 'bold'), bg='black', fg='white')
mainlabel.place(x=10, y=10)

def drawData(array, colorArray=['red' for i in range(len(array))]):
    global canvas
    canvas.delete("all")
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
        print(x0, y0, x1, y1)
        canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        canvas.create_text(x0 + 2, y0, anchor=S, text=str(array[i]))
    root.update()


def generate(array):
    colorArray = ['red' for i in range(len(array))]
    drawData(array, colorArray)


def startAlgorithm(array, passed_algorithm):
    generate(array)
    time.sleep(1.5)

    Algorithms[passed_algorithm](array, drawData, timeTick)

    # generate(array)

canvas = Canvas(root, width=870, height=450, bg='white')
canvas.place(x=10, y=70)


# time.sleep(1)

start = Button(root, text="Start",bg="blue", relief=SUNKEN, activebackground="blue", activeforeground="yellow", bd=5, width=10, command=startAlgorithm)
start.place(x=750, y=0)

# startAlgorithm()


root.mainloop()




