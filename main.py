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


    winning_paths = {
        "horizontal": [
            [row, 0],
            [row, 1],
            [row, 2],
            [row, 3],
            [row, 4],
            [row, 5],
            [row, 6],
        ],
        "vertical": [
            [0, col],
            [1, col],
            [2, col],
            [3, col],
            [4, col],
            [5, col],
        ],
        "main_ diagonal": [
            [row, col],
            [row + 1, col + 1],
            [row + 2, col + 2],
            [row + 3, col + 3],

        ],
        "secondary_diagonal": [
            [row, col],
            [row + 1, col - 1],
            [row + 2, col - 2],
            [row + 3, col - 3],

        ]

    }

    for key, value in winning_paths.items():
        need_to_win = str(current_player) * 4
        valid_values = is_valid_indices(value, rows, cols)
        result = find_from_board(valid_values, board)
        if need_to_win in result:
            return True


def print_board(board):
    return [print(row) for row in board]

def get_free_rows(board, cols):
    free_spaces = [0] * cols

    index = 0

    for row in range(len(board[0])):
        next_row = 0
        next_col = index
        while next_row <= len(board) - 1:
            if board[next_row][next_col] == 0:
                free_spaces[next_col] += 1
                next_row += 1
            else:
                break

        index += 1


    return free_spaces

def apply_move(board, current_player, make_move, free_rows):

    position = make_move - 1

    if free_rows[position] > 0:
        last_free_row = free_rows[position] - 1
        board[last_free_row][position] = current_player
        free_rows[position] -= 1

    return board



def is_valid_move(move, cols):

    return 1 <= move <= cols

def make_board(rows, cols):

    return [[0] * cols for _ in range(rows)]


def play(board):

    current_player = 1

    free_rows = get_free_rows(board, cols)

    while True:

        make_move = input(f"Player {current_player}, please choose a column between [1-7]: ")

        if make_move.isdigit():
            make_move = int(make_move)
            if is_valid_move(make_move, cols):
                board = apply_move(board, current_player, make_move, free_rows)
                print_board(board)
                if is_winning(board, current_player, make_move, free_rows, rows, cols):
                    print(f"The winner is player {current_player}")
                    break
            else:
                print("Please enter a valid column between [1-7]")
                continue

        else:
            print("Please enter a valid number, MUST BE INTEGER !!!")
            continue

        if current_player == 2:
            current_player = 1
            continue

        current_player += 1


rows, cols = 6, 7
board = make_board(rows, cols)
play(board)
# test = [
#     [0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 1, 4],
#     [1, 0, 0, 1, 0, 1, 4],
#     [1, 0, 1, 2, 0, 1, 4],
#     [1, 1, 1, 1, 5, 1, 4],
#     [1, 2, 2, 2, 5, 1, 2],
# ]
# 1
# 2
# 2
# 3
# 3
# 7
# 3
# 4
# 4
# 4
# 4
