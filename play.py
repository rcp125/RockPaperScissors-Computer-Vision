from cv2 import cv2
import capture_move
import game

def instructions():
    print("\n\nWelcome to RPS, Computer Vision Edition. \nTo get started, click on camera window and press 'b' key to set background. Do not show hand in the frame and make sure there are no moving objects.\nAfter capturing background, press 's' key to play a game.\nPress 'esc' key to exit game.\nFor score log, type 'score' into the terminal.")
    


def play_game():
    # user_move = input("Your selected move is: ")

    # game.play(user_move)
    capture_move.open_camera()


if __name__ == "__main__":
   instructions()
   play_game()