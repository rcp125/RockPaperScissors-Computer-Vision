from cv2 import cv2


def getBackground():
    bg = cv2.createBackgroundSubtractorMOG2(0, 50)
    print('Background Captured')
    return bg

def removeBackground():
    bg = None
    return bg


def getImage():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("cap")

    while True:
        ret, frame = cam.read()
        cv2.imshow("cap", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Exiting...")
            break
        elif k%256 == 32:
            # SPACE pressed
            print("frame captured")
            return frame