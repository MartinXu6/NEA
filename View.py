import sys
import time
from tkinter import *
import tkinter.scrolledtext as st
from PIL import Image
from PIL import ImageTk


# Class to create and manage the start menu GUI
class start_menu:
    # Initialize the start menu window and GUI components
    def __init__(self):
        # Main Tkinter window for the menu
        self.menu = Tk()
        # Set window dimensions
        self.menu.geometry("1000x600")

        # Buttons for game modes and quit option:
        # Single Player button (red) - triggers single() method
        self.single_p = Button(self.menu, text="Single Player", bg="red", height="7", width="20", command=self.single)
        # Multi Player button (blue) - triggers multi() method
        self.multi = Button(self.menu, text="Multi Player", bg="blue", height="7", width="20", command=self.multi)
        # Online Play button (yellow) - triggers online() method
        self.online = Button(self.menu, text="Play Online", bg="yellow", height="7", width="20", command=self.online)
        # Quit button (grey) - exits application
        self.quit = Button(self.menu, text="QUIT", bg="grey", height="7", width="20", command=quit)

        # Add buttons to window
        self.single_p.pack()
        self.multi.pack()
        self.online.pack()
        self.quit.pack()

        # Tracks active game mode (False = no mode selected)
        self.running = False
        # Start GUI event loop
        self.menu.mainloop()

    # Handle single player mode selection
    def single(self):
        self.menu.destroy()  # Close menu window
        self.running = "single"  # Set mode to single player

    # Handle local multiplayer mode selection
    def multi(self):
        self.menu.destroy()  # Close menu window
        self.running = "multi"  # Set mode to local multiplayer

    def online(self):
        self.menu.destroy()
        self.running = "online"


class Choosing:
    # Initialize the choosing window and UI components.
    def __init__(self):
        self.choosing = Tk()  # Create the main Tkinter window.
        self.choosing.geometry("1000x600")  # Set the window size.
        self.choice = Label(self.choosing, text="Choose your side")  # Label for side selection.
        self.red = Button(self.choosing, text="Red", bg="red", height="7", width="20", command=self.red)  # Button for choosing Red.
        self.blue = Button(self.choosing, text="Blue", bg="blue", height="7", width="20", command=self.blue)  # Button for choosing Blue.
        Side = ""
        self.choice.pack()
        self.red.pack()
        self.blue.pack()
        self.choosing.mainloop()  # Start the Tkinter event loop.

    # Handle selection of the red side.
    def red(self):
        self.choosing.destroy()
        self.Side = "red"  # Set the selected side to red.

    # Handle selection of the blue side.
    def blue(self):
        self.choosing.destroy()
        self.Side = "blue"  # Set the selected side to blue.



class online_choosing:
    def __init__(self):
        self.o_choosing = Tk()
        self.o_choosing.geometry("300x300")
        self.host_red_game = Button(self.o_choosing, text="Host Game Red", bg="grey", height="5", width="15", command=self.Host_Game_Red)
        self.host_blue_game = Button(self.o_choosing, text="Host Game Blue", bg="brown", height="5", width="15", command=self.Host_Game_Blue)
        self.join_game = Button(self.o_choosing, text="Join Game", bg="purple", height="5", width="15", command=self.Join_Game)
        self.status = ""
        self.host_red_game.pack()
        self.host_blue_game.pack()
        self.join_game.pack()
        self.o_choosing.mainloop()

    def Host_Game_Red(self):
        self.status = "host_r"
        self.o_choosing.destroy()
    def Host_Game_Blue(self):
        self.status = "host_b"
        self.o_choosing.destroy()


    def Join_Game(self):
        self.status = "join"
        self.o_choosing.destroy()


class GUI:
    def __init__(self):
        self.stored_moves = ""
        self.root = Tk()
        self.main_board = Frame(self.root, bg="black", bd=0, width=440, height=440)
        self.evaluation = Label(self.root, width=55, height=3, text="Current Evaluation", bg="grey")
        self.evaluation_red_text = Label(self.root, width=10, height=1, text="Red: 0.5")
        self.evaluation_blue_text = Label(self.root, width=10, height=1, text="Blue: 0.5")
        self.evaluation_bar = Frame(self.root, width=395, height=50)
        self.evaluation_red = Frame(self.evaluation_bar, width=395 / 2, height=50, bg="red")
        self.evaluation_blue = Frame(self.evaluation_bar, width=395 / 2, height=50, bg="blue")
        self.horizontal_cords = Frame(self.root, width=457, height=20)
        self.vertical_cords = Frame(self.root, width=20, height=457)
        self.mover_display = Label(self.root, width=10, height=30, bg="white")
        self.quit_button = Button(self.root, bg="yellow", text="QUIT", width=20, height=10, command=self.quit)
        self.moves = st.ScrolledText(self.root, width=50, height=20, )
        self.red_pieces = Frame(self.root, bg="white", width=470, height=110, )
        self.blue_pieces = Frame(self.root, bg="white", width=470, height=110, )
        self.displayed_pieces = []
        self.red = []
        self.blue = []
        self.red_locations = [(-1, -1)] * 16
        self.blue_locations = [(-1, -1)] * 16
        self.red_captured = []
        self.blue_captured = []
        self.capturing = (-1, -1, 0)
        self.captured = (-1, -1, 0)
        self.red_spots = [i for i in range(16)]
        self.blue_spots = [i for i in range(16)]
        self.red_taken_spots = [-1 for i in range(16)]
        self.blue_taken_spots = [-1 for i in range(16)]
        self.clicked_piece = (-1, -1, 0)
        self.destination = (-1, -1)
        self.piece_size = (45, 45)
        self.piece_colour = "white"
        self.rtpt = None
        self.rzpo = None
        self.ropo = None
        self.ropt = None
        self.rzpt = None
        self.btpt = None
        self.bzpt = None
        self.bopt = None
        self.bzpo = None
        self.bopo = None

    def quit(self):
        self.root.destroy()

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
        # Window configuration and title
        self.root.title("ZERO POINT ONE")
        self.root.geometry("1500x800")
        self.root.resizable(False, False)
        self.root.state("zoomed")

        # Convert image references for Tkinter compatibility
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

        # Position main UI components
        self.main_board.place(relx=0.5, y=340, anchor="center")
        self.evaluation_bar.place(relx=0.69, y=290)
        self.evaluation_red_text.place(relx=0.69, y=265)
        self.evaluation_blue_text.place(relx=0.93, y=265)
        self.evaluation_red.place(relx=0)
        self.evaluation_blue.place(relx=1, anchor="ne")
        self.evaluation.place(relx=0.69, y=210)
        self.horizontal_cords.place(relx=0.5, y=580, anchor="center")
        self.vertical_cords.place(y=340, relx=0.31, anchor="center")
        self.quit_button.place(relx=0.1, rely=0.5)
        self.mover_display.place(relx=0.24, y=115, anchor="nw")
        self.moves.place(relx=0.69, rely=0.5)
        self.moves.configure(state="disabled")

        # Create coordinate labels for board edges
        for i in range(8):
            square = Label(self.horizontal_cords, height=1, width=7, text=str(i))
            square.place(relx=i * 0.126, anchor="nw")
        for i in range(8):
            square = Label(self.vertical_cords, height=3, width=2, text=str(i))
            square.place(rely=i * 0.126, anchor="nw")

        # Generate 8x8 game board grid with click handlers
        for i in range(8):
            for j in range(8):
                if 6 <= i <= 7:
                    square = Frame(self.main_board, height=55, width=55, bg="white")
                elif 0 <= i <= 1:
                    square = Frame(self.main_board, height=55, width=55, bg="white")
                else:
                    square = Frame(self.main_board, height=55, width=55, bg="white")
                square.bind("<Button-1>", lambda e, i=i, j=j: self.board_on_click(i, j, e))
                square.grid(row=i, column=j, padx=1, pady=1)

        # Position piece containers below/above main board
        self.red_pieces.place(relx=0.5, y=650, anchor="center")
        self.blue_pieces.place(relx=0.5, y=50, anchor="center")

        # Initialize red piece tracking list
        rtptl1, rtptl2, rtptl3, rtptl4, rtptl5, rtptl6, rtptl7, rtptl8, rzptl1, rzptl2, rzptl3, rzptl4, ropol1, ropol2, roptl, rzpol = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.red = [rtptl1, rtptl2, rtptl3, rtptl4, rtptl5, rtptl6, rtptl7, rtptl8, rzptl1, rzptl2, rzptl3, rzptl4,
                    ropol1,
                    ropol2,
                    roptl, rzpol]

        # Create first row of red pieces
        counter = 0
        for i in range(8):
            self.red[i] = Label(self.red_pieces, image=self.rtpt, bg=self.piece_colour)
            self.red[i].bind("<Button-1>",
                             lambda e, i=-1, j=-1, index=i, s="red": self.piece_on_click(i, j, e, s, index))
            self.red[i].place(relx=0.126 * counter)
            counter += 1

        # Second row of red pieces
        counter = 0
        for i in range(8, 12):
            self.red[i] = Label(self.red_pieces, image=self.rzpt, bg=self.piece_colour)
            self.red[i].bind("<Button-1>",
                             lambda e, i=-1, j=-1, index=i, s="red": self.piece_on_click(i, j, e, s, index))
            self.red[i].place(relx=0.126 * counter, y=55)
            counter += 1

        # Special red pieces
        counter = 0
        for i in range(12, 14):
            self.red[i] = Label(self.red_pieces, image=self.ropo, bg=self.piece_colour)
            self.red[i].bind("<Button-1>",
                             lambda e, i=-1, j=-1, index=i, s="red": self.piece_on_click(i, j, e, s, index))
            self.red[i].place(relx=4 * 0.126 + 0.126 * counter, y=55)
            counter += 1

        # Final red special pieces
        self.red[14] = Label(self.red_pieces, image=self.ropt, bg=self.piece_colour)
        self.red[14].bind("<Button-1>", lambda e, i=-1, j=-1, index=14, s="red": self.piece_on_click(i, j, e, s, index))
        self.red[14].place(relx=6 * 0.126, y=55)
        self.red[15] = Label(self.red_pieces, image=self.rzpo, bg=self.piece_colour)
        self.red[15].bind("<Button-1>", lambda e, i=-1, j=-1, index=15, s="red": self.piece_on_click(i, j, e, s, index))
        self.red[15].place(relx=7 * 0.126, y=55)

        # Initialize blue piece tracking list
        btptl1, btptl2, btptl3, btptl4, btptl5, btptl6, btptl7, btptl8, bzptl1, bzptl2, bzptl3, bzptl4, bopol1, bopol2, boptl, bzpol = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.blue = [btptl1, btptl2, btptl3, btptl4, btptl5, btptl6, btptl7, btptl8, bzptl1, bzptl2, bzptl3, bzptl4,
                     bopol1,
                     bopol2,
                     boptl, bzpol]

        # Create first row of blue pieces
        counter = 0
        for i in range(8):
            self.blue[i] = Label(self.blue_pieces, image=self.btpt, bg=self.piece_colour)
            self.blue[i].bind("<Button-1>",
                              lambda e, i=-1, j=-1, index=i, s="blue": self.piece_on_click(i, j, e, s, index))
            self.blue[i].place(relx=0.126 * counter)
            counter += 1

        # Second row of blue pieces
        counter = 0
        for i in range(8, 12):
            self.blue[i] = Label(self.blue_pieces, image=self.bzpt, bg=self.piece_colour)
            self.blue[i].bind("<Button-1>",
                              lambda e, i=-1, j=-1, index=i, s="blue": self.piece_on_click(i, j, e, s, index))
            self.blue[i].place(relx=0.126 * counter, y=55)
            counter += 1

        # Special blue pieces
        counter = 0
        for i in range(12, 14):
            self.blue[i] = Label(self.blue_pieces, image=self.bopo, bg=self.piece_colour)
            self.blue[i].bind("<Button-1>",
                              lambda e, i=-1, j=-1, index=i, s="blue": self.piece_on_click(i, j, e, s, index))
            self.blue[i].place(relx=4 * 0.126 + 0.126 * counter, y=55)
            counter += 1

        # Final blue special pieces
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
        previous_colour = self.mover_display.cget("bg")
        self.mover_display.config(bg="red") if previous_colour == "blue" else self.mover_display.config(bg="blue")
        if side == "red":
            previous_image = self.blue[piece].cget("image")
            self.blue[piece].destroy()
            self.blue.pop(piece)
            new_piece = Label(self.main_board, image=previous_image, bg="white")
            new_piece.bind("<Button-1>",
                           lambda e, i=-1, j=-1, index=piece, s="red": self.captured_on_click(i, j, e, s, index))
            self.blue.insert(piece, new_piece)
            self.blue[piece].place(x=5+57*end[1], y=403-57*(7-end[0]))
            self.blue_locations[piece] = end
            self.red_spots.append(self.blue_taken_spots[piece])
            self.blue_taken_spots[piece] = -1
        else:
            previous_image = self.red[piece].cget("image")
            self.red[piece].destroy()
            self.red.pop(piece)
            new_piece = Label(self.main_board, image=previous_image, bg="white")
            new_piece.bind("<Button-1>",
                           lambda e, i=-1, j=-1, index=piece, s="blue": self.captured_on_click(i, j, e, s, index))
            self.red.insert(piece, new_piece)
            self.red[piece].place(x=5+57*end[1], y=403-57*(7-end[0]))
            self.red_locations[piece] = end
            self.blue_spots.append(self.red_taken_spots[piece])
            self.red_taken_spots[piece] = -1

    def make_deploy(self, side, piece, end):
        if side == "red":
            previous_image = self.red[piece].cget("image")
            self.red[piece].destroy()
            self.red.pop(piece)
            new_piece = Label(self.main_board, image=previous_image, bg="white")
            new_piece.bind("<Button-1>",
                           lambda e, i=-1, j=-1, index=piece, s="red": self.piece_on_click(i, j, e, s, index))
            self.red.insert(piece, new_piece)
            self.red[piece].place(x=5+57*end[1], y=403-57*(7-end[0]))
            self.red_locations[piece] = end
            if self.red_taken_spots[piece] != -1:
                self.red_spots.append(self.red_taken_spots[piece])
                self.red_taken_spots[piece] = -1
        else:
            previous_image = self.blue[piece].cget("image")
            self.blue[piece].destroy()
            self.blue.pop(piece)
            new_piece = Label(self.main_board, image=previous_image, bg="white")
            new_piece.bind("<Button-1>",
                           lambda e, i=-1, j=-1, index=piece, s="blue": self.piece_on_click(i, j, e, s, index))
            self.blue.insert(piece, new_piece)
            self.blue[piece].place(x=5+57*end[1], y=403-57*(7-end[0]))
            self.blue_locations[piece] = end
            if self.blue_taken_spots[piece] != -1:
                self.blue_spots.append(self.blue_taken_spots[piece])
                self.blue_taken_spots[piece] = -1

    def make_move(self, side, piece, end, CAPTURED):
        previous_colour = self.mover_display.cget("bg")
        self.mover_display.config(bg="red") if previous_colour == "blue" else self.mover_display.config(bg="blue")
        if side == "red":
            if CAPTURED == 0:
                previous_image = self.red[piece].cget("image")
                self.red[piece].destroy()
                self.red.pop(piece)
                new_piece = Label(self.main_board, image=previous_image, bg="white")
                new_piece.bind("<Button-1>",
                               lambda e, i=-1, j=-1, index=piece, s="red": self.piece_on_click(i, j, e, s, index))
                self.red.insert(piece, new_piece)
                self.red[piece].place(x=5+57*end[1], y=403-57*(7-end[0]))
                self.red_locations[piece] = end
            else:
                previous_image = self.blue[piece].cget("image")
                self.blue[piece].destroy()
                self.blue.pop(piece)
                new_piece = Label(self.main_board, image=previous_image, bg="white")
                new_piece.bind("<Button-1>",
                               lambda e, i=-1, j=-1, index=piece, s="red": self.captured_on_click(i, j, e, s, index))
                self.blue.insert(piece, new_piece)
                self.blue[piece].place(x=5+57*end[1], y=403-57*(7-end[0]))
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
                self.blue[piece].place(x=5+57*end[1], y=403-57*(7-end[0]))
                self.blue_locations[piece] = end
            else:
                previous_image = self.red[piece].cget("image")
                self.red[piece].destroy()
                self.red.pop(piece)
                new_piece = Label(self.main_board, image=previous_image, bg="white")
                new_piece.bind("<Button-1>",
                               lambda e, i=-1, j=-1, index=piece, s="blue": self.captured_on_click(i, j, e, s, index))
                self.red.insert(piece, new_piece)
                self.red[piece].place(x=5+57*end[1], y=403-57*(7-end[0]))
                self.red_locations[piece] = end

    def display_movable(self, movable):
        for place in movable:
            new_label = Label(self.main_board, bg="black", height=1, width=2)
            new_label.bind("<Button-1>", lambda e, i=place[0], j=place[1]: self.board_on_click(i, j, e))
            print(place[0],place[1])
            new_label.place(x=19+57*place[1], y=415-57*(7-place[0]) )
            self.displayed_pieces.append(new_label)

    def got_captured(self, side, index, reverse_captured):
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
            spot = min(self.blue_spots)
            self.blue_spots.remove(spot)
            if reverse_captured:
                self.blue_taken_spots[index] = spot
            else:
                self.red_taken_spots[index] = spot
        else:
            spot = min(self.red_spots)
            self.red_spots.remove(spot)
            if reverse_captured:
                self.red_taken_spots[index] = spot
            else:
                self.blue_taken_spots[index] = spot
        if spot > 7:
            spot -= 8
            new_piece.place(relx=0.126 * spot, y=55)
        else:
            new_piece.place(relx=0.126 * spot, y=0)

    def save(self):
        print(self.stored_moves)
        self.new.destroy()
        quit()

    def game_won(self, side):
        if side == "red":
            Game_over = Label(self.root, text=f"GAME OVER RED WON!", height=10, width=20, font=50, bg="red")
        else:
            Game_over = Label(self.root, text=f"GAME OVER BLUE WON!", height=10, width=20, font=50, bg="blue")
        self.stored_moves = self.moves.get('1.0', END)
        Game_over.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.root.update()
        time.sleep(2)
        self.root.destroy()
        self.new = Tk()
        self.new.geometry("500x500")
        save = Button(self.new, text="Save Game", width=10, height=5, bg="grey", command=self.save)
        save.place(relx=0.5, rely=0.3, anchor="center")
        while True:
            self.new.update()
        # quit()
