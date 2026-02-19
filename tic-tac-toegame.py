import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board(board):
    print("\n")
    print("       TIC TAC TOE")
    print("  ----------------------")
    print(f"       {board[0]} | {board[1]} | {board[2]} ")
    print("      ---+---+---")
    print(f"       {board[3]} | {board[4]} | {board[5]} ")
    print("      ---+---+---")
    print(f"       {board[6]} | {board[7]} | {board[8]} ")
    print("  ----------------------\n")


def check_win(board, player):
    win_position = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]

    for pos in win_position:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def get_valid_moves(board,player_name):
    while True:
        try:
            move = int(input(f"{player_name}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid input. Please enter a number between 1 and 9.")
            elif board[move] != " ":
                print("That position is already taken. Try again.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def play_game(player1,player2,scores):
    board = [" "] * 9
    current_player = "X"
    current_name = player1

    for turn in range(9):
        clear_screen()
        print(f"Scores: {player1} - {scores[player1]}, {player2} - {scores[player2]}")
        print_board(board)
        move = get_valid_moves(board,current_name)
        board[move] = current_player

        if check_win(board, current_player):
            clear_screen()
            print_board(board)
            print(f"Congratulations {current_name}! You win!")
            scores[current_name] += 1
            return
        
        if current_player == "X":
            current_player = "O"
            current_name = player2
        else:
            current_player = "X"
            current_name = player1
    clear_screen()
    print_board(board)
    print("It's a draw!")

def main():
    print("Welcome to Tic Tac Toe!")
    player1 = input("Enter name for Player 1 (X): ")
    player2 = input("Enter name for Player 2 (O): ")
    scores = {player1: 0, player2: 0}

    while True:
        play_game(player1, player2, scores)
        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'yes':
            print("Final Scores:")
            print(f"Final Scores: {player1} - {scores[player1]}")
            print(f"Final Scores: {player2} - {scores[player2]}")
            print("Thanks for playing!")
            break
if __name__ == "__main__":
    main()