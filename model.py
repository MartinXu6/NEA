import pprint


class Piece:
    def __init__(self, side, Type, location):
        self.side = side
        self.type = Type
        self.location = location


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
        self.deployed = True

    def is_move_legal(self, piece, end):
        if self.deployed:
            start = piece.location
            if 0 <= end[0] <= 7 and 0 <= end[1] <= 7:
                if (abs(end[0] - start[0]), abs(end[1] - start[1])) in [piece.type, piece.type[::-1]]:
                    if self.board[end[0]][end[1]].side == piece.side:
                        return False
                    else:
                        return True
        else:
            return False

    def deploy(self, piece, end):
        if self.board[end[0]][end[1]] != 0:
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

    def move(self, piece, end):
        if self.is_move_legal(piece, end):
            start = piece.location
            if self.board[end[0]][end[1]] != 0:
                self.board[end[0]][end[1]].side = piece.side
                self.board[end[0]][end[1]].location = (-1, -1)
            self.board[start[0]][start[1]] = 0
            self.board[end[0]][end[1]] = piece
            piece.location = end

    def movable(self, piece):
        diagram_board = [[0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0], ]
        if piece != 0:
            start = piece.location
            diagram_board[start[0]][start[1]] = 2
            movables = []
            for i in piece.type, piece.type[::-1]:
                movables.append((start[0] + i[0], start[1] + i[1]))
                movables.append((start[0] - i[0], start[1] - i[1]))
                movables.append((start[0] + i[0], start[1] - i[1]))
                movables.append((start[0] - i[0], start[1] + i[1]))
            for move in movables:
                if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                    diagram_board[move[0]][move[1]] = 1
            return diagram_board


Game = game()
# deployment cycles

# reds deploying
for r in range(16):
    index = int(input(f"{[i.type for i in Game.reds]}"))
    ending = input("Input the cords")
    Game.deploy(Game.reds[index],(int(ending[0]), int(ending[1])))
    current_board = Game.board
    for i in range(8):
        for j in range(8):
            if current_board[i][j] != 0:
                current_board[i][j] = current_board[i][j].type
    pprint.pprint(Game.board)
    pprint.pprint(current_board)
print(Game.board)



