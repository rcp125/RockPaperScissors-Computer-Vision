from cv2 import cv2
import numpy as np
import math
import game

def image_process(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (35, 35), 0)
    _, thres = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)
    return thres

def removeBG(frame, bgModel):
    mask = bgModel.apply(frame,learningRate=0)
    kernel = np.ones((2, 2), np.uint8)
    mask = cv2.erode(mask, kernel)
    removed = cv2.bitwise_and(frame, frame, mask=mask)
    return removed


def find_max_contour(contours, img):
    maxArea = 0
    maxIndex = 0
    if len(contours) > 0:
        for i in range(len(contours)):
            curr = contours[i]
            area = cv2.contourArea(curr)
            if area > maxArea:
                maxArea = area
                maxIndex = i

        max_contour = contours[maxIndex]
        hull = cv2.convexHull(max_contour)
        drawing = np.zeros(img.shape, np.uint8)
        cv2.drawContours(drawing, [max_contour], 0, (0, 255, 0), 2)
        cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 3)

        cnt = calculateFingers(max_contour,drawing, img)

        return cnt

def calculateFingers(max_contour,drawing, img):
    hull = cv2.convexHull(max_contour, returnPoints=False)
    if len(hull) > 3:
        defects = cv2.convexityDefects(max_contour, hull)
        if type(defects) != type(None):
            cnt = 0
            for i in range(defects.shape[0]):  # calculate the angle
                s, e, f, _ = defects[i][0]
                start = tuple(max_contour[s][0])
                end = tuple(max_contour[e][0])
                far = tuple(max_contour[f][0])
                angle = calculateAngle(far, start, end)
                
                if angle <= math.pi / 2:
                    cnt += 1
                    cv2.circle(drawing, far, 8, [211, 84, 0], -1)
            return cnt
    return 0

def calculateAngle(far, start, end):
    a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
    b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
    c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
    angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    return angle


def open_camera():
    camera = cv2.VideoCapture(0)
    bgModel = None

    while camera.isOpened():
        _, frame = camera.read()
        frame = cv2.flip(frame, 1)
        cv2.rectangle(frame, (int(0.5 * frame.shape[1]), 0), (frame.shape[1], int(0.75 * frame.shape[0])), (255, 0, 0), 2)
        cv2.imshow('original', frame)

        if bgModel:
            removed = removeBG(frame, bgModel)
            cropped = removed[0:int(0.75 * frame.shape[0]), int(0.5 * frame.shape[1]):frame.shape[1]]
            cv2.imshow('removed', cropped)

            thres = image_process(cropped)
            contours, _ = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            count = find_max_contour(contours, cropped)

            # count = contours(thres, cropped)

        k = cv2.waitKey(10)
        if k == 27:
            camera.release()
            cv2.destroyAllWindows()
            print("Exiting...")
            break
        elif k == ord('b'):
            bgModel = cv2.createBackgroundSubtractorMOG2(0, 50)
            print("Background captured")
        elif k == ord('s') and bgModel:
            move = ""
            if(count == 0):
                move = "Rock"
            if(count == 1):
                move = "Scissors"
            if(count == 4):
                move = "Paper"
            game.play(move)
        elif k == ord("l"):
            game.scoreLog()