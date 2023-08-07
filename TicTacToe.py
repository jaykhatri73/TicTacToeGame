# to print game board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# to check winner
def check_winner(board):
    # to check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != " ":
            return row[0]

    # to check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # to check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # if there is no winner
    return None

# main function


def play_game():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    # game starts with X and keeps switching between X and O
    current_player = "X"

    while True:
        print_board(board)

        # to take position from user
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        # if there is already a value at the user given position
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player

        # to check winner after each move
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a tie!")
            break

        # to switch between players
        current_player = "O" if current_player == "X" else "X"


play_game()
