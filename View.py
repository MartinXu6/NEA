from tkinter import *
from PIL import Image
from PIL import ImageTk


class GUI:
    def __init__(self):
        self.root = Tk()
        self.main_board = Frame(self.root, bg="black", bd=0, width=440, height=440)
        self.red_pieces = Frame(self.root, bg="yellow", width=470, height=110, )
        self.blue_pieces = Frame(self.root, bg="yellow", width=470, height=110, )
        self.red = []
        self.blue = []
        self.red_locations = [(-1, -1) * 16]
        self.blue_locations = [(-1, -1) * 16]
        self.clicked_piece = (-1, -1)
        self.destination = (-1, -1)

    def board_on_click(self, i, j, event):
        if self.clicked_piece != (-1,-1):
            self.destination = (i, j)

    def piece_on_click(self, i, j, event, side, index):
        if side == "red":
            self.red[index].config(bg = "white")
            self.clicked_piece = ("red",index)
        else:
            self.clicked_piece = ("blue",index)

    def initialise_GUI(self):
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

        self.root.title("ZERO POINT ONE")
        self.root.geometry("1500x800")
        self.root.resizable(False, False)
        self.root.state("zoomed")

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

        self.main_board.place(relx=0.5, y=350, anchor="center")
        for i in range(8):
            for j in range(8):
                if 6 <= i <= 7:
                    square = Frame(self.main_board, height=55, width=55, bg="red")
                elif 0 <= i <= 1:
                    square = Frame(self.main_board, height=55, width=55, bg="blue")
                else:
                    square = Frame(self.main_board, height=55, width=55, bg="white")
                square.bind("<Button-1>", lambda e, i=i, j=j: self.board_on_click(i, j, e))
                square.grid(row=i, column=j, padx=1, pady=1)
        self.red_pieces.place(relx=0.5, y=650, anchor="center")
        self.blue_pieces.place(relx=0.5, y=50, anchor="center")
        rtptl1, rtptl2, rtptl3, rtptl4, rtptl5, rtptl6, rtptl7, rtptl8, rzptl1, rzptl2, rzptl3, rzptl4, ropol1, ropol2, roptl, rzpol = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.red = [rtptl1, rtptl2, rtptl3, rtptl4, rtptl5, rtptl6, rtptl7, rtptl8, rzptl1, rzptl2, rzptl3, rzptl4, ropol1,
               ropol2,
               roptl, rzpol]

        counter = 0
        for i in range(8):
            self.red[i] = Label(self.red_pieces, image=rtpt, bg="yellow")
            self.red[i].bind("<Button-1>", lambda e, i=-1, j=-1, index=i, s="red": self.piece_on_click(i, j, e, s, index))
            self.red[i].place(relx=0.126 * counter)
            counter += 1
        counter = 0
        for i in range(8, 12):
            self.red[i] = Label(self.red_pieces, image=rzpt, bg="yellow")
            self.red[i].bind("<Button-1>", lambda e, i=-1, j=-1, index=i, s="red": self.piece_on_click(i, j, e, s, index))
            self.red[i].place(relx=0.126 * counter, y=55)
            counter += 1
        counter = 0
        for i in range(12, 14):
            self.red[i] = Label(self.red_pieces, image=ropo, bg="yellow")
            self.red[i].bind("<Button-1>", lambda e, i=-1, j=-1, index=i, s="red": self.piece_on_click(i, j, e, s, index))
            self.red[i].place(relx=4 * 0.126 + 0.126 * counter, y=55)
            counter += 1
        self.red[14] = Label(self.red_pieces, image=ropt, bg="yellow")
        self.red[14].bind("<Button-1>", lambda e, i=-1, j=-1, index=14, s="red": self.piece_on_click(i, j, e, s, index))
        self.red[14].place(relx=6 * 0.126, y=55)
        self.red[15] = Label(self.red_pieces, image=rzpo, bg="yellow")
        self.red[15].bind("<Button-1>", lambda e, i=-1, j=-1, index=15, s="red": self.piece_on_click(i, j, e, s, index))
        self.red[15].place(relx=7 * 0.126, y=55)

        btptl1, btptl2, btptl3, btptl4, btptl5, btptl6, btptl7, btptl8, bzptl1, bzptl2, bzptl3, bzptl4, bopol1, bopol2, boptl, bzpol = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.blue = [btptl1, btptl2, btptl3, btptl4, btptl5, btptl6, btptl7, btptl8, bzptl1, bzptl2, bzptl3, bzptl4, bopol1,
                bopol2,
                boptl, bzpol]
        counter = 0
        for i in range(8):
            self.blue[i] = Label(self.blue_pieces, image=btpt, bg="yellow")
            self.blue[i].bind("<Button-1>", lambda e, i=-1, j=-1, index=i, s="blue": self.piece_on_click(i, j, e, s, index))
            self.blue[i].place(relx=0.126 * counter)
            counter += 1
        counter = 0
        for i in range(8, 12):
            self.blue[i] = Label(self.blue_pieces, image=bzpt, bg="yellow")
            self.blue[i].bind("<Button-1>", lambda e, i=-1, j=-1, index=i, s="blue": self.piece_on_click(i, j, e, s, index))
            self.blue[i].place(relx=0.126 * counter, y=55)
            counter += 1
        counter = 0
        for i in range(12, 14):
            self.blue[i] = Label(self.blue_pieces, image=bopo, bg="yellow")
            self.blue[i].bind("<Button-1>", lambda e, i=-1, j=-1, index=i, s="blue": self.piece_on_click(i, j, e, s, index))
            self.blue[i].place(relx=4 * 0.126 + 0.126 * counter, y=55)
            counter += 1
        self.blue[14] = Label(self.blue_pieces, image=bopt, bg="yellow")
        self.blue[14].bind("<Button-1>", lambda e, i=-1, j=-1, index=14, s="blue": self.piece_on_click(i, j, e, s, index))
        self.blue[14].place(relx=6 * 0.126, y=55)
        self.blue[15] = Label(self.blue_pieces, image=bzpo, bg="yellow")
        self.blue[15].bind("<Button-1>", lambda e, i=-1, j=-1, index=15, s="blue": self.piece_on_click(i, j, e, s, index))
        self.blue[15].place(relx=7 * 0.126, y=55)

        # blue[15].destroy()
        # blue[15] = Label(main_board, image=bzpo, bg="yellow")
        # blue[15].bind("<Button-1>", lambda e, i=-1, j=-1,index = 15, s="blue": piece_on_click(i, j, e, s,index))
        # blue[15].place(relx=0 * 0.126, y=0)
        self.root.mainloop()

    def make_move(self, side, piece, end):
        if side == "red":
            self.red[piece].destroy()
            self.red_locations[piece] = end
        else:
            self.blue[piece].destroy()
            self.blue_locations[piece] = end
