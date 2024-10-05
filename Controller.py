import View
import model
import pprint
import copy
from tkinter import *
from random import randint

gui = View.GUI()
gui.initialise_GUI()
Game = model.game()
colours = ["red", "blue", "green", "white"]

# gui.root.wm_attributes("-transparentcolor", colours[randint(0,3)])
# gui.root.update()
while True:
    # red deployment cycle
    red_deployed_index = []
    red_deployable = [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7),
                      (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]
    blue_deployed_index = []
    blue_deployable = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                       (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]
    while True:
        gui.root.update()
        if gui.clicked_piece != (-1, -1):
            if gui.clicked_piece[0] == "red" and gui.clicked_piece[1] not in red_deployed_index:
                gui.red[gui.clicked_piece[1]].config(bg="black")
                gui.display_movable(red_deployable)
                if gui.destination != (-1, -1):
                    if Game.deploy(Game.reds[gui.clicked_piece[1]], gui.destination):
                        for i in gui.displayed_pieces:
                            i.destroy()
                            gui.displayed_pieces = []
                        gui.make_deploy(gui.clicked_piece[0], gui.clicked_piece[1], gui.destination)
                        red_deployed_index.append(gui.clicked_piece[1])
                        red_deployable.remove(gui.destination)
                        gui.destination = (-1, -1)
                        gui.clicked_piece = (-1, -1)
                    else:
                        gui.red[gui.clicked_piece[1]].config(bg="white")
                        for i in gui.displayed_pieces:
                            i.destroy()
                            gui.displayed_pieces = []
                        gui.clicked_piece = (-1, -1)
                        gui.destination = (-1, -1)
            else:
                gui.clicked_piece = (-1, -1)
        if len(red_deployed_index) == 16:
            break
    # blue deployment cycle
    while True:
        gui.root.update()
        if gui.clicked_piece != (-1, -1):
            if gui.clicked_piece[0] == "blue" and gui.clicked_piece[1] not in blue_deployed_index:
                gui.blue[gui.clicked_piece[1]].config(bg="black")
                gui.display_movable(blue_deployable)
                if gui.destination != (-1, -1):
                    if Game.deploy(Game.blues[gui.clicked_piece[1]], gui.destination):
                        for i in gui.displayed_pieces:
                            i.destroy()
                            gui.displayed_pieces = []
                        gui.make_deploy(gui.clicked_piece[0], gui.clicked_piece[1], gui.destination)
                        blue_deployed_index.append(gui.clicked_piece[1])
                        blue_deployable.remove(gui.destination)
                        gui.destination = (-1, -1)
                        gui.clicked_piece = (-1, -1)
                    else:
                        gui.blue[gui.clicked_piece[1]].config(bg="white")
                        for i in gui.displayed_pieces:
                            i.destroy()
                            gui.displayed_pieces = []
                        gui.clicked_piece = (-1, -1)
                        gui.destination = (-1, -1)
            else:
                gui.clicked_piece = (-1, -1)
        if len(blue_deployed_index) == 16:
            break

    Game.deployed = True
    while True:
        # red move cycle
        while True:
            gui.root.update()
            if gui.clicked_piece != (-1, -1):
                if gui.clicked_piece[0] == "red":
                    gui.red[gui.clicked_piece[1]].config(bg="black")
                    red_movable = Game.reds[gui.clicked_piece[1]].movable(Game.board)
                    gui.display_movable(red_movable)
                    if gui.destination != (-1, -1):
                        if Game.move(Game.reds[gui.clicked_piece[1]], gui.destination, "red"):
                            for i in gui.displayed_pieces:
                                i.destroy()
                                gui.displayed_pieces = []
                            gui.make_move(gui.clicked_piece[0], gui.clicked_piece[1], gui.destination)
                            gui.destination = (-1, -1)
                            gui.clicked_piece = (-1, -1)
                            break
                        else:
                            gui.red[gui.clicked_piece[1]].config(bg="white")
                            for i in gui.displayed_pieces:
                                i.destroy()
                                gui.displayed_pieces = []
                            gui.clicked_piece = (-1, -1)
                            gui.destination = (-1, -1)
                else:
                    gui.clicked_piece = (-1, -1)
            else:
                if gui.captured != (-1, -1) and gui.capturing != (-1, -1):
                    if gui.capturing[0] == "red":
                        if Game.move(Game.reds[gui.capturing[1]], gui.blue_locations[gui.captured[1]], "red"):
                            for i in gui.displayed_pieces:
                                i.destroy()
                                gui.displayed_pieces = []
                            gui.blue[gui.captured[1]].destroy()
                            gui.make_move(gui.capturing[0], gui.capturing[1], gui.blue_locations[gui.captured[1]])
                            gui.capturing = (-1, -1)
                            gui.captured = (-1, -1)
                            break
                for i in gui.displayed_pieces:
                    i.destroy()
                    gui.displayed_pieces = []
                gui.captured = (-1, -1)
                gui.capturing = (-1, -1)

        # blue move cycle
        while True:
            gui.root.update()
            if gui.clicked_piece != (-1, -1):
                if gui.clicked_piece[0] == "blue":
                    gui.blue[gui.clicked_piece[1]].config(bg="black")
                    blue_movable = Game.blues[gui.clicked_piece[1]].movable(Game.board)
                    gui.display_movable(blue_movable)
                    if gui.destination != (-1, -1):
                        if Game.move(Game.blues[gui.clicked_piece[1]], gui.destination, "blue"):
                            for i in gui.displayed_pieces:
                                i.destroy()
                                gui.displayed_pieces = []
                            gui.make_move(gui.clicked_piece[0], gui.clicked_piece[1], gui.destination)
                            gui.destination = (-1, -1)
                            gui.clicked_piece = (-1, -1)
                            break
                        else:
                            gui.blue[gui.clicked_piece[1]].config(bg="white")
                            for i in gui.displayed_pieces:
                                i.destroy()
                                gui.displayed_pieces = []
                            gui.clicked_piece = (-1, -1)
                            gui.destination = (-1, -1)
                else:
                    gui.clicked_piece = (-1, -1)
            else:
                if gui.captured != (-1, -1) and gui.capturing != (-1, -1):
                    if gui.capturing[0] == "blue":
                        if Game.move(Game.blues[gui.capturing[1]], gui.red_locations[gui.captured[1]], "blue"):
                            for i in gui.displayed_pieces:
                                i.destroy()
                                gui.displayed_pieces = []
                            gui.red[gui.captured[1]].destroy()
                            gui.make_move(gui.capturing[0], gui.capturing[1], gui.red_locations[gui.captured[1]])
                            gui.capturing = (-1, -1)
                            gui.captured = (-1, -1)
                            break
                for i in gui.displayed_pieces:
                    i.destroy()
                    gui.displayed_pieces = []
                gui.captured = (-1, -1)
                gui.capturing = (-1, -1)

# while True:
#     # red move
#     s, e = input("Input the two cords for red move").split()
#     while True:
#         if Game.is_move_legal(Game.board[int(s[0])][int(s[1])], (int(e[0]), int(e[1]))):
#             break
#         else:
#             s, e = input("Input the two cords for red move").split()
#     Game.move(Game.board[int(s[0])][int(s[1])], (int(e[0]), int(e[1])), "red")
#     current_board = copy.deepcopy(Game.board)
#     for i in range(8):
#         for j in range(8):
#             if current_board[i][j] != 0:
#                 current_board[i][j] = current_board[i][j].type
#     pprint.pprint(current_board)
#     if Game.winner:
#         break
#     # blue move
#     s, e = input("Input the two cords for blue move").split()
#     while True:
#         if Game.is_move_legal(Game.board[int(s[0])][int(s[1])], (int(e[0]), int(e[1]))):
#             break
#         else:
#             s, e = input("Input the two cords for blue move").split()
#     Game.move(Game.board[int(s[0])][int(s[1])], (int(e[0]), int(e[1])), "blue")
#     current_board = copy.deepcopy(Game.board)
#     for i in range(8):
#         for j in range(8):
#             if current_board[i][j] != 0:
#                 current_board[i][j] = current_board[i][j].type
#     pprint.pprint(current_board)
#     if Game.winner:
#         break
# deployment cycles

# reds deploying
# while Game.reds:
#     Game.deploy(Game.reds[index], (int(ending[0]), int(ending[1])))
#     current_board = copy.deepcopy(Game.board)
#     for i in range(8):
#         for j in range(8):
#             if current_board[i][j] != 0:
#                 current_board[i][j] = current_board[i][j].type
#     pprint.pprint(current_board)
# # blues deploying
#
# while Game.blues:
#     index = int(input(f"{[i.type for i in Game.blues]}"))
#     ending = input("Input the cords")
#     Game.deploy(Game.blues[index], (int(ending[0]), int(ending[1])))
#     current_board = copy.deepcopy(Game.board)
#     for i in range(8):
#         for j in range(8):
#             if current_board[i][j] != 0:
#                 current_board[i][j] = current_board[i][j].type
#     pprint.pprint(current_board)
# Game.deployed = True
