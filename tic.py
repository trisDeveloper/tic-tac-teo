import random


def print_tem(tem):
    for row in tem:
        print("|", " | ".join(row), "|")
        print("-" * 12)


# check who wins
def winner(tem, player):
    for row in tem:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(tem[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(tem[i][i] == player for i in range(3)) or all(
        tem[i][2 - i] == player for i in range(3)
    ):
        return True
    return False


# check if it's a tie
def is_tem_full(tem):
    for row in tem:
        if " " in row:
            return False
    return True


# move input
def play_move(tem, player):
    while True:
        try:
            if player == "X":
                row, col = map(
                    int,
                    input(
                        "your turn, enter row and column (e.g., 0 0 for top left): "
                    ).split(),
                )
            else:
                print("computer's turn:")
                # check if computer can win in the next move
                for i in range(3):
                    for j in range(3):
                        if tem[i][j] == " ":
                            tem[i][j] = player
                            if winner(tem, player):
                                return
                            tem[i][j] = " "
                # check if player can win in the next move
                for i in range(3):
                    for j in range(3):
                        if tem[i][j] == " ":
                            tem[i][j] = "X"
                            if winner(tem, "X"):
                                tem[i][j] = player
                                return
                            tem[i][j] = " "
                while True:
                    row, col = random.randint(0, 2), random.randint(0, 2)
                    if tem[row][col] == " ":
                        tem[row][col] = player
                        break
                break
            if tem[row][col] == " ":
                tem[row][col] = player
                break
            else:
                print("Invalid move! That spot is already taken.")
        except (ValueError, IndexError):
            print(
                "Invalid input! Please enter two integers (0, 1, 2) separated by a space."
            )


def play_game():
    tem = [[" "] * 3 for _ in range(3)]
    current_player = "X"

    while True:
        print_tem(tem)
        play_move(tem, current_player)
        if winner(tem, current_player):
            print_tem(tem)
            if current_player == "X":
                print(f"You wins!")
                break
            else:
                print(f"Computer wins!")
                break
        elif is_tem_full(tem):
            print_tem(tem)
            print("It's a tie :(")
            break
        else:
            current_player = "O" if current_player == "X" else "X"


play_game()
