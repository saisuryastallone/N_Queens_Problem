from random import randint

board = []

N = int(input("Enter the number of queens to be placed: "))

for i in range(N):
    board.append(list(0 for i in range(N)))


# To print the Solution Matrix
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def isSafe(board, row, col):
    # Check Row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check Upper Diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check Lower Diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQueens(board, col):
    # Reaching the column N indicates that all queens are placed
    if col == N:
        return True

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1

            if solveNQueens(board, col + 1):
                return True

            board[i][col] = 0

    return False


if solveNQueens(board, 0):
    printSolution(board)
else:
    print("Solution doesn't exist")
