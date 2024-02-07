def is_valid(row: int, col: int, board: list[list[int]], new_val: int) -> bool:
    '''Checks if a board state is valid specifically considering
    the addition of the newest row and column change to num'''

    for value in range(0, 9):
        if board[row][value] == new_val:
            return False
    for value in range(0, 9):
        if board[value][col] == new_val:
            return False
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[box_row + i][box_col + j] == new_val:
                return False
    return True



def solve(row: int, col: int, board: list[list[int]]) -> bool | list[list[int]]:
    '''Backtracking recursive algorithm which goes through the list, and inserts
    a value. It then checks if that is a valid board state, and if it is, it moves
    on using recursion. In the case that it reaches an invalid board state, it goes
    back until it's valid again and then keeps going'''
    if row == (len(board) - 1) and col == len(board[row]):
        return True
    if col == len(board[row]):
        col = 0
        row += 1

    if board[row][col] != 0:
        return solve(row, col + 1, board)
    for i in range(1, 10):

        if is_valid(row, col, board, i):
            board[row][col] = i
            if solve(row, col + 1, board): #recursive for backtracking
                return True
        board[row][col] = 0
    return False

if __name__ == '__main__':
    board = [
            [3, 0, 0, 0, 4, 0, 0, 7, 0],
            [0, 0, 6, 0, 2, 0, 0, 0, 0],
            [5, 0, 0, 7, 0, 6, 0, 0, 9],
            [0, 0, 5, 3, 0, 1, 0, 2, 0],
            [0, 0, 0, 0, 6, 0, 0, 0, 0],
            [9, 0, 0, 0, 0, 0, 8, 0, 0],
            [0, 3, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 4, 0, 0, 0, 0, 0],
            [0, 0, 1, 5, 0, 7, 0, 3, 0]
        ]
    for lst in board:
        print(lst)
    print('\nSOLVES TO\n')
    solve(0, 0, board)
    for lst in board:
        print(lst)