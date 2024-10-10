import time
from tkinter import *
from PIL import Image
from PIL import ImageTk
import model



class start_menu:
    def __init__(self):
        self.menu = Tk()
        self.menu.geometry("1000x600")
        self.single = Button(self.menu, text="Single Player", bg="red", height="10", width="20", command=self.single)
        self.multi = Button(self.menu, text="Multi Player", bg="blue", height="10", width="20", command=self.multi)
        self.quit = Button(self.menu, text="QUIT", bg="grey", height="10", width="20", command=quit)
        self.single.pack()
        self.multi.pack()
        self.quit.pack()
        self.running = False
        self.menu.mainloop()

    def single(self):
        self.menu.destroy()
        self.running = "single"

    def multi(self):
        self.menu.destroy()
        self.running = "multi"


class GUI:
    def __init__(self):
        self.root = Tk()
        self.main_board = Frame(self.root, bg="black", bd=0, width=440, height=440)
        self.red_pieces = Frame(self.root, bg="yellow", width=470, height=110, )
        self.blue_pieces = Frame(self.root, bg="yellow", width=470, height=110, )
        self.displayed_pieces = []
        self.red = []
        self.blue = []
        self.red_locations = [(-1, -1)] * 16
        self.blue_locations = [(-1, -1)] * 16
        self.red_captured = []
        self.blue_captured = []
        self.capturing = (-1, -1, 0)
        self.captured = (-1, -1, 0)

        self.clicked_piece = (-1, -1, 0)
        self.destination = (-1, -1)
        self.piece_size = (45, 45)
        self.piece_colour = "white"
        self.rtpt = Image.open("Images/Pieces/r2.2.png")
        self.rtpt = self.rtpt.resize(self.piece_size)
        self.rzpo = Image.open("Images/Pieces/r0.1.png")
        self.rzpo = self.rzpo.resize(self.piece_size)
        self.ropo = Image.open("Images/Pieces/r1.1.png")
        self.ropo = self.ropo.resize(self.piece_size)
        self.ropt = Image.open("Images/Pieces/r1.2.png")
        self.ropt = self.ropt.resize(self.piece_size)
        self.rzpt = Image.open("Images/Pieces/r0.2.png")
        self.rzpt = self.rzpt.resize(self.piece_size)
        self.btpt = Image.open("Images/Pieces/b2.2.png")
        self.btpt = self.btpt.resize(self.piece_size)
        self.bzpt = Image.open("Images/Pieces/b0.2.png")
        self.bzpt = self.bzpt.resize(self.piece_size)
        self.bopt = Image.open("Images/Pieces/b1.2.png")
        self.bopt = self.bopt.resize(self.piece_size)
        self.bzpo = Image.open("Images/Pieces/b0.1.png")
        self.bzpo = self.bzpo.resize(self.piece_size)
        self.bopo = Image.open("Images/Pieces/b1.1.png")
        self.bopo = self.bopo.resize(self.piece_size)

    def board_on_click(self, i, j, event):
        if self.clicked_piece[0] != -1 and self.clicked_piece[1] != -1:
            self.destination = (i, j)
            if self.clicked_piece[0] == "red":
                for location in range(len(self.blue_locations)):
                    if self.blue_locations[location] == (i, j):
                        self.destination = (-1, -1)
                        self.capturing = (self.clicked_piece[0], self.clicked_piece[1], self.clicked_piece[2])
                        self.captured = ("blue", location, 0)
                        self.clicked_piece = (-1, -1, 0)
                        break
                else:
                    for location in range(len(self.red_captured)):
                        if self.red_locations[self.red_captured[location]] == (i, j):
                            self.destination = (-1, -1)
                            self.capturing = (self.clicked_piece[0], self.clicked_piece[1], self.clicked_piece[2])
                            self.captured = ("red", self.red_captured[location], 1)
                            self.clicked_piece = (-1, -1, 0)
                            break

            elif self.clicked_piece[0] == "blue":
                for location in range(len(self.red_locations)):
                    if self.red_locations[location] == (i, j):
                        self.destination = (-1, -1)
                        self.capturing = (self.clicked_piece[0], self.clicked_piece[1], self.clicked_piece[2])
                        self.captured = ("red", location, 0)
                        self.clicked_piece = (-1, -1, 0)
                        break
                else:
                    for location in range(len(self.blue_captured)):
                        if self.blue_locations[self.blue_captured[location]] == (i, j):
                            self.destination = (-1, -1)
                            self.capturing = (self.clicked_piece[0], self.clicked_piece[1], self.clicked_piece[2])
                            self.captured = ("blue", self.blue_captured[location], 1)
                            self.clicked_piece = (-1, -1, 0)
                            break

    def piece_on_click(self, i, j, event, side, index):
        if side == "red":
            if self.clicked_piece[0] == -1 and self.clicked_piece[1] == -1:
                self.clicked_piece = ("red", index, 0)
            else:
                if self.clicked_piece[0] == "red":
                    if self.clicked_piece[2] == 0:
                        self.red[self.clicked_piece[1]].config(bg="white")
                    elif self.clicked_piece[2] == 1:
                        self.blue[self.clicked_piece[1]].config(bg="white")
                    self.clicked_piece = (-1, -1, 0)
                    for i in self.displayed_pieces:
                        i.destroy()
                        self.displayed_pieces = []
                else:
                    self.capturing = (self.clicked_piece[0], self.clicked_piece[1], self.clicked_piece[2])
                    self.captured = (side, index, 0)
                    if self.clicked_piece[2] == 0:
                        self.blue[self.clicked_piece[1]].config(bg="white")
                    elif self.clicked_piece[2] == 1:
                        self.red[self.clicked_piece[1]].config(bg="white")
                    self.clicked_piece = (-1, -1, 0)
                    for i in self.displayed_pieces:
                        i.destroy()
                        self.displayed_pieces = []
        else:
            if self.clicked_piece[0] == -1 and self.clicked_piece[1] == -1:
                self.clicked_piece = ("blue", index, 0)
            else:
                if self.clicked_piece[0] == "blue":
                    if self.clicked_piece[2] == 0:
                        self.blue[self.clicked_piece[1]].config(bg="white")
                    elif self.clicked_piece[2] == 1:
                        self.red[self.clicked_piece[1]].config(bg="white")
                    self.clicked_piece = (-1, -1, 0)
                    for i in self.displayed_pieces:
                        i.destroy()
                        self.displayed_pieces = []
                else:
                    self.capturing = (self.clicked_piece[0], self.clicked_piece[1], self.clicked_piece[2])
                    self.captured = (side, index, 0)
                    if self.clicked_piece[2] == 0:
                        self.red[self.clicked_piece[1]].config(bg="white")
                    elif self.clicked_piece[2] == 1:
                        self.blue[self.clicked_piece[1]].config(bg="white")
                    self.clicked_piece = (-1, -1, 0)
                    for i in self.displayed_pieces:
                        i.destroy()
                        self.displayed_pieces = []

    def captured_on_click(self, i, j, event, side, index):
        if side == "red":
            if self.clicked_piece[0] == -1 and self.clicked_piece[1] == -1:
                self.clicked_piece = ("red", index, 1)
            else:
                if self.clicked_piece[0] == "red":
                    if self.clicked_piece[2] == 0:
                        self.red[self.clicked_piece[1]].config(bg="white")
                    elif self.clicked_piece[2] == 1:
                        self.blue[self.clicked_piece[1]].config(bg="white")
                    self.clicked_piece = (-1, -1, 0)
                    for i in self.displayed_pieces:
                        i.destroy()
                        self.displayed_pieces = []
                else:
                    self.capturing = (self.clicked_piece[0], self.clicked_piece[1], self.clicked_piece[2])
                    self.captured = (side, index, 1)
                    if self.clicked_piece[2] == 0:
                        self.blue[self.clicked_piece[1]].config(bg="white")
                    elif self.clicked_piece[2] == 1:
                        self.red[self.clicked_piece[1]].config(bg="white")
                    self.clicked_piece = (-1, -1, 0)
                    for i in self.displayed_pieces:
                        i.destroy()
                        self.displayed_pieces = []
        else:
            if self.clicked_piece[0] == -1 and self.clicked_piece[1] == -1:
                self.clicked_piece = ("blue", index, 1)
            else:
                if self.clicked_piece[0] == "blue":
                    if self.clicked_piece[2] == 0:
                        self.blue[self.clicked_piece[1]].config(bg="white")
                    elif self.clicked_piece[2] == 1:
                        self.red[self.clicked_piece[1]].config(bg="white")
                    self.clicked_piece = (-1, -1, 0)
                    for i in self.displayed_pieces:
                        i.destroy()
                        self.displayed_pieces = []
                else:
                    self.capturing = (self.clicked_piece[0], self.clicked_piece[1], self.clicked_piece[2])
                    self.captured = (side, index, 1)
                    if self.clicked_piece[2] == 0:
                        self.red[self.clicked_piece[1]].config(bg="white")
                    elif self.clicked_piece[2] == 1:
                        self.blue[self.clicked_piece[1]].config(bg="white")
                    self.clicked_piece = (-1, -1, 0)
                    for i in self.displayed_pieces:
                        i.destroy()
                        self.displayed_pieces = []

    def initialise_GUI(self):

        self.root.title("ZERO POINT ONE")
        self.root.geometry("1500x800")
        self.root.resizable(False, False)
        self.root.state("zoomed")

        self.rtpt = ImageTk.PhotoImage(self.rtpt)
        self.rzpo = ImageTk.PhotoImage(self.rzpo)
        self.rzpt = ImageTk.PhotoImage(self.rzpt)
        self.ropo = ImageTk.PhotoImage(self.ropo)
        self.ropt = ImageTk.PhotoImage(self.ropt)
        self.btpt = ImageTk.PhotoImage(self.btpt)
        self.bzpo = ImageTk.PhotoImage(self.bzpo)
        self.bzpt = ImageTk.PhotoImage(self.bzpt)
        self.bopo = ImageTk.PhotoImage(self.bopo)
        self.bopt = ImageTk.PhotoImage(self.bopt)

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
        self.red = [rtptl1, rtptl2, rtptl3, rtptl4, rtptl5, rtptl6, rtptl7, rtptl8, rzptl1, rzptl2, rzptl3, rzptl4,
                    ropol1,
                    ropol2,
                    roptl, rzpol]

        counter = 0
        for i in range(8):
            self.red[i] = Label(self.red_pieces, image=self.rtpt, bg=self.piece_colour)
            self.red[i].bind("<Button-1>",
                             lambda e, i=-1, j=-1, index=i, s="red": self.piece_on_click(i, j, e, s, index))
            self.red[i].place(relx=0.126 * counter)
            counter += 1
        counter = 0
        for i in range(8, 12):
            self.red[i] = Label(self.red_pieces, image=self.rzpt, bg=self.piece_colour)
            self.red[i].bind("<Button-1>",
                             lambda e, i=-1, j=-1, index=i, s="red": self.piece_on_click(i, j, e, s, index))
            self.red[i].place(relx=0.126 * counter, y=55)
            counter += 1
        counter = 0
        for i in range(12, 14):
            self.red[i] = Label(self.red_pieces, image=self.ropo, bg=self.piece_colour)
            self.red[i].bind("<Button-1>",
                             lambda e, i=-1, j=-1, index=i, s="red": self.piece_on_click(i, j, e, s, index))
            self.red[i].place(relx=4 * 0.126 + 0.126 * counter, y=55)
            counter += 1
        self.red[14] = Label(self.red_pieces, image=self.ropt, bg=self.piece_colour)
        self.red[14].bind("<Button-1>", lambda e, i=-1, j=-1, index=14, s="red": self.piece_on_click(i, j, e, s, index))
        self.red[14].place(relx=6 * 0.126, y=55)
        self.red[15] = Label(self.red_pieces, image=self.rzpo, bg=self.piece_colour)
        self.red[15].bind("<Button-1>", lambda e, i=-1, j=-1, index=15, s="red": self.piece_on_click(i, j, e, s, index))
        self.red[15].place(relx=7 * 0.126, y=55)

        btptl1, btptl2, btptl3, btptl4, btptl5, btptl6, btptl7, btptl8, bzptl1, bzptl2, bzptl3, bzptl4, bopol1, bopol2, boptl, bzpol = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.blue = [btptl1, btptl2, btptl3, btptl4, btptl5, btptl6, btptl7, btptl8, bzptl1, bzptl2, bzptl3, bzptl4,
                     bopol1,
                     bopol2,
                     boptl, bzpol]
        counter = 0
        for i in range(8):
            self.blue[i] = Label(self.blue_pieces, image=self.btpt, bg=self.piece_colour)
            self.blue[i].bind("<Button-1>",
                              lambda e, i=-1, j=-1, index=i, s="blue": self.piece_on_click(i, j, e, s, index))
            self.blue[i].place(relx=0.126 * counter)
            counter += 1
        counter = 0
        for i in range(8, 12):
            self.blue[i] = Label(self.blue_pieces, image=self.bzpt, bg=self.piece_colour)
            self.blue[i].bind("<Button-1>",
                              lambda e, i=-1, j=-1, index=i, s="blue": self.piece_on_click(i, j, e, s, index))
            self.blue[i].place(relx=0.126 * counter, y=55)
            counter += 1
        counter = 0
        for i in range(12, 14):
            self.blue[i] = Label(self.blue_pieces, image=self.bopo, bg=self.piece_colour)
            self.blue[i].bind("<Button-1>",
                              lambda e, i=-1, j=-1, index=i, s="blue": self.piece_on_click(i, j, e, s, index))
            self.blue[i].place(relx=4 * 0.126 + 0.126 * counter, y=55)
            counter += 1
        self.blue[14] = Label(self.blue_pieces, image=self.bopt, bg=self.piece_colour)
        self.blue[14].bind("<Button-1>",
                           lambda e, i=-1, j=-1, index=14, s="blue": self.piece_on_click(i, j, e, s, index))
        self.blue[14].place(relx=6 * 0.126, y=55)
        self.blue[15] = Label(self.blue_pieces, image=self.bzpo, bg=self.piece_colour)
        self.blue[15].bind("<Button-1>",
                           lambda e, i=-1, j=-1, index=15, s="blue": self.piece_on_click(i, j, e, s, index))
        self.blue[15].place(relx=7 * 0.126, y=55)

        # self.blue[15].destroy()
        # blue[15] = Label(main_board, image=bzpo, bg="yellow")
        # blue[15].bind("<Button-1>", lambda e, i=-1, j=-1,index = 15, s="blue": piece_on_click(i, j, e, s,index))
        # blue[15].place(relx=0 * 0.126, y=0)

    def captured_deploy(self, side, piece, end):
        if side == "red":
            previous_image = self.blue[piece].cget("image")
            self.blue[piece].destroy()
            self.blue.pop(piece)
            new_piece = Label(self.main_board, image=previous_image, bg="white")
            new_piece.bind("<Button-1>",
                           lambda e, i=-1, j=-1, index=piece, s="red": self.captured_on_click(i, j, e, s, index))
            self.blue.insert(piece, new_piece)
            self.blue[piece].place(relx=0.127 * end[1], rely=0.126 * end[0])
            self.blue_locations[piece] = end
        else:
            previous_image = self.red[piece].cget("image")
            self.red[piece].destroy()
            self.red.pop(piece)
            new_piece = Label(self.main_board, image=previous_image, bg="white")
            new_piece.bind("<Button-1>",
                           lambda e, i=-1, j=-1, index=piece, s="blue": self.captured_on_click(i, j, e, s, index))
            self.red.insert(piece, new_piece)
            self.red[piece].place(relx=0.127 * end[1], rely=0.126 * end[0])
            self.red_locations[piece] = end

    def make_deploy(self, side, piece, end):
        if side == "red":
            previous_image = self.red[piece].cget("image")
            self.red[piece].destroy()
            self.red.pop(piece)
            new_piece = Label(self.main_board, image=previous_image, bg="white")
            new_piece.bind("<Button-1>",
                           lambda e, i=-1, j=-1, index=piece, s="red": self.piece_on_click(i, j, e, s, index))
            self.red.insert(piece, new_piece)
            self.red[piece].place(relx=0.127 * end[1], rely=0.126 * end[0])
            self.red_locations[piece] = end
        else:
            previous_image = self.blue[piece].cget("image")
            self.blue[piece].destroy()
            self.blue.pop(piece)
            new_piece = Label(self.main_board, image=previous_image, bg="white")
            new_piece.bind("<Button-1>",
                           lambda e, i=-1, j=-1, index=piece, s="blue": self.piece_on_click(i, j, e, s, index))
            self.blue.insert(piece, new_piece)
            self.blue[piece].place(relx=0.127 * end[1], rely=0.126 * end[0])
            self.blue_locations[piece] = end

    def make_move(self, side, piece, end, CAPTURED):
        if side == "red":
            if CAPTURED == 0:
                previous_image = self.red[piece].cget("image")
                self.red[piece].destroy()
                self.red.pop(piece)
                new_piece = Label(self.main_board, image=previous_image, bg="white")
                new_piece.bind("<Button-1>",
                               lambda e, i=-1, j=-1, index=piece, s="red": self.piece_on_click(i, j, e, s, index))
                self.red.insert(piece, new_piece)
                self.red[piece].place(relx=0.127 * end[1], rely=0.126 * end[0])
                self.red_locations[piece] = end
            else:
                previous_image = self.blue[piece].cget("image")
                self.blue[piece].destroy()
                self.blue.pop(piece)
                new_piece = Label(self.main_board, image=previous_image, bg="white")
                new_piece.bind("<Button-1>",
                               lambda e, i=-1, j=-1, index=piece, s="red": self.captured_on_click(i, j, e, s, index))
                self.blue.insert(piece, new_piece)
                self.blue[piece].place(relx=0.127 * end[1], rely=0.126 * end[0])
                self.blue_locations[piece] = end
        else:
            if CAPTURED == 0:
                previous_image = self.blue[piece].cget("image")
                self.blue[piece].destroy()
                self.blue.pop(piece)
                new_piece = Label(self.main_board, image=previous_image, bg="white")
                new_piece.bind("<Button-1>",
                               lambda e, i=-1, j=-1, index=piece, s="blue": self.piece_on_click(i, j, e, s, index))
                self.blue.insert(piece, new_piece)
                self.blue[piece].place(relx=0.127 * end[1], rely=0.126 * end[0])
                self.blue_locations[piece] = end
            else:
                previous_image = self.red[piece].cget("image")
                self.red[piece].destroy()
                self.red.pop(piece)
                new_piece = Label(self.main_board, image=previous_image, bg="white")
                new_piece.bind("<Button-1>",
                               lambda e, i=-1, j=-1, index=piece, s="blue": self.captured_on_click(i, j, e, s, index))
                self.red.insert(piece, new_piece)
                self.red[piece].place(relx=0.127 * end[1], rely=0.126 * end[0])
                self.red_locations[piece] = end

    def display_movable(self, movable):
        for place in movable:
            new_label = Label(self.main_board, bg="black", height=1, width=1)
            new_label.bind("<Button-1>", lambda e, i=place[0], j=place[1]: self.board_on_click(i, j, e))
            new_label.place(relx=0.14 * place[1], rely=0.130 * place[0], )
            self.displayed_pieces.append(new_label)

    def got_captured(self, side, index, captured, CAPTURED, reverse_captured):
        if side == "red":
            if 0 <= index <= 7:
                new_image = self.btpt
            elif 8 <= index <= 11:
                new_image = self.bzpt
            elif 12 <= index <= 13:
                new_image = self.bopo
            elif index == 14:
                new_image = self.bopt
            elif index == 15:
                return
        elif side == "blue":
            if 0 <= index <= 7:
                new_image = self.rtpt
            elif 8 <= index <= 11:
                new_image = self.rzpt
            elif 12 <= index <= 13:
                new_image = self.ropo
            elif index == 14:
                new_image = self.ropt
            elif index == 15:
                return
        if side == "red":
            new_piece = Label(self.blue_pieces, image=new_image, bg="white")
            if reverse_captured:
                self.blue.pop(index)
                self.blue.insert(index, new_piece)
                self.blue_captured.remove(index)
            else:
                self.red.pop(index)
                self.red.insert(index, new_piece)
                self.red_captured.append(index)
            if reverse_captured:
                new_piece.bind("<Button-1>",
                               lambda e, i=-1, j=-1, index=index, s="blue": self.piece_on_click(i, j, e, s, index))
            else:
                new_piece.bind("<Button-1>",
                               lambda e, i=-1, j=-1, index=index, s="blue": self.captured_on_click(i, j, e, s, index))
        else:
            new_piece = Label(self.red_pieces, image=new_image, bg="white")
            if reverse_captured:
                self.red.pop(index)
                self.red.insert(index, new_piece)
                self.red_captured.remove(index)
            else:
                self.blue.pop(index)
                self.blue.insert(index, new_piece)
                self.blue_captured.append(index)
            if reverse_captured:
                new_piece.bind("<Button-1>",
                               lambda e, i=-1, j=-1, index=index, s="red": self.piece_on_click(i, j, e, s, index))
            else:
                new_piece.bind("<Button-1>",
                               lambda e, i=-1, j=-1, index=index, s="red": self.captured_on_click(i, j, e, s, index))
        if side == "blue":
            if reverse_captured:
                self.red_locations[index] = (-1, -1)
            else:
                self.blue_locations[index] = (-1, -1)
        else:
            if reverse_captured:
                self.blue_locations[index] = (-1, -1)
            else:
                self.red_locations[index] = (-1, -1)
        if side == "red":
            if reverse_captured:
                length = len([1 for i in range(16) if self.blue_locations[i] == (-1, -1)])
            else:
                length = len([1 for i in range(16) if self.red_locations[i] == (-1, -1)])
        else:
            if reverse_captured:
                length = len([1 for i in range(16) if self.red_locations[i] == (-1, -1)])
            else:
                length = len([1 for i in range(16) if self.blue_locations[i] == (-1, -1)])
        if length > 8:
            length -= 8
            new_piece.place(relx=0.126 * (length - 1), y=55)
        else:
            new_piece.place(relx=0.126 * (length - 1), y=0)

    def game_won(self, side):
        if side == "red":
            Game_over = Label(self.root, text=f"GAME OVER RED WON!", height=25, width=50, font=500, bg="red")
        else:
            Game_over = Label(self.root, text=f"GAME OVER BLUE WON!", height=25, width=50, font=500, bg="blue")
        Game_over.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.root.update()
        time.sleep(3)
        pls = Label(self.root, text="SIR CAN I PLEASE GET AN A*!!!", height = 25, width = 50, font = 500, bg = "yellow")
        pls.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.root.update()
        time.sleep(1)
        pls.destroy()
        self.root.update()
        time.sleep(2)
        quit()
