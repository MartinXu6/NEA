from random import randint


def evaluation(current_position):
    return


def deploy_minimax(current_position, deployable, deployed_index, depth, max_player):
    deployable_index = [i for i in range(0, 16) if i not in deployed_index]
    current_index = deployable_index[randint(0, len(deployable_index) - 1)]
    current_deploy = deployable[randint(0, len(deployable) - 1)]
    return (current_index, current_deploy)


def move_minimax(current_position, pieces, depth, max_player):
    all_pieces = []
    for i in current_position:
        for j in i:
            if j != 0:
                if j.side == "blue":
                    all_pieces.append(j)
    while True:
        current_piece = all_pieces[randint(0, len(all_pieces)-1)]
        ends = current_piece.movable(current_position)
        if ends:
            ending = ends[randint(0,len(ends)-1)]
            break
    piece_index = None
    for index in range(len(pieces)):
        if pieces[index] == current_piece.location:
            piece_index = index
            break
    return (piece_index,ending)
