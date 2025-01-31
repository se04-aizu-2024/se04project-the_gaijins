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
        # "Do you need this Sort",
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

    # # Create an Exit button.
    # b2 = Button(root, text = "NEXT",
    # 			command = root.destroy)

    # l.pack()
    # T.pack()
    # b2.pack()

    # # Insert The Fact.
    # T.insert(tk.END, Fact)
    # root.mainloop()

    # #ACCEPT NUMBER OF Input
    # win = tk.Tk()
    # win.geometry("700x350")
    # # Create an Entry widget
    # a=Entry(win, width=35)
    # a.pack()
    # Button(win, text="Enter number of Display BARS from", command=Accept_value).pack()
    # Button(win, text="Next", command=win.destroy).pack()

    # win.mainloop()

    # #Making a window using the Tk widget
    # window = tk.Tk()
    # window.title('Sorting Visualizer')
    # window.geometry('1000x450')

    # #Making a Canvas within the window to display contents
    # canvas = tk.Canvas(window, width='1000', height='400')
    # canvas.grid(column=0,row=0, columnspan = 50)

    # #Buttons
    # insert = tk.Button(window, text='Insertion Sort', command=insertion_sort)
    # select = tk.Button(window, text='Selection Sort', command=selection_sort)
    # bubble = tk.Button(window, text='Bubble Sort', command=bubble_sort)
    # shuf = tk.Button(window, text='Shuffle', command=generate)
    # insert.grid(column=1,row=1)
    # select.grid(column=2,row=1)
    # bubble.grid(column=3,row=1)
    # shuf.grid(column=0, row=1)

    # generate()
    # window.mainloop()

    # #Import the required Libraries
    # from tkinter import *
    # import tkinter as tk
    # import random
    # import time

    # #accepting value:

    # #n =int(input("Enter Total Number of Elements:    "))

    # #Function to swap two bars that will be animated
    # def swap(pos_0, pos_1):

    #     bar11, _, bar12, _ = canvas.coords(pos_0)
    #     bar21, _, bar22, _ = canvas.coords(pos_1)
    #     canvas.move(pos_0, bar21-bar11, 0)
    #     canvas.move(pos_1, bar12-bar22, 0)

    # worker = None

    # #Insertion Sort
    # def _insertion_sort():
    #     global barList
    #     global lengthList

    #     for i in range(len(lengthList)):
    #         cursor = lengthList[i]
    #         cursorBar = barList[i]
    #         pos = i

    #         while pos > 0 and lengthList[pos - 1] > cursor:
    #             lengthList[pos] = lengthList[pos - 1]
    #             barList[pos], barList[pos - 1] = barList[pos - 1], barList[pos]
    #             swap(barList[pos],barList[pos-1])
    #             yield
    #             pos -= 1

    #         lengthList[pos] = cursor
    #         barList[pos] = cursorBar
    #         swap(barList[pos],cursorBar)

    # #Bubble Sort
    # def _bubble_sort():
    #     global barList
    #     global lengthList

    #     for i in range(len(lengthList) - 1):
    #         for j in range(len(lengthList) - i - 1):
    #             if(lengthList[j] > lengthList[j + 1]):
    #                 lengthList[j] , lengthList[j + 1] = lengthList[j + 1] , lengthList[j]
    #                 barList[j], barList[j + 1] = barList[j + 1] , barList[j]
    #                 swap(barList[j + 1] , barList[j])
    #                 yield

    # #Selection Sort
    # def _selection_sort():
    #     global barList
    #     global lengthList

    #     for i in range(len(lengthList)):
    #         min = i
    #         time.sleep(0.5)
    #         for j in range(i + 1 ,len(lengthList)):
    #             if(lengthList[j] < lengthList[min]):
    #                 min = j
    #         lengthList[min], lengthList[i] = lengthList[i] ,lengthList[min]
    #         barList[min] , barList[i] = barList[i] , barList[min]

    #         swap(barList[min] , barList[i])

    #         yield

    # #Animation Function
    # def animate():
    #     global worker
    #     if worker is not None:
    #         try:
    #             next(worker)
    #             window.after(10, animate)
    #         except StopIteration:
    #             worker = None
    #         finally:
    #             window.after_cancel(animate)

    # #Generator function for generating data
    # def generate():
    #     global barList
    #     global lengthList
    #     canvas.delete('all')
    #     barstart = 5
    #     barend = 15
    #     barList = []
    #     lengthList = []

    #     #Creating a rectangle
    #     for bar in range(0, (number)):
    #         randomY = random.randint(1, 360)
    #         bar = canvas.create_rectangle(barstart, randomY, barend, 365, fill='yellow')
    #         barList.append(bar)
    #         barstart += 10
    #         barend += 10

    #     #Getting length of the bar and appending into length list
    #     for bar in barList:
    #         bar = canvas.coords(bar)
    #         length = bar[3] - bar[1]
    #         lengthList.append(length)

    #     #Maximum is colored Red
    #     #Minimum is colored Black
    #     for i in range(len(lengthList)-1):
    #         if lengthList[i] == min(lengthList):
    #             canvas.itemconfig(barList[i], fill='red')
    #         elif lengthList[i] == max(lengthList):
    #             canvas.itemconfig(barList[i], fill='black')

    # #for Accepting total number of Inputs
    # def Accept_value():
    #    global number
    #    t1=int(a.get())
    #    number = t1

    # #Main Code(Driver Code)

    # root = Tk()
    # # specify size of window.
    # root.geometry("700x350")
    # # Create text widget and specify size.
    # T = Text(root, height = 5, width = 52,bg = "yellow")
    # # Create label
    # l = Label(root, text = "SORTING ALGORITHM VISUALIZER")
    # l.config(font =("Courier", 14))

    # Fact = """MINI PROJECT
    #           Group Members are :-
    #           ADITYA SURYAWANSHI
    #           MIHIR SONAWANE"""

    # # Create an Exit button.
    # b2 = Button(root, text = "NEXT",
    # 			command = root.destroy)

    # l.pack()
    # T.pack()
    # b2.pack()

    # # Insert The Fact.
    # T.insert(tk.END, Fact)
    # root.mainloop()

    # #ACCEPT NUMBER OF Input
    # win = tk.Tk()
    # win.geometry("700x350")
    # # Create an Entry widget
    # a=Entry(win, width=35)
    # a.pack()
    # Button(win, text="Enter number of Display BARS from", command=Accept_value).pack()
    # Button(win, text="Next", command=win.destroy).pack()

    # win.mainloop()

    # #Making a window using the Tk widget
    # window = tk.Tk()
    # window.title('Sorting Visualizer')
    # window.geometry('1000x450')

    # #Making a Canvas within the window to display contents
    # canvas = tk.Canvas(window, width='1000', height='400')
    # canvas.grid(column=0,row=0, columnspan = 50)

    # #Buttons
    # insert = tk.Button(window, text='Insertion Sort', command=insertion_sort)
    # select = tk.Button(window, text='Selection Sort', command=selection_sort)
    # bubble = tk.Button(window, text='Bubble Sort', command=bubble_sort)
    # shuf = tk.Button(window, text='Shuffle', command=generate)
    # insert.grid(column=1,row=1)
    # select.grid(column=2,row=1)
    # bubble.grid(column=3,row=1)
    # shuf.grid(column=0, row=1)

    # generate()
