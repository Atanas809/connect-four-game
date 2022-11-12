def is_valid_indices(value, rows, cols):

    valid = []

    for index in value:
        row, col = index[0], index[1]
        if 0 <= row < rows and 0 <= col < cols:
            valid.append([row, col])

    return valid

def find_from_board(value, board):

    output = ""

    for x in value:
        str_value = str(board[x[0]][x[1]])
        output += str_value

    return output

def is_winning(board, current_player, make_move, free_rows,rows, cols):

    row = free_rows[make_move - 1]
    col = make_move - 1
