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


def board_on_click(i, j, event):
    print(i, j)


def piece_on_click(i, j, event,side,index):
    print(index)


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
        square.bind("<Button-1>", lambda e, i=i, j=j: board_on_click(i, j, e))
        square.grid(row=i, column=j, padx=1, pady=1)
red_pieces = Frame(root, bg="yellow", width=470, height=110, )
red_pieces.place(relx=0.5, y=650, anchor="center")
blue_pieces = Frame(root, bg="yellow", width=470, height=110, )
blue_pieces.place(relx=0.5, y=50, anchor="center")
rtptl1, rtptl2, rtptl3, rtptl4, rtptl5, rtptl6, rtptl7, rtptl8, rzptl1, rzptl2, rzptl3, rzptl4, ropol1, ropol2, roptl, rzpol = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
red = [rtptl1, rtptl2, rtptl3, rtptl4, rtptl5, rtptl6, rtptl7, rtptl8, rzptl1, rzptl2, rzptl3, rzptl4, ropol1, ropol2,
       roptl, rzpol]

counter = 0
for i in range(8):
    red[i] = Label(red_pieces, image=rtpt, bg="yellow")
    red[i].bind("<Button-1>", lambda e, i=-1, j=-1,index = i ,s ="red": piece_on_click(i, j, e, s,index))
    red[i].place(relx=0.126 * counter)
    counter += 1
counter = 0
for i in range(8, 12):
    red[i] = Label(red_pieces, image=rzpt, bg="yellow")
    red[i].bind("<Button-1>", lambda e, i=-1, j=-1, index = i, s="red": piece_on_click(i, j, e, s,index))
    red[i].place(relx=0.126 * counter, y=55)
    counter += 1
counter = 0
for i in range(12, 14):
    red[i] = Label(red_pieces, image=ropo, bg="yellow")
    red[i].bind("<Button-1>", lambda e, i=-1, j=-1, index = i, s="red": piece_on_click(i, j, e, s,index))
    red[i].place(relx=4 * 0.126 + 0.126 * counter, y=55)
    counter += 1
red[14] = Label(red_pieces, image=ropt, bg="yellow")
red[14].bind("<Button-1>", lambda e, i=-1, j=-1, index = 14,s ="red": piece_on_click(i, j, e, s,index))
red[14].place(relx=6 * 0.126, y=55)
red[15] = Label(red_pieces, image=rzpo, bg="yellow")
red[15].bind("<Button-1>", lambda e, i=-1, j=-1, index =15,s ="red": piece_on_click(i, j, e, s,index))
red[15].place(relx=7 * 0.126, y=55)

btptl1, btptl2, btptl3, btptl4, btptl5, btptl6, btptl7, btptl8, bzptl1, bzptl2, bzptl3, bzptl4, bopol1, bopol2, boptl, bzpol = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
blue = [btptl1, btptl2, btptl3, btptl4, btptl5, btptl6, btptl7, btptl8, bzptl1, bzptl2, bzptl3, bzptl4, bopol1, bopol2,
        boptl, bzpol]
counter = 0
for i in range(8):
    blue[i] = Label(blue_pieces, image=btpt, bg="yellow")
    blue[i].bind("<Button-1>", lambda e, i=-1, j=-1, index = i,s="blue": piece_on_click(i, j, e, s,index))
    blue[i].place(relx=0.126 * counter)
    counter += 1
counter = 0
for i in range(8, 12):
    blue[i] = Label(blue_pieces, image=bzpt, bg="yellow")
    blue[i].bind("<Button-1>", lambda e, i=-1, j=-1, index = i, s="blue": piece_on_click(i, j, e, s,index))
    blue[i].place(relx=0.126 * counter, y=55)
    counter += 1
counter = 0
for i in range(12, 14):
    blue[i] = Label(blue_pieces, image=bopo, bg="yellow")
    blue[i].bind("<Button-1>", lambda e, i=-1, j=-1,index =i, s="blue": piece_on_click(i, j, e, s,index))
    blue[i].place(relx=4 * 0.126 + 0.126 * counter, y=55)
    counter += 1
blue[14] = Label(blue_pieces, image=bopt, bg="yellow")
blue[14].bind("<Button-1>", lambda e, i=-1, j=-1, index =14, s="blue": piece_on_click(i, j, e, s,index))
blue[14].place(relx=6 * 0.126, y=55)
blue[15] = Label(blue_pieces, image=bzpo, bg="yellow")
blue[15].bind("<Button-1>", lambda e, i=-1, j=-1,index = 15, s="blue": piece_on_click(i, j, e, s,index))
blue[15].place(relx=7 * 0.126, y=55)

blue[15] = Label(main_board, image=bzpo, bg="yellow")
blue[15].bind("<Button-1>", lambda e, i=-1, j=-1,index = 15, s="blue": piece_on_click(i, j, e, s,index))
blue[15].place(relx=0 * 0.126, y=0)

root.mainloop()
