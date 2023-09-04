import random
import os


def Game():
    os.system("cls")
    print("| Welcome to Rock Paper Scissor Game |")
    print("\nRules of Game are:")
    print("1. Rock beats scissor.\n2. Scissor beats paper.\n3. Paper beats rock.\n")

    Choices = ["rock", "paper", "scissor"]
    PlayerCounter = 0
    ComputerCounter = 0

    while (PlayerCounter >= 0 and PlayerCounter < 3) and (ComputerCounter >= 0 and ComputerCounter < 3):
        PlayerChoice = input("Enter your choice (rock | paper | scissor): ")
        while PlayerChoice not in Choices:
            PlayerChoice = input("\nWrong Entry! Enter your choice (rock | paper | scissor): ")
        ComputerChoice = random.choice(Choices)

        print("Player chooses:", PlayerChoice)
        print("Computer chooses:", ComputerChoice)

        if PlayerChoice == ComputerChoice:
            print("\nIt's a draw!")
        elif (
            (PlayerChoice == "rock" and ComputerChoice == "scissor") or
            (PlayerChoice == "paper" and ComputerChoice == "rock") or
            (PlayerChoice == "scissor" and ComputerChoice == "paper")
        ):
            print("\nYou win!\n")
            ComputerCounter += 1
            if (PlayerCounter > 0 and PlayerCounter <= 3):
                PlayerCounter -= 1
        else:
            print("\nComputer wins!\n")
            PlayerCounter +=1
            if (ComputerCounter > 0 and ComputerCounter <= 3):
                ComputerCounter -= 1
    if PlayerCounter == 3:
        print("Game finished. Winner is: Computer.")
    else:
        print("Game finished. Winner is: You.")
    Again = input("\n\nDo you want to play again? (y/n): ")
    if Again == "y":
        Game()
    else:
        exit()


Game()