import time

import View
import model
import Minimax
import PIL
import pprint
import copy
from tkinter import *
from random import randint


def multi_players(colour):
    # colours = ["red", "blue", "green", "white"]


    while True:
        red_deployed_index = []
        red_deployable = [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7),
                          (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]
        blue_deployed_index = []
        blue_deployable = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                           (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]
        red_got_captured = []
        blue_got_captured = []

        # red deployment cycle
        while True:
            gui.root.update()
            if gui.clicked_piece[0] != -1 and gui.clicked_piece[1] != -1:
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

            if Game.current_move:
                if colour == "red":
                    gui.moves.configure(state ="normal")
                    gui.moves.insert(INSERT,f"\n{Game.current_move[0][0]} has deployed {Game.current_move[1]} to position {Game.current_move[3]}")
                    gui.moves.configure(state="normal")
                else:
                    if Game.current_move[0] =="red":
                        gui.moves.configure(state="normal")
                        gui.moves.insert(INSERT,
                                         f"\nb has deployed {Game.current_move[1]} to position {Game.current_move[3]}")
                        gui.moves.configure(state="normal")
                    else:
                        gui.moves.configure(state="normal")
                        gui.moves.insert(INSERT,
                                         f"\nr has deployed {Game.current_move[1]} to position {Game.current_move[3]}")
                        gui.moves.configure(state="normal")

                Game.current_move = []
            if len(red_deployed_index) == 16:
                break
        # blue deployment cycle
        while True:
            gui.root.update()
            if gui.clicked_piece[0] != -1 and gui.clicked_piece[1] != -1:
                if gui.clicked_piece[0] == "blue" and gui.clicked_piece[1] not in blue_deployed_index:
                    gui.blue[gui.clicked_piece[1]].config(bg="black")
                    gui.display_movable(blue_deployable)
                    if gui.destination != (-1, -1):
                        if Game.deploy(Game.blues[gui.clicked_piece[1]], gui.destination):
                            print(Game.current_move)
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
            if Game.current_move:
                print(Game.current_move)
                Game.current_move = []
            if len(blue_deployed_index) == 16:
                break

        Game.deployed = True
        while True:
            # red move cycle
            if Game.winner:
                gui.game_won(Game.winner)
                break
            while True:
                gui.root.update()
                if gui.clicked_piece[0] != -1 and gui.clicked_piece[1] != -1:
                    if gui.clicked_piece[0] == "red":
                        if gui.clicked_piece[2] == 0:
                            red_movable = []
                            if gui.red_locations[gui.clicked_piece[1]] == (-1, -1):
                                gui.red[gui.clicked_piece[1]].config(bg="black")
                                for i in range(8):
                                    for j in range(8):
                                        if Game.board[i][j] == 0:
                                            red_movable.append((i, j))
                            else:
                                gui.red[gui.clicked_piece[1]].config(bg="black")
                                red_movable = Game.reds[gui.clicked_piece[1]].movable(Game.board)
                        else:
                            red_movable = []
                            if gui.blue_locations[gui.clicked_piece[1]] == (-1, -1):
                                gui.blue[gui.clicked_piece[1]].config(bg="black")
                                for i in range(8):
                                    for j in range(8):
                                        if Game.board[i][j] == 0:
                                            red_movable.append((i, j))
                            else:
                                gui.blue[gui.clicked_piece[1]].config(bg="black")
                                red_movable = Game.blues[gui.clicked_piece[1]].movable(Game.board)
                        gui.display_movable(red_movable)
                        if gui.destination != (-1, -1):
                            current_piece = ""
                            location = ""
                            captured = 0
                            if gui.clicked_piece[2] == 0:
                                current_piece = Game.reds[gui.clicked_piece[1]]
                                location = gui.red_locations[gui.clicked_piece[1]]
                                captured = 0
                            else:
                                current_piece = Game.blues[gui.clicked_piece[1]]
                                location = gui.blue_locations[gui.clicked_piece[1]]
                                captured = 1
                            if location == (-1, -1):
                                if gui.clicked_piece[2] == 1:
                                    if Game.move(Game.blues[gui.clicked_piece[1]], gui.destination, "red"):
                                        if gui.destination in red_movable:
                                            for i in gui.displayed_pieces:
                                                i.destroy()
                                                gui.displayed_pieces = []
                                            print(Game.current_move)
                                            gui.captured_deploy("red", gui.clicked_piece[1], gui.destination)
                                            gui.destination = (-1, -1)
                                            gui.clicked_piece = (-1, -1, 0)
                                            break
                                else:
                                    if Game.move(Game.reds[gui.clicked_piece[1]], gui.destination, "red"):
                                        if gui.destination in red_movable:
                                            for i in gui.displayed_pieces:
                                                i.destroy()
                                                gui.displayed_pieces = []
                                            gui.make_deploy("red", gui.clicked_piece[1], gui.destination)
                                            gui.destination = (-1, -1)
                                            gui.clicked_piece = (-1, -1, 0)
                                            break
                            else:
                                if Game.move(current_piece, gui.destination, "red"):
                                    for i in gui.displayed_pieces:
                                        i.destroy()
                                        gui.displayed_pieces = []
                                    if gui.clicked_piece[2] == 0:
                                        gui.make_move(gui.clicked_piece[0], gui.clicked_piece[1], gui.destination,
                                                      False)
                                    else:
                                        gui.make_move(gui.clicked_piece[0], gui.clicked_piece[1], gui.destination, True)
                                    gui.destination = (-1, -1)
                                    gui.clicked_piece = (-1, -1, 0)
                                    break
                                else:
                                    if gui.clicked_piece[2] == 0:
                                        gui.red[gui.clicked_piece[1]].config(bg="white")
                                    else:
                                        gui.blue[gui.clicked_piece[1]].config(bg="white")
                                    for i in gui.displayed_pieces:
                                        i.destroy()
                                        gui.displayed_pieces = []
                                    gui.clicked_piece = (-1, -1, 0)
                                    gui.destination = (-1, -1)
                    else:
                        gui.clicked_piece = (-1, -1, 0)
                else:
                    if gui.captured[0] != -1 and gui.captured[1] != -1 and gui.capturing[0] != -1 and gui.capturing[
                        1] != -1:
                        if gui.capturing[0] == "red":
                            current_piece = ""
                            position = ""
                            if gui.capturing[2] == 0:
                                current_piece = Game.reds[gui.capturing[1]]
                            else:
                                current_piece = Game.blues[gui.capturing[1]]
                            if gui.captured[2] == 0:
                                position = gui.blue_locations[gui.captured[1]]
                            else:
                                position = gui.red_locations[gui.captured[1]]
                            if Game.move(current_piece, position, "red"):
                                for i in gui.displayed_pieces:
                                    i.destroy()
                                    gui.displayed_pieces = []
                                if gui.captured[2] == 0:
                                    reverse_captured = False
                                else:
                                    reverse_captured = True
                                if gui.captured[2] == 0:
                                    gui.blue[gui.captured[1]].destroy()
                                else:
                                    gui.red[gui.captured[1]].destroy()
                                if gui.captured[2] == 0:
                                    end_point = gui.blue_locations[gui.captured[1]]
                                else:
                                    end_point = gui.red_locations[gui.captured[1]]
                                if gui.capturing[2] == 0:
                                    gui.make_move(gui.capturing[0], gui.capturing[1], end_point,
                                                  False)
                                    gui.got_captured("blue", gui.captured[1], blue_got_captured, False,
                                                     reverse_captured)
                                else:
                                    gui.make_move(gui.capturing[0], gui.capturing[1], end_point,
                                                  True)
                                    gui.got_captured("blue", gui.captured[1], blue_got_captured, True, reverse_captured)
                                gui.capturing = (-1, -1, 0)
                                gui.captured = (-1, -1, 0)
                                break
                    for i in gui.displayed_pieces:
                        i.destroy()
                        gui.displayed_pieces = []
                    gui.captured = (-1, -1, 0)
                    gui.capturing = (-1, -1, 0)
            if Game.current_move:
                print(Game.current_move)
                Game.current_move = []

            # blue move cycle
            if Game.winner:
                gui.game_won(Game.winner)
                break
            while True:
                gui.root.update()
                if gui.clicked_piece[0] != -1 and gui.clicked_piece[1] != -1:
                    if gui.clicked_piece[0] == "blue":
                        if gui.clicked_piece[2] == 0:
                            blue_movable = []
                            if gui.blue_locations[gui.clicked_piece[1]] == (-1, -1):
                                gui.blue[gui.clicked_piece[1]].config(bg="black")
                                for i in range(8):
                                    for j in range(8):
                                        if Game.board[i][j] == 0:
                                            blue_movable.append((i, j))
                            else:
                                gui.blue[gui.clicked_piece[1]].config(bg="black")
                                blue_movable = Game.blues[gui.clicked_piece[1]].movable(Game.board)
                        else:
                            blue_movable = []
                            if gui.red_locations[gui.clicked_piece[1]] == (-1, -1):
                                gui.red[gui.clicked_piece[1]].config(bg="black")
                                for i in range(8):
                                    for j in range(8):
                                        if Game.board[i][j] == 0:
                                            blue_movable.append((i, j))
                            else:
                                gui.red[gui.clicked_piece[1]].config(bg="black")
                                blue_movable = Game.reds[gui.clicked_piece[1]].movable(Game.board)
                        gui.display_movable(blue_movable)
                        if gui.destination != (-1, -1):
                            current_piece = ""
                            location = ""
                            captured = 0
                            if gui.clicked_piece[2] == 0:
                                current_piece = Game.blues[gui.clicked_piece[1]]
                                location = gui.blue_locations[gui.clicked_piece[1]]
                                captured = 0
                            else:
                                current_piece = Game.reds[gui.clicked_piece[1]]
                                location = gui.red_locations[gui.clicked_piece[1]]
                                captured = 1
                            if location == (-1, -1):
                                if gui.clicked_piece[2] == 1:
                                    if Game.move(Game.reds[gui.clicked_piece[1]], gui.destination, "blue"):
                                        if gui.destination in blue_movable:
                                            for i in gui.displayed_pieces:
                                                i.destroy()
                                                gui.displayed_pieces = []
                                            gui.captured_deploy("blue", gui.clicked_piece[1], gui.destination)
                                            gui.destination = (-1, -1)
                                            gui.clicked_piece = (-1, -1, 0)
                                            break
                                else:
                                    if Game.move(Game.blues[gui.clicked_piece[1]], gui.destination, "blue"):
                                        if gui.destination in blue_movable:
                                            for i in gui.displayed_pieces:
                                                i.destroy()
                                                gui.displayed_pieces = []
                                            gui.make_deploy("blue", gui.clicked_piece[1], gui.destination)
                                            gui.destination = (-1, -1)
                                            gui.clicked_piece = (-1, -1, 0)
                                            break
                            else:
                                if Game.move(current_piece, gui.destination, "blue"):
                                    for i in gui.displayed_pieces:
                                        i.destroy()
                                        gui.displayed_pieces = []
                                    if gui.clicked_piece[2] == 0:
                                        gui.make_move(gui.clicked_piece[0], gui.clicked_piece[1], gui.destination,
                                                      False)
                                    else:
                                        gui.make_move(gui.clicked_piece[0], gui.clicked_piece[1], gui.destination, True)
                                    gui.destination = (-1, -1)
                                    gui.clicked_piece = (-1, -1, 0)
                                    break
                                else:
                                    if gui.clicked_piece[2] == 0:
                                        gui.blue[gui.clicked_piece[1]].config(bg="white")
                                    else:
                                        gui.red[gui.clicked_piece[1]].config(bg="white")
                                    for i in gui.displayed_pieces:
                                        i.destroy()
                                        gui.displayed_pieces = []
                                    gui.clicked_piece = (-1, -1, 0)
                                    gui.destination = (-1, -1)
                    else:
                        gui.clicked_piece = (-1, -1, 0)
                else:
                    if gui.captured[0] != -1 and gui.captured[1] != -1 and gui.capturing[0] != -1 and gui.capturing[
                        1] != -1:
                        if gui.capturing[0] == "blue":
                            current_piece = ""
                            position = ""
                            if gui.capturing[2] == 0:
                                current_piece = Game.blues[gui.capturing[1]]
                            else:
                                current_piece = Game.reds[gui.capturing[1]]
                            if gui.captured[2] == 0:
                                position = gui.red_locations[gui.captured[1]]
                            else:
                                position = gui.blue_locations[gui.captured[1]]
                            if Game.move(current_piece, position, "blue"):
                                for i in gui.displayed_pieces:
                                    i.destroy()
                                    gui.displayed_pieces = []
                                if gui.captured[2] == 0:
                                    reverse_captured = False
                                else:
                                    reverse_captured = True
                                if gui.captured[2] == 0:
                                    gui.red[gui.captured[1]].destroy()
                                else:
                                    gui.blue[gui.captured[1]].destroy()
                                if gui.captured[2] == 0:
                                    end_point = gui.red_locations[gui.captured[1]]
                                else:
                                    end_point = gui.blue_locations[gui.captured[1]]
                                if gui.capturing[2] == 0:
                                    gui.make_move(gui.capturing[0], gui.capturing[1], end_point,
                                                  False)
                                    gui.got_captured("red", gui.captured[1], red_got_captured, False, reverse_captured)
                                else:
                                    gui.make_move(gui.capturing[0], gui.capturing[1], end_point,
                                                  True)
                                    gui.got_captured("red", gui.captured[1], red_got_captured, True, reverse_captured)
                                gui.capturing = (-1, -1, 0)
                                gui.captured = (-1, -1, 0)
                                break
                    for i in gui.displayed_pieces:
                        i.destroy()
                        gui.displayed_pieces = []
                    gui.captured = (-1, -1, 0)
                    gui.capturing = (-1, -1, 0)
            if Game.current_move:
                print(Game.current_move)
                Game.current_move = []


def single_player_red():
    # colours = ["red", "blue", "green", "white"]

    while True:
        red_deployed_index = []
        red_deployable = [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7),
                          (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]
        blue_deployed_index = []
        blue_deployable = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                           (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]
        red_got_captured = []
        blue_got_captured = []

        # red deployment cycle
        while True:
            gui.root.update()
            if gui.clicked_piece[0] != -1 and gui.clicked_piece[1] != -1:
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
            current_move = Minimax.deploy_minimax(Game.board, blue_deployable, blue_deployed_index, 4, "blue")
            Game.deploy(Game.blues[current_move[0]], current_move[1])
            gui.make_deploy("blue", current_move[0], current_move[1])
            blue_deployed_index.append(current_move[0])
            blue_deployable.remove(current_move[1])
            time.sleep(0.1)
            if len(blue_deployed_index) == 16:
                break

        Game.deployed = True
        while True:
            # red move cycle
            if Game.winner:
                gui.game_won(Game.winner)
                break
            while True:
                gui.root.update()
                if gui.clicked_piece[0] != -1 and gui.clicked_piece[1] != -1:
                    if gui.clicked_piece[0] == "red":
                        if gui.clicked_piece[2] == 0:
                            red_movable = []
                            if gui.red_locations[gui.clicked_piece[1]] == (-1, -1):
                                gui.red[gui.clicked_piece[1]].config(bg="black")
                                for i in range(8):
                                    for j in range(8):
                                        if Game.board[i][j] == 0:
                                            red_movable.append((i, j))
                            else:
                                gui.red[gui.clicked_piece[1]].config(bg="black")
                                red_movable = Game.reds[gui.clicked_piece[1]].movable(Game.board)
                        else:
                            red_movable = []
                            if gui.blue_locations[gui.clicked_piece[1]] == (-1, -1):
                                gui.blue[gui.clicked_piece[1]].config(bg="black")
                                for i in range(8):
                                    for j in range(8):
                                        if Game.board[i][j] == 0:
                                            red_movable.append((i, j))
                            else:
                                gui.blue[gui.clicked_piece[1]].config(bg="black")
                                red_movable = Game.blues[gui.clicked_piece[1]].movable(Game.board)
                        gui.display_movable(red_movable)
                        if gui.destination != (-1, -1):
                            current_piece = ""
                            location = ""
                            captured = 0
                            if gui.clicked_piece[2] == 0:
                                current_piece = Game.reds[gui.clicked_piece[1]]
                                location = gui.red_locations[gui.clicked_piece[1]]
                                captured = 0
                            else:
                                current_piece = Game.blues[gui.clicked_piece[1]]
                                location = gui.blue_locations[gui.clicked_piece[1]]
                                captured = 1
                            if location == (-1, -1):
                                if gui.clicked_piece[2] == 1:
                                    if Game.move(Game.blues[gui.clicked_piece[1]], gui.destination, "red"):
                                        if gui.destination in red_movable:
                                            for i in gui.displayed_pieces:
                                                i.destroy()
                                                gui.displayed_pieces = []
                                            gui.captured_deploy("red", gui.clicked_piece[1], gui.destination)
                                            gui.destination = (-1, -1)
                                            gui.clicked_piece = (-1, -1, 0)
                                            break
                                else:
                                    if Game.move(Game.reds[gui.clicked_piece[1]], gui.destination, "red"):
                                        if gui.destination in red_movable:
                                            for i in gui.displayed_pieces:
                                                i.destroy()
                                                gui.displayed_pieces = []
                                            gui.make_deploy("red", gui.clicked_piece[1], gui.destination)
                                            gui.destination = (-1, -1)
                                            gui.clicked_piece = (-1, -1, 0)
                                            break
                            else:
                                if Game.move(current_piece, gui.destination, "red"):
                                    for i in gui.displayed_pieces:
                                        i.destroy()
                                        gui.displayed_pieces = []
                                    if gui.clicked_piece[2] == 0:
                                        gui.make_move(gui.clicked_piece[0], gui.clicked_piece[1], gui.destination,
                                                      False)
                                    else:
                                        gui.make_move(gui.clicked_piece[0], gui.clicked_piece[1], gui.destination, True)
                                    gui.destination = (-1, -1)
                                    gui.clicked_piece = (-1, -1, 0)
                                    break
                                else:
                                    if gui.clicked_piece[2] == 0:
                                        gui.red[gui.clicked_piece[1]].config(bg="white")
                                    else:
                                        gui.blue[gui.clicked_piece[1]].config(bg="white")
                                    for i in gui.displayed_pieces:
                                        i.destroy()
                                        gui.displayed_pieces = []
                                    gui.clicked_piece = (-1, -1, 0)
                                    gui.destination = (-1, -1)
                    else:
                        gui.clicked_piece = (-1, -1, 0)
                else:
                    if gui.captured[0] != -1 and gui.captured[1] != -1 and gui.capturing[0] != -1 and gui.capturing[
                        1] != -1:
                        if gui.capturing[0] == "red":
                            current_piece = ""
                            position = ""
                            if gui.capturing[2] == 0:
                                current_piece = Game.reds[gui.capturing[1]]
                            else:
                                current_piece = Game.blues[gui.capturing[1]]
                            if gui.captured[2] == 0:
                                position = gui.blue_locations[gui.captured[1]]
                            else:
                                position = gui.red_locations[gui.captured[1]]
                            if Game.move(current_piece, position, "red"):
                                for i in gui.displayed_pieces:
                                    i.destroy()
                                    gui.displayed_pieces = []
                                if gui.captured[2] == 0:
                                    reverse_captured = False
                                else:
                                    reverse_captured = True
                                if gui.captured[2] == 0:
                                    gui.blue[gui.captured[1]].destroy()
                                else:
                                    gui.red[gui.captured[1]].destroy()
                                if gui.captured[2] == 0:
                                    end_point = gui.blue_locations[gui.captured[1]]
                                else:
                                    end_point = gui.red_locations[gui.captured[1]]
                                if gui.capturing[2] == 0:
                                    gui.make_move(gui.capturing[0], gui.capturing[1], end_point,
                                                  False)
                                    gui.got_captured("blue", gui.captured[1], blue_got_captured, False,
                                                     reverse_captured)
                                else:
                                    gui.make_move(gui.capturing[0], gui.capturing[1], end_point,
                                                  True)
                                    gui.got_captured("blue", gui.captured[1], blue_got_captured, True, reverse_captured)
                                gui.capturing = (-1, -1, 0)
                                gui.captured = (-1, -1, 0)
                                break
                    for i in gui.displayed_pieces:
                        i.destroy()
                        gui.displayed_pieces = []
                    gui.captured = (-1, -1, 0)
                    gui.capturing = (-1, -1, 0)

            # blue move cycle
            if Game.winner:
                gui.game_won(Game.winner)
                break
            gui.root.update()
            current_move = Minimax.move_minimax(Game.board, gui.blue_locations, 4, "blue")
            Game.move(Game.blues[current_move[0]], current_move[1], "blue")
            gui.make_move("blue", current_move[0], current_move[1], 0)

def single_player_blue():
    # colours = ["red", "blue", "green", "white"]

    while True:
        red_deployed_index = []
        red_deployable = [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7),
                          (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]
        blue_deployed_index = []
        blue_deployable = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                           (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]
        red_got_captured = []
        blue_got_captured = []
        # blue deployment cycle
        while True:
            gui.root.update()
            current_move = Minimax.deploy_minimax(Game.board, blue_deployable, blue_deployed_index, 4, "blue")
            Game.deploy(Game.blues[current_move[0]], current_move[1])
            gui.make_deploy("blue", current_move[0], current_move[1])
            blue_deployed_index.append(current_move[0])
            blue_deployable.remove(current_move[1])
            time.sleep(0.1)
            if len(blue_deployed_index) == 16:
                break
        # red deployment cycle
        while True:
            gui.root.update()
            if gui.clicked_piece[0] != -1 and gui.clicked_piece[1] != -1:
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

        Game.deployed = True
        while True:
            # blue move cycle
            if Game.winner:
                gui.game_won(Game.winner)
                break
            gui.root.update()
            current_move = Minimax.move_minimax(Game.board, gui.blue_locations, 4, "blue")
            Game.move(Game.blues[current_move[0]], current_move[1], "blue")
            gui.make_move("blue", current_move[0], current_move[1], 0)
            # red move cycle
            if Game.winner:
                gui.game_won(Game.winner)
                break
            while True:
                gui.root.update()
                if gui.clicked_piece[0] != -1 and gui.clicked_piece[1] != -1:
                    if gui.clicked_piece[0] == "red":
                        if gui.clicked_piece[2] == 0:
                            red_movable = []
                            if gui.red_locations[gui.clicked_piece[1]] == (-1, -1):
                                gui.red[gui.clicked_piece[1]].config(bg="black")
                                for i in range(8):
                                    for j in range(8):
                                        if Game.board[i][j] == 0:
                                            red_movable.append((i, j))
                            else:
                                gui.red[gui.clicked_piece[1]].config(bg="black")
                                red_movable = Game.reds[gui.clicked_piece[1]].movable(Game.board)
                        else:
                            red_movable = []
                            if gui.blue_locations[gui.clicked_piece[1]] == (-1, -1):
                                gui.blue[gui.clicked_piece[1]].config(bg="black")
                                for i in range(8):
                                    for j in range(8):
                                        if Game.board[i][j] == 0:
                                            red_movable.append((i, j))
                            else:
                                gui.blue[gui.clicked_piece[1]].config(bg="black")
                                red_movable = Game.blues[gui.clicked_piece[1]].movable(Game.board)
                        gui.display_movable(red_movable)
                        if gui.destination != (-1, -1):
                            current_piece = ""
                            location = ""
                            captured = 0
                            if gui.clicked_piece[2] == 0:
                                current_piece = Game.reds[gui.clicked_piece[1]]
                                location = gui.red_locations[gui.clicked_piece[1]]
                                captured = 0
                            else:
                                current_piece = Game.blues[gui.clicked_piece[1]]
                                location = gui.blue_locations[gui.clicked_piece[1]]
                                captured = 1
                            if location == (-1, -1):
                                if gui.clicked_piece[2] == 1:
                                    if Game.move(Game.blues[gui.clicked_piece[1]], gui.destination, "red"):
                                        if gui.destination in red_movable:
                                            for i in gui.displayed_pieces:
                                                i.destroy()
                                                gui.displayed_pieces = []
                                            gui.captured_deploy("red", gui.clicked_piece[1], gui.destination)
                                            gui.destination = (-1, -1)
                                            gui.clicked_piece = (-1, -1, 0)
                                            break
                                else:
                                    if Game.move(Game.reds[gui.clicked_piece[1]], gui.destination, "red"):
                                        if gui.destination in red_movable:
                                            for i in gui.displayed_pieces:
                                                i.destroy()
                                                gui.displayed_pieces = []
                                            gui.make_deploy("red", gui.clicked_piece[1], gui.destination)
                                            gui.destination = (-1, -1)
                                            gui.clicked_piece = (-1, -1, 0)
                                            break
                            else:
                                if Game.move(current_piece, gui.destination, "red"):
                                    for i in gui.displayed_pieces:
                                        i.destroy()
                                        gui.displayed_pieces = []
                                    if gui.clicked_piece[2] == 0:
                                        gui.make_move(gui.clicked_piece[0], gui.clicked_piece[1], gui.destination,
                                                      False)
                                    else:
                                        gui.make_move(gui.clicked_piece[0], gui.clicked_piece[1], gui.destination, True)
                                    gui.destination = (-1, -1)
                                    gui.clicked_piece = (-1, -1, 0)
                                    break
                                else:
                                    if gui.clicked_piece[2] == 0:
                                        gui.red[gui.clicked_piece[1]].config(bg="white")
                                    else:
                                        gui.blue[gui.clicked_piece[1]].config(bg="white")
                                    for i in gui.displayed_pieces:
                                        i.destroy()
                                        gui.displayed_pieces = []
                                    gui.clicked_piece = (-1, -1, 0)
                                    gui.destination = (-1, -1)
                    else:
                        gui.clicked_piece = (-1, -1, 0)
                else:
                    if gui.captured[0] != -1 and gui.captured[1] != -1 and gui.capturing[0] != -1 and gui.capturing[
                        1] != -1:
                        if gui.capturing[0] == "red":
                            current_piece = ""
                            position = ""
                            if gui.capturing[2] == 0:
                                current_piece = Game.reds[gui.capturing[1]]
                            else:
                                current_piece = Game.blues[gui.capturing[1]]
                            if gui.captured[2] == 0:
                                position = gui.blue_locations[gui.captured[1]]
                            else:
                                position = gui.red_locations[gui.captured[1]]
                            if Game.move(current_piece, position, "red"):
                                for i in gui.displayed_pieces:
                                    i.destroy()
                                    gui.displayed_pieces = []
                                if gui.captured[2] == 0:
                                    reverse_captured = False
                                else:
                                    reverse_captured = True
                                if gui.captured[2] == 0:
                                    gui.blue[gui.captured[1]].destroy()
                                else:
                                    gui.red[gui.captured[1]].destroy()
                                if gui.captured[2] == 0:
                                    end_point = gui.blue_locations[gui.captured[1]]
                                else:
                                    end_point = gui.red_locations[gui.captured[1]]
                                if gui.capturing[2] == 0:
                                    gui.make_move(gui.capturing[0], gui.capturing[1], end_point,
                                                  False)
                                    gui.got_captured("blue", gui.captured[1], blue_got_captured, False,
                                                     reverse_captured)
                                else:
                                    gui.make_move(gui.capturing[0], gui.capturing[1], end_point,
                                                  True)
                                    gui.got_captured("blue", gui.captured[1], blue_got_captured, True, reverse_captured)
                                gui.capturing = (-1, -1, 0)
                                gui.captured = (-1, -1, 0)
                                break
                    for i in gui.displayed_pieces:
                        i.destroy()
                        gui.displayed_pieces = []
                    gui.captured = (-1, -1, 0)
                    gui.capturing = (-1, -1, 0)

menu = View.start_menu()
game_mode = ""
if menu.running:
    game_mode = menu.running
else:
    quit()
choosing = View.Choosing()
gui = View.GUI()
if choosing.Side == "red":
    gui.rtpt = PIL.Image.open("Images/Pieces/r2.2.png")
    gui.rtpt = gui.rtpt.resize(gui.piece_size)
    gui.rzpo = PIL.Image.open("Images/Pieces/r0.1.png")
    gui.rzpo = gui.rzpo.resize(gui.piece_size)
    gui.ropo = PIL.Image.open("Images/Pieces/r1.1.png")
    gui.ropo = gui.ropo.resize(gui.piece_size)
    gui.ropt = PIL.Image.open("Images/Pieces/r1.2.png")
    gui.ropt = gui.ropt.resize(gui.piece_size)
    gui.rzpt = PIL.Image.open("Images/Pieces/r0.2.png")
    gui.rzpt = gui.rzpt.resize(gui.piece_size)
    gui.btpt = PIL.Image.open("Images/Pieces/b2.2.png")
    gui.btpt = gui.btpt.resize(gui.piece_size)
    gui.bzpt = PIL.Image.open("Images/Pieces/b0.2.png")
    gui.bzpt = gui.bzpt.resize(gui.piece_size)
    gui.bopt = PIL.Image.open("Images/Pieces/b1.2.png")
    gui.bopt = gui.bopt.resize(gui.piece_size)
    gui.bzpo = PIL.Image.open("Images/Pieces/b0.1.png")
    gui.bzpo = gui.bzpo.resize(gui.piece_size)
    gui.bopo = PIL.Image.open("Images/Pieces/b1.1.png")
    gui.bopo = gui.bopo.resize(gui.piece_size)
elif choosing.Side == "blue":
    gui.rtpt = PIL.Image.open("Images/Pieces/b2.2.png")
    gui.rtpt = gui.rtpt.resize(gui.piece_size)
    gui.rzpo = PIL.Image.open("Images/Pieces/b0.1.png")
    gui.rzpo = gui.rzpo.resize(gui.piece_size)
    gui.ropo = PIL.Image.open("Images/Pieces/b1.1.png")
    gui.ropo = gui.ropo.resize(gui.piece_size)
    gui.ropt = PIL.Image.open("Images/Pieces/b1.2.png")
    gui.ropt = gui.ropt.resize(gui.piece_size)
    gui.rzpt = PIL.Image.open("Images/Pieces/b0.2.png")
    gui.rzpt = gui.rzpt.resize(gui.piece_size)
    gui.btpt = PIL.Image.open("Images/Pieces/r2.2.png")
    gui.btpt = gui.btpt.resize(gui.piece_size)
    gui.bzpt = PIL.Image.open("Images/Pieces/r0.2.png")
    gui.bzpt = gui.bzpt.resize(gui.piece_size)
    gui.bopt = PIL.Image.open("Images/Pieces/r1.2.png")
    gui.bopt = gui.bopt.resize(gui.piece_size)
    gui.bzpo = PIL.Image.open("Images/Pieces/r0.1.png")
    gui.bzpo = gui.bzpo.resize(gui.piece_size)
    gui.bopo = PIL.Image.open("Images/Pieces/r1.1.png")
    gui.bopo = gui.bopo.resize(gui.piece_size)
gui.initialise_GUI()
Game = model.game()


if menu.running == "multi":
    multi_players(choosing.Side)
elif menu.running == "single":
    if choosing.Side == "red":
        single_player_red()
    elif choosing.Side == "blue":
        single_player_blue()
