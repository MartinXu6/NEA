import pprint
import copy


class Piece:
    def __init__(self, side, Type, location):
        self.side = side
        self.type = Type
        self.location = location

    def movable(self, board):
        start = self.location
        all_moves = []
        movables = []
        for i in self.type, self.type[::-1]:
            all_moves.append((start[0] + i[0], start[1] + i[1]))
            all_moves.append((start[0] - i[0], start[1] - i[1]))
            all_moves.append((start[0] + i[0], start[1] - i[1]))
            all_moves.append((start[0] - i[0], start[1] + i[1]))
        for move in all_moves:
            if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                if board[move[0]][move[1]] != 0:
                    if board[move[0]][move[1]].side != self.side:
                        movables.append(move)
            else:
                movables.append(move)
        return movables


class game:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0], ]
        self.reds = [Piece("red", (2, 2), (-1, -1)), Piece("red", (2, 2), (-1, -1)), Piece("red", (2, 2), (-1, -1)),
                     Piece("red", (2, 2), (-1, -1)), Piece("red", (2, 2), (-1, -1)), Piece("red", (2, 2), (-1, -1)),
                     Piece("red", (2, 2), (-1, -1)), Piece("red", (2, 2), (-1, -1)), Piece("red", (0, 2), (-1, -1)),
                     Piece("red", (0, 2), (-1, -1)), Piece("red", (0, 2), (-1, -1)), Piece("red", (0, 2), (-1, -1)),
                     Piece("red", (1, 1), (-1, -1)), Piece("red", (1, 1), (-1, -1)), Piece("red", (1, 2), (-1, -1)),
                     Piece("red", (0, 1), (-1, -1))]
        self.blues = [Piece("blue", (2, 2), (-1, -1)), Piece("blue", (2, 2), (-1, -1)), Piece("blue", (2, 2), (-1, -1)),
                      Piece("blue", (2, 2), (-1, -1)), Piece("blue", (2, 2), (-1, -1)), Piece("blue", (2, 2), (-1, -1)),
                      Piece("blue", (2, 2), (-1, -1)), Piece("blue", (2, 2), (-1, -1)), Piece("blue", (0, 2), (-1, -1)),
                      Piece("blue", (0, 2), (-1, -1)), Piece("blue", (0, 2), (-1, -1)), Piece("blue", (0, 2), (-1, -1)),
                      Piece("blue", (1, 1), (-1, -1)), Piece("blue", (1, 1), (-1, -1)), Piece("blue", (1, 2), (-1, -1)),
                      Piece("blue", (0, 1), (-1, -1))]
        self.deployed = False
        self.winner = None

    def is_move_legal(self, piece, end):
        if self.deployed:
            if end in piece.movable():
                return True
            else:
                print("ilegal move!")
                return False
        else:
            return False

    def game_won(self, side):
        print(f"{side} has won!")

    def deploy(self, piece, end):
        if self.board[end[0]][end[1]] == 0:
            if not self.deployed:
                if piece.side == "red":
                    self.reds.remove(piece)
                    if end[0] in [6, 7] and 0 <= end[1] <= 7:
                        self.board[end[0]][end[1]] = piece
                        piece.location = end

                elif piece.side == "blue":
                    self.blues.remove(piece)
                    if end[0] in [0, 1] and 0 <= end[1] <= 7:
                        self.board[end[0]][end[1]] = piece
                        piece.location = end

    def move(self, piece, end, side):
        if piece != 0:
            if piece.side == side:
                if self.is_move_legal(piece, end):
                    start = piece.location
                    if self.board[end[0]][end[1]] != 0:
                        captured_piece = self.board[end[0]][end[1]]
                        if captured_piece.type == (0, 1):
                            self.game_won(piece.side)
                            self.winner = piece.side
                        captured_piece.side = piece.side
                        captured_piece.location = (-1, -1)
                        if captured_piece.side == "reds":
                            self.reds.append(captured_piece)
                        else:
                            self.blues.append(captured_piece)
                    self.board[start[0]][start[1]] = 0
                    self.board[end[0]][end[1]] = piece
                    piece.location = end


Game = game()
# deployment cycles

# reds deploying
while Game.reds:
    index = int(input(f"{[i.type for i in Game.reds]}"))
    ending = input("Input the cords")
    Game.deploy(Game.reds[index], (int(ending[0]), int(ending[1])))
    current_board = copy.deepcopy(Game.board)
    for i in range(8):
        for j in range(8):
            if current_board[i][j] != 0:
                current_board[i][j] = current_board[i][j].type
    pprint.pprint(current_board)
# blues deploying

while Game.blues:
    index = int(input(f"{[i.type for i in Game.blues]}"))
    ending = input("Input the cords")
    Game.deploy(Game.blues[index], (int(ending[0]), int(ending[1])))
    current_board = copy.deepcopy(Game.board)
    for i in range(8):
        for j in range(8):
            if current_board[i][j] != 0:
                current_board[i][j] = current_board[i][j].type
    pprint.pprint(current_board)
Game.deployed = True

# game cycle

while True:
    # red move
    s,e = input("Input the two cords for red move").split()
    Game.move(Game.board[int(s[0])][int(s[1])],(int(e[0]), int(e[1])), "red")
    current_board = copy.deepcopy(Game.board)
    for i in range(8):
        for j in range(8):
            if current_board[i][j] != 0:
                current_board[i][j] = current_board[i][j].type
    pprint.pprint(current_board)
    if Game.winner:
        break
    s,e = input("Input the two cords for blue move").split()
    Game.move(Game.board[int(s[0])][int(s[1])], (int(e[0]), int(e[1])), "blue")
    current_board = copy.deepcopy(Game.board)
    for i in range(8):
        for j in range(8):
            if current_board[i][j] != 0:
                current_board[i][j] = current_board[i][j].type
    pprint.pprint(current_board)
    if Game.winner:
        break

