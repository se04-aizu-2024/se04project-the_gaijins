import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tkinter import *
from tkinter import ttk
import random
from visualizer import *


def main_GUI():
    # The original window
    root = Tk()
    # Size of the window
    root.geometry("900x500+200+80")
    # Name of the window
    root.title("Sorting Algorithm Visualizer")
    # Color of background
    root.config(bg="#082A46")

    # Variables that will be used
    sorting_algs = [  # All sorting algorithm
        "Bubble Sort",
        "Heap Sort",
        "Insert Sort",
        "Merge Sort",
        "Quick Sort",
        "Radix Sort",
        "Selection Sort",
    ]
    selected_algorithm = StringVar()  # The algorithm that the current display shows

    def GetData():
        return list(map(int, inputtxt.get("1.0", "end-1c").split(" ")))

    def Generate():  # Generate values and display in the box
        try:
            minivalue = int(minvalue.get())
        except:
            minivalue = 1

        try:
            maxivalue = int(maxvalue.get())
        except:
            maxivalue = 100

        try:
            sizeevalue = int(sizevalue.get())
        except:
            sizeevalue = 10

        if minivalue < 0:
            minivalue = 0
        if maxivalue > 100:
            maxivalue = 100

        if minivalue > maxivalue:
            minivalue, maxivalue = maxivalue, minivalue

        inputtxt.delete("1.0", END)
        for i in range(sizeevalue):
            # Insert random value into the data field
            inputtxt.insert(END, random.randrange(minivalue, maxivalue + 1))
            if i != sizeevalue - 1:
                inputtxt.insert(END, " ")

    # Algorithm chosen
    mainlabel = Label(
        root,
        text="Algorithm:",
        font=("new roman", 16, "italic bold"),
        bg="#05897A",
        width=10,
        fg="black",
        relief=GROOVE,
        bd=5,
    )
    mainlabel.place(x=0, y=0)

    algo_menu = ttk.Combobox(
        root, width=15, font=("new roman", 19, "italic bold"), textvariable=selected_algorithm, values=sorting_algs
    )
    algo_menu.place(x=165, y=2.5)
    algo_menu.current(0)

    # Generate button
    random_generate = Button(
        root,
        text="Generate",
        bg="#2DAE9A",
        font=("arial", 12, "italic bold"),
        relief=SUNKEN,
        activebackground="#059458",
        activeforeground="white",
        bd=5,
        command=Generate,
    )
    random_generate.place(x=750, y=60)

    # Amount of elements
    sizevaluelabel = Label(
        root,
        text="Size:",
        font=("new roman", 12, "italic bold"),
        bg="#0E6DA5",
        width=10,
        fg="black",
        height=2,
        relief=GROOVE,
        bd=5,
    )
    sizevaluelabel.place(x=0, y=60)

    sizevalue = Scale(
        root,
        from_=0,
        to=30,
        resolution=1,
        orient=HORIZONTAL,
        font=("arial", 14, "italic bold"),
        width=10,
        relief=GROOVE,
        bd=2,
    )
    sizevalue.place(x=125, y=62.5)

    # Minimum value an element can be
    minvaluelabel = Label(
        root,
        text="Min value:",
        font=("new roman", 12, "italic bold"),
        bg="#0E6DA5",
        width=10,
        fg="black",
        height=2,
        relief=GROOVE,
        bd=5,
    )
    minvaluelabel.place(x=250, y=60)

    minvalue = Scale(
        root,
        from_=0,
        to=10,
        resolution=1,
        orient=HORIZONTAL,
        font=("arial", 14, "italic bold"),
        width=10,
        relief=GROOVE,
        bd=2,
    )
    minvalue.place(x=375, y=62.5)

    # Maximum value an element can be
    maxvaluelabel = Label(
        root,
        text="Max value:",
        font=("new roman", 12, "italic bold"),
        bg="#0E6DA5",
        width=10,
        fg="black",
        height=2,
        relief=GROOVE,
        bd=5,
    )
    maxvaluelabel.place(x=500, y=60)

    maxvalue = Scale(
        root,
        from_=0,
        to=100,
        resolution=1,
        orient=HORIZONTAL,
        font=("arial", 14, "italic bold"),
        width=10,
        relief=GROOVE,
        bd=2,
    )
    maxvalue.place(x=625, y=62.5)

    # Speed of the sorting algorithm
    speedlabel = Label(
        root, text="Speed:", font=("new roman", 12, "italic bold"), bg="#0E6DA5", width=10, fg="black", relief=GROOVE, bd=5
    )
    speedlabel.place(x=500, y=0)

    speedscale = Scale(
        root,
        from_=0.01,
        to=1,
        resolution=0.01,
        orient=HORIZONTAL,
        font=("arial", 14, "italic bold"),
        width=10,
        relief=GROOVE,
        bd=2,
    )
    speedscale.place(x=620, y=0)

    # Text box that will show generated array and also you can change data of the elements
    inputtxt = Text(root, width=108, height=20, relief=GROOVE, bd=5)
    inputtxt.place(x=10, y=130)

    # Start sorting button
    start = Button(
        root,
        text="Start",
        bg="#C45B09",
        font=("arial", 12, "italic bold"),
        relief=SUNKEN,
        activebackground="#059458",
        activeforeground="white",
        bd=5,
        width=10,
        command=lambda: start_visualizer(root, GetData(), selected_algorithm.get(), speedscale.get()),
    )
    start.place(x=750, y=0)

    # Let the window exists continuously
    root.mainloop()