from random import randint

def play(playerChoice):
    choices = ["Rock", "Paper", "Scissors"]
    computer = choices[randint(0,2)]
    player = playerChoice
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose...", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose...", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "beat", player)
        else:
            print("You win!", player, "beat", computer)
    else:
        print("That's not a valid move.")
