from tkinter import *

root = Tk()
root.title("ZERO POINT ONE")
root.geometry("800x600")
root.resizable(False, False)


def on_click(i, j, event):
    print(i, j)


board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0], ]
counter = 0
for i in range(8):
    for j in range(8):
        if counter %2 ==0 :
            square = Label(root, height=4, width=8, bg="red")
            counter += 1
        else:
            square = Label(root, height=4, width=8, bg="black")
            counter += 1
        square.bind("<Button-1>", lambda e, i=i, j=j: on_click(i, j, e))
        square.place(x=i * 50 + 185, y=j * 50+85)
root.mainloop()
