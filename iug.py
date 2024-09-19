from tkinter import *

root = Tk()
root.title("ZERO POINT ONE")
root.geometry("1500x800")
root.resizable(False, False)
canvas = Canvas()


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
main_board = Frame(root, bg="black", bd=0, width=440, height=440)
main_board.place(relx=0.5, y=370, anchor="center")
for i in range(8):
    for j in range(8):
        if 6 <= i <= 7:
            square = Frame(main_board, height=55, width=55, bg="red")
        elif 0 <= i <= 1:
            square = Frame(main_board, height=55, width=55, bg="blue")
        else:
            square = Frame(main_board, height=55, width=55, bg="white")
        square.bind("<Button-1>", lambda e, i=i, j=j: on_click(i, j, e))
        square.grid(row=i, column=j, padx=1, pady=1)
red_pieces = Frame(root, bg="brown", width=500, height=100, )
red_pieces.place(relx=0.5, y=680, anchor="center")
blue_pieces = Frame(root, bg="purple", width=500, height=100, )
blue_pieces.place(relx=0.5, y=60, anchor="center")
canvas.pack()
root.mainloop()
