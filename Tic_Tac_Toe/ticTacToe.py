board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

gameEnded = False
currentPlayer = "X"

def printBoard(board):
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]}")
        if i < 2:
            print("---+---+---")

def hasWon(player, board):
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player or
            board[0][i] == player and board[1][i] == player and board[2][i] == player):
            return True
        
        if (board[0][2] == player and board[1][1] == player and board[2][0] or
            board[0][0] == player and board[1][1] == player and board[2][2]):
            return True
    return False 

def isDrawn(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

# Main execution

while not gameEnded: 
    printBoard(board)

    print(f"Player {currentPlayer}, your turn. Enter row and column(1, 2, and 3 only)")
    row = (int(input("Enter row: ")) - 1)
    column = (int(input("Enter column: ")) - 1)

    if (row < 0 or row > 2 or column < 0 or column > 2):
        print("Inaccessible cell, Try Again")
        continue

    if board[row][column] != " ":
        print("Cell is already filled, Try another cell")
        continue

    board[row][column] = currentPlayer

    if hasWon(currentPlayer, board):
        printBoard(board)
        print(f"Player {currentPlayer} wins!")
        gameEnded = True
    elif isDrawn(board):
        printBoard(board)
        print("Game is draw!")
        gameEnded = True
    else:
        if currentPlayer == "X":
            currentPlayer = "O"
        else:
            currentPlayer = "X"