import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time

from tkinter import *
from tkinter import ttk
import random
from Sorting_algorithms import *

root = Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry("900x600+200+80")
root.config(bg='black')

array = [random.randint(1, 100) for i in range(50)]

algorithm = "bubble_sort"

mainlabel = Label(root, text="Sorting Algorithm Visualizer", font=('arial', 20, 'bold'), bg='black', fg='white')
mainlabel.place(x=10, y=10)

def drawData(array, colorArray=['red' for i in range(len(array))]):
    canvas.delete("all")
    c_height = 450
    c_width = 870
    x_width = c_width / (len(array) + 1)
    offset = 10
    normalizedData = [i / max(array) for i in array]
    print(array)
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset 
        y0 = c_height - height * 400
        x1 = (i + 1) * x_width
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(array[i]))
    root.update_idletasks()


def generate(array):
    colorArray = ['red' for i in range(len(array))]
    drawData(array, colorArray)


def startAlgorithm():
    global array
    # print("Algorithm selected: " + algorithm)

    drawData(array)

    bubble_sort(array, drawData, 0.01)

    # generate(array)

canvas = Canvas(root, width=870, height=450, bg='white')
canvas.place(x=10, y=70)

# generate(array)
# time.sleep(1)
startAlgorithm()

root.mainloop()




