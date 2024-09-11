import pprint


class Piece:
    def __init__(self, side, Type, location):
        self.side = side
        self.type = Type
        self.location = location


class game:
    def __init__(self):
        self.board = [[0] * 8,
                      [0] * 8,
                      [0] * 8,
                      [0] * 8,
                      [0] * 8,
                      [0] * 8,
                      [0] * 8,
                      [0] * 8, ]
        self.reds = [Piece("red", (2, 2), (-1, -1))] * 8 + [Piece("red", (0, 2), (-1, -1))] * 4 + [
            Piece("red", (1, 1), (-1, -1))] * 2 + [Piece("red", (1, 2), (-1, -1))] + [Piece("red", (0, 1), (-1, -1))]
        self.blues = [Piece("blue", (2, 2), (-1, -1))] * 8 + [Piece("blue", (0, 2), (-1, -1))] * 4 + [
            Piece("blue", (1, 1), (-1, -1))] * 2 + [Piece("blue", (1, 2), (-1, -1))] + [Piece("blue", (0, 1), (-1, -1))]
        self.deployed = False

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

    def deployment(self, piece, end):
        if not self.deployed:
            if piece.side == "red":
                if end[0] in [6, 7] and 0 <= end[1] <= 7:
                    self.board[end[0]][end[1]] = piece
                    piece.location = end
                else:
                    print("fjrdhfdhfcdm")
            elif piece.side == "blue":
                if end[0] in [0, 1] and 0 <= end[1] <= 7:
                    self.board[end[0]][end[1]] = piece
                    piece.location = end

    def move(self, piece, end):
        if self.is_move_legal(piece, end):
            start = piece.location
            self.board[start[0]][start[1]] = 0
            self.board[end[0]][end[1]] = piece
            piece.location = end


Game = game()
Game.deployment(Game.reds[0], (6, 2))
pprint.pprint(Game.board)
