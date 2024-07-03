def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    move_history = []
    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (row and column): ")
        row, col = map(int, move.split())

        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player
        move_history.append((row, col))

        if len(move_history) > 6:  # Start deleting moves after the 6th move
            oldest_move = move_history.pop(0)
            board[oldest_move[0]][oldest_move[1]] = " "

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


while True:
    play_game()
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        break

print("Thank you for playing!")
