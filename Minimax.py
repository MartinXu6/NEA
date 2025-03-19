import time
from random import randint
from copy import deepcopy


def evaluation(current_position, max_player, bench):
    # Heatmap assigns strategic positional weights to prioritize central control
    board_heat_map = [[1, 2, 2, 2, 2, 2, 2, 1],
                      [2, 2, 2, 2, 2, 2, 2, 2],
                      [2, 2, 3, 3, 3, 3, 2, 2],
                      [2, 2, 3, 3.5, 3.5, 3, 2, 2],
                      [2, 2, 3, 3.5, 3.5, 3, 2, 2],
                      [2, 2, 3, 3, 3, 3, 2, 2],
                      [2, 2, 2, 2, 2, 2, 2, 2],
                      [1, 2, 2, 2, 2, 2, 2, 1], ]

    # Static values assigned to piece types to reflect their relative importance
    piece_value = {(2, 2): 3, (0, 2): 3, (1, 1): 5, (1, 2): 9, (0, 1): 1}

    total_value = 0
    red_won = True  # Assumes red has won unless proven otherwise
    blue_won = False  # Assumes blue has not won unless proven otherwise

    # Iterates over every board position to evaluate piece contributions and threats
    for line in range(8):
        for piece in range(8):
            if current_position[line][piece] != 0:
                current_movable = current_position[line][piece].movable(current_position)

                # For max_player's pieces: adds value based on position and captures of enemy 0-1
                if current_position[line][piece].side == max_player:
                    if current_position[line][piece].type == (0, 1):
                        red_won = False  # Max's 0-1 is alive; red hasn't won yet
                    # Checks if any move threatens the opponent's 0-1 piece
                    for move in current_movable:
                        if current_position[move[0]][move[1]] != 0:
                            if current_position[move[0]][move[1]].type == (0, 1) and current_position[move[0]][
                                move[1]].side != max_player:
                                total_value += 15  # Bonus for threatening enemy 0-1
                    # Combines piece value and positional heatmap for scoring
                    total_value += piece_value.get(current_position[line][piece].type) * board_heat_map[line][piece]

                # For opponent's pieces: subtracts their value and tracks their threats
                else:
                    if current_position[line][piece].type == (0, 1):
                        blue_won = False  # Opponent's 0-1 is alive; blue hasn't won yet
                    for move in current_movable:
                        if current_position[move[0]][move[1]] != 0:
                            if current_position[move[0]][move[1]].type == (0, 1) and current_position[move[0]][
                                move[1]].side == max_player:
                                total_value -= 15  # Penalty for opponent threatening max's 0-1
                    total_value -= piece_value.get(current_position[line][piece].type) * board_heat_map[line][piece]


    # Adjusts total_value drastically if a player's 0-1 is captured
    if red_won:
        total_value -= 999  # Severe penalty if max_player (red) loses
    if blue_won:
        total_value += 999  # Massive reward if max_player (blue) wins

    return total_value


def get_all_moves(current_position, player):
    all_moves = {}
    for row in range(8):
        for col in range(8):
            current_piece = current_position[row][col]
            if current_piece != 0:
                if current_piece.side == player:
                    ends = current_piece.movable(current_position)
                    all_moves[(row, col)] = ends
    return all_moves


def get_all_deploys(current_position):
    available_position = []
    for row in range(8):
        for col in range(8):
            if current_position[row][col] == 0:
                available_position.append((row, col))
    return available_position


def deploy_minimax(current_position, deployable, deployed_index, depth, current_player):
    deployable_index = [i for i in range(0, 16) if i not in deployed_index]
    current_index = deployable_index[randint(0, len(deployable_index) - 1)]
    current_deploy = deployable[randint(0, len(deployable) - 1)]
    return current_index, current_deploy


def move_minimax(current_position, current_pieces, opposition_pieces, depth, current_player, previous_move):
    # Deep copies preserve the original game state while simulating moves
    new_current_pieces = deepcopy(current_pieces)
    new_opposition_pieces = deepcopy(opposition_pieces)
    # Tracks captured pieces (marked with (-1, -1) location) for potential re-deployment
    bench = [piece for piece in new_current_pieces + new_opposition_pieces if piece.location == (-1, -1)]

    # Base case: returns the board evaluation and the preceding move at depth 0
    if depth == 0:
        return [evaluation(current_position, "blue", bench), previous_move]

    # Generates all possible moves and deployment options for the current player
    all_moves = get_all_moves(current_position, current_player)
    # Identifies captured pieces that can be re-deployed
    current_deployable = [piece for piece in new_current_pieces + new_opposition_pieces if
                          piece.location == (-1, -1) and piece.side == current_player]
    all_deploys = get_all_deploys(current_position)
    all_positions = []
    all_root_moves = []
    winning_move = False

    # Simulates all possible piece movements and captures
    for piece in all_moves:
        piece_moves = all_moves.get(piece)
        for move in piece_moves:
            new_position = deepcopy(current_position)
            current_piece = new_position[piece[0]][piece[1]]
            # Checks if a move captures the opponent’s 0-1 (win condition)
            if new_position[move[0]][move[1]] != 0:
                if new_position[move[0]][move[1]].type == (0, 1):
                    winning_move = (piece, move)  # Flags a winning move
                # Updates captured piece ownership based on the capturer’s side
                taken_piece = new_position[move[0]][move[1]]
                if taken_piece.origin == current_player:
                    new_current_pieces[taken_piece.index].location = (-1, -1)
                else:
                    new_opposition_pieces[taken_piece.index].location = (-1, -1)
            # Updates the board with the new piece location
            new_position[move[0]][move[1]] = current_piece
            new_position[piece[0]][piece[1]] = 0
            new_position[move[0]][move[1]].location = (move[0], move[1])
            all_positions.append(new_position)
            all_root_moves.append((piece, move))

    # Simulates all possible deployments of captured pieces
    for piece in current_deployable:
        for move in all_deploys:
            new_position = deepcopy(current_position)
            new_position[move[0]][move[1]] = piece
            new_position[move[0]][move[1]].location = (move[0], move[1])
            # Updates the deploying player’s piece list
            if piece.origin == current_player:
                new_current_pieces[piece.index].location = (move[0], move[1])
            else:
                new_opposition_pieces[piece.index].location = (move[0], move[1])
            all_positions.append(new_position)
            all_root_moves.append((piece.origin, piece.side, piece.index, move))

    # Recursive minimax logic with alternating players and depth-based termination
    if depth != 2:
        if current_player == "blue":
            # Maximizes evaluations for the blue player (AI)
            evals = [move_minimax(all_positions[position], new_opposition_pieces, new_current_pieces, depth - 1, "red",
                                  all_root_moves[position]) for position in range(len(all_positions))]
            max_eval = max(evals, key=lambda x: x[0])
            max_eval[1] = previous_move  # Tracks the root move for backtracking
            return max_eval
        else:
            # Minimizes evaluations for the red player (opponent)
            evals = [move_minimax(all_positions[position], new_opposition_pieces, new_current_pieces, depth - 1, "blue",
                                  all_root_moves[position]) for position in range(len(all_positions))]
            min_eval = min(evals, key=lambda x: x[0])
            min_eval[1] = previous_move
            return min_eval
    else:
        # Prioritizes immediate winning moves at depth 2 (terminal layer)
        if winning_move:
            return winning_move
        # Default to maximizing evaluations if no win is detected
        evals = [
            move_minimax(all_positions[position], new_opposition_pieces, new_current_pieces, depth - 1, "red",
                         all_root_moves[position])
            for position in range(len(all_positions))]
        max_eval = max(evals, key=lambda x: x[0])
        return max_eval[1]

    # for index in range(len(pieces)):
    #     if pieces[index] == current_piece.location:
    #         piece_index = index
    #         break
    # return (piece_index, ending)
