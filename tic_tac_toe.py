


def display_board(board):
    print("---------")
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("---------")


def check_win(board, player):
    # Check rows, columns, and diagonals
    return (
        any(all(cell == player for cell in row) for row in board) or
        any(all(row[i] == player for row in board) for i in range(3)) or
        all(board[i][i] == player for i in range(3)) or
        all(board[i][2 - i] == player for i in range(3))
    )


def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    # Initialize the board with empty spaces
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    
    while True:
        display_board(board)
        
        
        try:
            row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1
            if board[row][col] != " ":
                print("Cell is already occupied! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter numbers between 1 and 3.")
            continue
        
        
        board[row][col] = current_player
        
        
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        
        
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break
        
        
        current_player = "O" if current_player == "X" else "X"


play_game()
