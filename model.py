import pprint
import copy


class Piece:
    # Constructor to initialize a game piece with its properties.
    # Parameters:
    #   side: str - The team/owner of the piece (e.g., "red" or "blue").
    #   Type: tuple - Movement pattern vector (e.g., (1, 2) for knight-like moves).
    #   location: tuple - Current board position as (row, col); (-1, -1) indicates off-board or reserve.
    #   index: int - Unique identifier for tracking the piece.
    def __init__(self, side, Type, location, index):
        self.origin = side  # Original team assignment (immutable once set).
        self.side = side  # Current team assignment (may change if the piece is captured).
        self.type = Type  # Movement pattern vector defining the piece's movement capabilities.
        self.location = location  # Current board position (row, col).
        self.index = index  # Unique identifier for the piece.

    # Compute and return all valid moves for this piece based on its movement pattern,
    # board boundaries, and the positions of other pieces.
    # Parameters:
    #   board: list of lists - The current state of the game board where each element is either 0 (empty) or a Piece.
    # Returns:
    #   list - Valid (row, col) positions where the piece can legally move.
    def movable(self, board):
        start = self.location  # Store the current position of the piece.

        # If the piece is off the board (e.g., in reserve), it cannot move.
        if start == (-1, -1):
            return []

        all_moves = []  # List to accumulate raw potential moves based on movement vectors.
        movables = []  # List to store moves validated against board limits and occupancy.

        # Generate potential moves using the original movement vector and its reversed form.
        # This allows for moves in different orders of magnitude in the two dimensions.
        for vector in [self.type, self.type[::-1]]:
            # Calculate four directional moves for each vector:
            # 1. Both components added.
            # 2. Both components subtracted.
            # 3. First added, second subtracted.
            # 4. First subtracted, second added.
            all_moves.extend([
                (start[0] + vector[0], start[1] + vector[1]),
                (start[0] - vector[0], start[1] - vector[1]),
                (start[0] + vector[0], start[1] - vector[1]),
                (start[0] - vector[0], start[1] + vector[1])
            ])

        # Validate each potential move.
        for move in all_moves:
            # Ensure the move is within an 8x8 board.
            if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                target = board[move[0]][move[1]]  # Get the board cell content at the target position.

                if target == 0:
                    # The square is empty; the move is valid.
                    movables.append(move)
                else:
                    # The square is occupied; check if it is an enemy piece.
                    if target.side != self.side:
                        movables.append(move)
                        # Note: The piece can capture an enemy but cannot jump over any piece.
        return movables


class game:
    # Initialize game state and components.
    def __init__(self):
        # 8x8 board with all cells empty (0).
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0], ]
        # List of red pieces with initial configuration.
        self.reds = [Piece("red", (2, 2), (-1, -1), 0), Piece("red", (2, 2), (-1, -1), 1), Piece("red", (2, 2), (-1, -1), 2),
                     Piece("red", (2, 2), (-1, -1), 3), Piece("red", (2, 2), (-1, -1), 4), Piece("red", (2, 2), (-1, -1), 5),
                     Piece("red", (2, 2), (-1, -1), 6), Piece("red", (2, 2), (-1, -1), 7), Piece("red", (0, 2), (-1, -1), 8),
                     Piece("red", (0, 2), (-1, -1), 9), Piece("red", (0, 2), (-1, -1), 10), Piece("red", (0, 2), (-1, -1), 11),
                     Piece("red", (1, 1), (-1, -1), 12), Piece("red", (1, 1), (-1, -1), 13), Piece("red", (1, 2), (-1, -1), 14),
                     Piece("red", (0, 1), (-1, -1), 15)]
        # List of blue pieces with initial configuration.
        self.blues = [Piece("blue", (2, 2), (-1, -1), 0), Piece("blue", (2, 2), (-1, -1), 1), Piece("blue", (2, 2), (-1, -1), 2),
                      Piece("blue", (2, 2), (-1, -1), 3), Piece("blue", (2, 2), (-1, -1), 4), Piece("blue", (2, 2), (-1, -1), 5),
                      Piece("blue", (2, 2), (-1, -1), 6), Piece("blue", (2, 2), (-1, -1), 7), Piece("blue", (0, 2), (-1, -1), 8),
                      Piece("blue", (0, 2), (-1, -1), 9), Piece("blue", (0, 2), (-1, -1), 10), Piece("blue", (0, 2), (-1, -1), 11),
                      Piece("blue", (1, 1), (-1, -1), 12), Piece("blue", (1, 1), (-1, -1), 13), Piece("blue", (1, 2), (-1, -1), 14),
                      Piece("blue", (0, 1), (-1, -1), 15)]
        # Count of deployed red pieces.
        self.deployed_reds = 0
        # Count of deployed blue pieces.
        self.deployed_blues = 0
        # Flag to indicate if pieces are deployed.
        self.deployed = False
        # Winner of the game (None if no winner yet).
        self.winner = None
        # List to store the current move positions.
        self.current_move = []
        # List to store the indices of pieces involved in the current move.
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
        moved = False  # Flag to track successful deployment

        # Check if target cell is empty and deployment phase is active
        if self.board[end[0]][end[1]] == 0:
            if not self.deployed:  # Verify deployment phase hasn't ended

                # Red team deployment rules (bottom rows 6-7)
                if piece.side == "red":
                    if end[0] in [6, 7] and 0 <= end[1] <= 7:
                        self.deployed_reds += 1  # Track red deployments
                        self.board[end[0]][end[1]] = piece  # Place piece on board
                        self.current_move = [piece.side, piece.type, piece.location, end]  # Record move
                        self.current_index = [piece.index]  # Track moved piece index
                        piece.location = end  # Update piece's position
                        moved = True

                # Blue team deployment rules (top rows 0-1)
                elif piece.side == "blue":
                    if end[0] in [0, 1] and 0 <= end[1] <= 7:
                        self.deployed_blues += 1  # Track blue deployments
                        self.board[end[0]][end[1]] = piece
                        self.current_move = [piece.side, piece.type, piece.location, end]
                        self.current_index = [piece.index]
                        piece.location = end
                        moved = True

        return moved  # Return deployment success status

    def move(self, piece, end, side):
        # Move a piece to the target position if legal.
        if piece != 0:
            # Ensure the piece belongs to the correct side.
            if piece.side == side:
                # If the piece is off-board (reserve deployment).
                if piece.location == (-1, -1):
                    start = piece.location  # Current location (off-board)
                    # Deploy only if target cell is empty.
                    if self.board[end[0]][end[1]] == 0:
                        self.board[end[0]][end[1]] = piece  # Place piece on board.
                        self.current_move = [piece.side, piece.type, piece.location, end]  # Record move.
                        self.current_index = [piece.index]  # Record piece index.
                        piece.location = end  # Update piece location.
                        return True
                    else:
                        return False
                else:
                    # For pieces already on board, check if move is legal.
                    if self.is_move_legal(piece, end):
                        start = piece.location  # Current location.
                        # If target cell is occupied, handle capture.
                        if self.board[end[0]][end[1]] != 0:
                            captured_piece = self.board[end[0]][end[1]]
                            # If the captured piece is of a special type, win the game.
                            if captured_piece.type == (0, 1):
                                self.game_won(piece.side)
                                self.winner = piece.side
                            # Capture: change captured piece's side and move it off-board.
                            self.board[end[0]][end[1]].side = piece.side
                            self.board[end[0]][end[1]].location = (-1, -1)
                        # Clear original cell and move piece.
                        self.board[start[0]][start[1]] = 0
                        self.board[end[0]][end[1]] = piece
                        # Record move details.
                        self.current_move = [piece.side, piece.type, piece.location, end]
                        self.current_index = [piece.index]
                        piece.location = end  # Update piece location.
                        return True
                    else:
                        return False


