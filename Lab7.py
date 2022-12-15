# Program of N-Queens

def Display(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

def isSafe(board, row, col):
    # For checking row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Checking the upper left diagonal
    m = row
    n = col
    while (m >= 0 and n >= 0):
        if board[m][n] == 1:
            return False
        m -= 1
        n -= 1

    # Checking lower diagonal on left side
    m = row
    n = col
    while (m < N and n >= 0):
        if board[m][n] == 1:
            return False
        m += 1
        n -= 1
    return True

def solveNQueens(board, col=0):
    if col == N:
        return True

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQueens(board, col+1):
                return True
            board[i][col] = 0
    return False


N = int(input("Enter the number of Queens: "))
Board = [[0 for i in range(N)] for j in range(N)]

if solveNQueens(Board) == False:
    print("Enter valid Input!")
else:
    Display(Board)
