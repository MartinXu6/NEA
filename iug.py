from tkinter import *
from PIL import Image
from PIL import ImageTk
from PIL import ImageDraw

rtpt = Image.open("Images/Pieces/r2.2.png")
rtpt = rtpt.resize((55, 55))
ropo = Image.open("Images/Pieces/r0.1.png")
ropo = ropo.resize((55, 55))

root = Tk()
root.title("ZERO POINT ONE")
root.geometry("1500x800")
root.resizable(False, False)
root.state("zoomed")

rtpt = ImageTk.PhotoImage(rtpt)
ropo = ImageTk.PhotoImage(ropo)


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
main_board.place(relx=0.5, y=350, anchor="center")
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
red_pieces = Frame(root, bg="red", width=500, height=100, )
red_pieces.place(relx=0.5, y=650, anchor="center")
blue_pieces = Frame(root, bg="blue", width=500, height=100, )
blue_pieces.place(relx=0.5, y=50, anchor="center")

rtptl = Label(root, image=rtpt)
ropol= Label(root, image=ropo)

rtptl.pack()
ropol.pack()
root.mainloop()
