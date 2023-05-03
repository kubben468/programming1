def checkVictory(player1_choice, player2_choice):
    """checks which player wins with players input"""
    if player1_choice == player2_choice:
        return "tie"
    elif player1_choice == "R" and player2_choice == "S":
        return "player 1"
    elif player1_choice == "P" and player2_choice == "R":
        return "player 1"
    elif player1_choice == "S" and player2_choice == "P":
        return "player 1"
    else:
        return "player 2"



def main():
    player1_choice = input("Player 1, enter your choice (R/P/S): ")
    player2_choice = input("Player 2, enter your choice (R/P/S): ")

    winner = checkVictory(player1_choice, player2_choice)
    if winner == "tie":
        print("It's a tie!")
    else:
        print(f"{winner.capitalize()} won!")

if __name__ == "__main__":

    main()