def is_valid(row: int, col: int, board: list[list[int]]) -> bool:
    '''Checks if a board state is valid specifically considering
    the addition of the newest row and column change'''
    for value in range(0, 8):
        if board[row][col] == board[row][value] and col != value:
            return False
        elif board[row][col] == board[value][col] and row != value:
            return False
    box_row = row // 3
    box_col = row // 3
    for i in range(0, 2):
        for j in range(0, 2):
            if box_row * 3 + i == row and box_col * 3 + j == col:
                pass
            elif board[box_row * 3 + i][box_col * 3 + j] == board[row][col]:
                return False
    return True



def solve(row: int, col: int, board: list[list[int]]) -> bool | list[list[int]]:
    '''Backtracking recursive algorithm which goes through the list, and inserts
    a value. It then checks if that is a valid board state, and if it is, it moves
    on using recursion. In the case that it reaches an invalid board state, it goes
    back until it's valid again and then keeps going'''
    pass