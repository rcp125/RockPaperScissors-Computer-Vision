from random import randint

win = 0
loss = 0

def play(playerChoice):
    global win
    global loss
    choices = ["Rock", "Paper", "Scissors"]
    computer = choices[randint(0,2)]
    player = playerChoice
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose...", computer, "beats", player)
            win = win + 1
            loss = loss + 1
        else:
            print("You win!", player, "beats", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose...", computer, "beats", player)
            loss = loss + 1
        else:
            print("You win!", player, "beats", computer)
            win = win + 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "beat", player)
            loss = loss + 1
        else:
            print("You win!", player, "beat", computer)
            win = win + 1
    else:
        print("That's not a valid move.")


def scoreLog():
    if(win > loss):
        print("You are winning. You lead " + str(win) + "-" + str(loss))
    elif(win < loss):
        print("You are losing. Computer leads " + str(win) + "-" + str(loss))
    else:
        print("You are tied. " + str(win) + "-" + str(loss))
