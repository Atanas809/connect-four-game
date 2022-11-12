def is_valid_indices(value, rows, cols):

    valid = []

    for index in value:
        row, col = index[0], index[1]
        if 0 <= row < rows and 0 <= col < cols:
            valid.append([row, col])

    return valid

def find_from_board(value, board):

    output = ""
