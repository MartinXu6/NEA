import View
import model
import pprint
import copy
from tkinter import *
from random import randint

gui = View.GUI()
gui.initialise_GUI()
Game = model.game()
num = 1
colours = ["red","blue","green","white"]

while True:
    gui.root.wm_attributes("-transparentcolor", colours[randint(0,3)])
    gui.root.update()
    if gui.destination != (-1, -1) and gui.clicked_piece != (-1, -1):
        gui.make_deploy(gui.clicked_piece[0], gui.clicked_piece[1], gui.destination)
        gui.destination = (-1, -1)
        gui.clicked_piece = (-1, -1)

# deployment cycles

# reds deploying
# while Game.reds:
#     index = int(input(f"{[i.type for i in Game.reds]}"))
#     ending = input("Input the cords")
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
#
# # game cycle
#
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
