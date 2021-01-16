''' Dice Game Simulator'''
import random

def dice_roll():
    DiceRoll = random.randint(1,6)
    return DiceRoll

def DiceGame():
    player1 = input("Enter the name of Player 1: ")
    player2 = input("Enter the name of Player 2: ")
    player1_score = 0
    player2_score = 0
    rounds = 0
    player1_wins = 0
    player2_wins = 0

    while rounds < 10:
        player1_score = dice_roll()
        print(f"{player1} rolls: {player1_score}")
        player2_score = dice_roll()
        print(f"{player2} rolls: {player2_score}")

        rounds += 1
        
        if player1_score == player2_score:
            print(f"round {rounds} result is Draw\n")
        elif player1_score > player2_score:
            print(f"{player1} wins in round {rounds}\n")
            player1_wins += 1
        else:
            print(f"{player2} wins in round {rounds}\n")
            player2_wins += 1

    if player1_wins == player2_wins:
        print("Final result of the game is Draw")

    elif player1_wins > player2_wins:
        if player2_wins <=1:
            print(f"{player1} wins total {player1_wins} rounds, {player2} wins total {player2_wins} round. Congratulations! {player1} is the winner of the Game\n")
        else:
            print(f"{player1} wins total {player1_wins} rounds, {player2} wins total {player2_wins} rounds. Congratulations! {player1} is the winner of the Game\n")

    else:
        if player1_wins <=1:
            print(f"{player2} wins total {player2_wins} rounds, {player1} wins total {player1_wins} round. Congratulations! {player2} is the winner of the Game\n")
        else:
            print(f"{player2} wins total {player2_wins} rounds, {player1} wins total {player1_wins} rounds. Congratulations! {player2} is the winner of the Game\n")
        
DiceGame()