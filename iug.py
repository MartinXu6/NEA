from tkinter import *
from PIL import Image
from PIL import ImageTk
from PIL import ImageDraw

rtpt = Image.open("Images/Pieces/r2.2.png")
rtpt = rtpt.resize((55, 55))
rzpo = Image.open("Images/Pieces/r0.1.png")
rzpo = rzpo.resize((55, 55))
ropo = Image.open("Images/Pieces/r1.1.png")
ropo = ropo.resize((55, 55))
ropt = Image.open("Images/Pieces/r1.2.png")
ropt = ropt.resize((55, 55))
rzpt = Image.open("Images/Pieces/r0.2.png")
rzpt = rzpt.resize((55, 55))
btpt = Image.open("Images/Pieces/b2.2.png")
btpt = btpt.resize((55, 55))
bzpt = Image.open("Images/Pieces/b0.2.png")
bzpt = bzpt.resize((55, 55))
bopt = Image.open("Images/Pieces/b1.2.png")
bopt = bopt.resize((55, 55))
bzpo = Image.open("Images/Pieces/b0.1.png")
bzpo = bzpo.resize((55, 55))
bopo = Image.open("Images/Pieces/b1.1.png")
bopo = bopo.resize((55, 55))

root = Tk()
root.title("ZERO POINT ONE")
root.geometry("1500x800")
root.resizable(False, False)
root.state("zoomed")

rtpt = ImageTk.PhotoImage(rtpt)
rzpo = ImageTk.PhotoImage(rzpo)
rzpt = ImageTk.PhotoImage(rzpt)
ropo = ImageTk.PhotoImage(ropo)
ropt = ImageTk.PhotoImage(ropt)
btpt = ImageTk.PhotoImage(btpt)
bzpo = ImageTk.PhotoImage(bzpo)
bzpt = ImageTk.PhotoImage(bzpt)
bopo = ImageTk.PhotoImage(bopo)
bopt = ImageTk.PhotoImage(bopt)


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

rtptl = Label(red_pieces, image=rtpt)
rtptl.place(x=7,y=7)
# rtptl.grid(row=0,column=0,padx=1,pady=1)
# bzpol= Label(blue_pieces, image=bzpo)

# bzpol.pack()
root.mainloop()
