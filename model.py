import pprint
import copy


class Piece:
    def __init__(self, side, Type, location, index):
        """
        Initialize a game piece with its properties

        Parameters:
        - side (str): Current team/owner of the piece (e.g., "red"/"blue")
        - Type (tuple): Movement pattern vector (e.g., (1,2) for knight-like moves)
        - location (tuple): Current (row, col) position on board. (-1,-1) = off-board
        - index (int): Unique identifier for tracking the piece in collections
        """
        self.origin = side  # Original team (never changes)
        self.side = side  # Current team (can change if captured)
        self.type = Type  # Movement capability definition
        self.location = location  # (row, column) position
        self.index = index  # Identification number

    def movable(self, board):
        """
        Calculate all valid moves for this piece based on:
        - Movement pattern
        - Board boundaries
        - Existing pieces

        Parameters:
        - board (2D list): Current game board state

        Returns:
        - list: Valid (row, col) positions the piece can move to
        """
        # If piece is off-board (in reserve), no possible moves
        start = self.location
        if start == (-1, -1):
            return []

        all_moves = []  # Raw potential moves before validation
        movables = []  # Validated legal moves

        # Generate movement vectors in all directions using:
        # Original type vector + reversed vector (e.g., (1,2) and (2,1))
        for vector in [self.type, self.type[::-1]]:
            # Create 4 directional combinations for each vector
            all_moves.extend([
                (start[0] + vector[0], start[1] + vector[1]),  # Forward
                (start[0] - vector[0], start[1] - vector[1]),  # Backward
                (start[0] + vector[0], start[1] - vector[1]),  # Right-diagonal
                (start[0] - vector[0], start[1] + vector[1])  # Left-diagonal
            ])

        # Validate potential moves
        for move in all_moves:
            # Check if move stays within board boundaries
            if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                target = board[move[0]][move[1]]

                if target == 0:  # Empty square
                    movables.append(move)
                else:  # Occupied square
                    # Only allow capture of enemy pieces
                    if target.side != self.side:
                        movables.append(move)
                        # Note: Does NOT allow moving through pieces, only capturing

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
        # self.board = [[Piece("blue", (2, 2), (0, 0)), Piece("blue", (2, 2), (0, 1)), Piece("blue", (2, 2), (0, 2)),
        # Piece("blue", (2, 2), (0, 3)), Piece("blue", (2, 2), (0, 4)), Piece("blue", (2, 2), (0, 5)), Piece("blue",
        # (2, 2), (0, 6)), Piece("blue", (2, 2), (0, 7))], [Piece("blue", (0, 2), (1, 0)), Piece("blue", (0, 2), (1,
        # 1)), Piece("blue", (0, 2), (1, 2)), Piece("blue", (0, 2), (1, 3)), Piece("blue", (1, 1), (1, 4)),
        # Piece("blue", (1, 1), (1, 5)), Piece("blue", (0, 1), (1, 6)), Piece("blue", (1, 2), (0, 7))], [0, 0, 0, 0,
        # 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [Piece("red",
        # (0, 2), (6, 0)), Piece("red", (0, 2), (6, 1)), Piece("red", (0, 2), (6, 2)), Piece("red", (0, 2), (6, 3)),
        # Piece("red", (1, 1), (6, 4)), Piece("red", (1, 1), (6, 5)), Piece("red", (0, 1), (6, 6)), Piece("red", (1,
        # 2), (6, 7))], [Piece("red", (2, 2), (7, 0)), Piece("red", (2, 2), (7, 1)), Piece("red", (2, 2), (7, 2)),
        # Piece("red", (2, 2), (7, 3)), Piece("red", (2, 2), (7, 4)), Piece("red", (2, 2), (7, 5)), Piece("red", (2,
        # 2), (7, 6)), Piece("red", (2, 2), (7, 7))], ]
        self.reds = [Piece("red", (2, 2), (-1, -1),0), Piece("red", (2, 2), (-1, -1),1), Piece("red", (2, 2), (-1, -1),2),
                     Piece("red", (2, 2), (-1, -1),3), Piece("red", (2, 2), (-1, -1),4), Piece("red", (2, 2), (-1, -1),5),
                     Piece("red", (2, 2), (-1, -1),6), Piece("red", (2, 2), (-1, -1),7), Piece("red", (0, 2), (-1, -1),8),
                     Piece("red", (0, 2), (-1, -1),9), Piece("red", (0, 2), (-1, -1),10), Piece("red", (0, 2), (-1, -1),11),
                     Piece("red", (1, 1), (-1, -1),12), Piece("red", (1, 1), (-1, -1),13), Piece("red", (1, 2), (-1, -1),14),
                     Piece("red", (0, 1), (-1, -1),15)]
        self.blues = [Piece("blue", (2, 2), (-1, -1),0), Piece("blue", (2, 2), (-1, -1),1), Piece("blue", (2, 2), (-1, -1),2),
                      Piece("blue", (2, 2), (-1, -1),3), Piece("blue", (2, 2), (-1, -1),4), Piece("blue", (2, 2), (-1, -1),5),
                      Piece("blue", (2, 2), (-1, -1),6), Piece("blue", (2, 2), (-1, -1),7), Piece("blue", (0, 2), (-1, -1),8),
                      Piece("blue", (0, 2), (-1, -1),9), Piece("blue", (0, 2), (-1, -1),10), Piece("blue", (0, 2), (-1, -1),11),
                      Piece("blue", (1, 1), (-1, -1),12), Piece("blue", (1, 1), (-1, -1),13), Piece("blue", (1, 2), (-1, -1),14),
                      Piece("blue", (0, 1), (-1, -1),15)]
        self.deployed_reds = 0
        self.deployed_blues = 0
        # self.reds = []
        # self.blues = []
        self.deployed = False
        self.winner = None
        self.current_move = []
        self.current_index = []

    def is_move_legal(self, piece, end):
        if self.deployed:
            if end in piece.movable(self.board):
                return True
            else:
                return False
        else:
            return False

    def game_won(self, side):
        pass

    def deploy(self, piece, end):
        moved = False
        if self.board[end[0]][end[1]] == 0:
            if not self.deployed:
                if piece.side == "red":
                    if end[0] in [6, 7] and 0 <= end[1] <= 7:
                        self.deployed_reds += 1
                        self.board[end[0]][end[1]] = piece
                        self.current_move = [piece.side, piece.type, piece.location,end]
                        self.current_index = [piece.index]
                        piece.location = end
                        moved = True


                elif piece.side == "blue":
                    if end[0] in [0, 1] and 0 <= end[1] <= 7:
                        self.deployed_blues += 1
                        self.board[end[0]][end[1]] = piece
                        self.current_move = [piece.side, piece.type, piece.location, end]
                        self.current_index = [piece.index]
                        piece.location = end
                        moved = True
        return moved

    def move(self, piece, end, side):
        if piece != 0:
            if piece.side == side:
                if piece.location == (-1,-1):
                    start = piece.location
                    if self.board[end[0]][end[1]] == 0:
                        self.board[end[0]][end[1]] = piece
                        self.current_move = [piece.side, piece.type, piece.location, end]
                        self.current_index = [piece.index]
                        piece.location = end
                        return True
                    else:
                        return False

                else:
                    if self.is_move_legal(piece, end):
                        start = piece.location
                        if self.board[end[0]][end[1]] != 0:
                            captured_piece = self.board[end[0]][end[1]]
                            if captured_piece.type == (0, 1):
                                self.game_won(piece.side)
                                self.winner = piece.side
                            self.board[end[0]][end[1]].side = piece.side
                            self.board[end[0]][end[1]].location = (-1, -1)
                        self.board[start[0]][start[1]] = 0
                        self.board[end[0]][end[1]] = piece
                        self.current_move = [piece.side, piece.type, piece.location, end]
                        self.current_index = [piece.index]
                        piece.location = end
                        return True
                    else:
                        return False

