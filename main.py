import game
import playerChoice
import captureImage
from cv2 import cv2

'''
# RULES #
1. Capture image on background by pressing 'b' key. Make sure there are no moving objects in frame
2. Put hand in frame with desired move and then click space key
3. Press space key again to keep playing

Notes: 
- press 'r' key to reset background
- press 'esc' key to exit

'''

if(__name__ == "__main__"):
    background = captureImage.getBackground()
    # if reset # captureImage.removeBackground()

    image = captureImage.getImage()
    move = playerChoice.getChoice(image, background)
    game.play(move)