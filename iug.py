from tkinter import *

root = Tk()
root.title("ZERO POINT ONE")

board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0], ]


def on_click(i, j, event):
    print("hi")


for i in range(8):
    for j in range(8):
        if i < 2:
            L = Label(root, text='    ', bg='blue')
        elif 1 < i < 6:
            L = Label(root, text='    ', bg='green')
        else:
            L = Label(root, text='    ', bg='red')
        L.grid(row = i, column=j)
        L.bind('<Button-1>', lambda e, i=i, j=j: on_click(i, j, e))

root.mainloop()
