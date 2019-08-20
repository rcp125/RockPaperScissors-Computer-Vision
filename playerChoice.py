from cv2 import cv2
import numpy as np
import math

def getChoice(image, background):
    if background == None:
        print("Set background first")
        return
    mask = applyMask(image, background)
    thres = preprocess(mask)
    fingerCount = getFingerCount(thres, image)
    if(fingerCount == 0):
        return "Rock"
    elif(fingerCount == 2):
        return "Scissors"
    elif(fingerCount == 5):
        return "Paper"
    else:
        print("Not valid option")
        return

def applyMask(image, background):
    foregroundMask = background.apply(image, learningRate = 0)
    kernel = np.ones((3, 3), np.uint8)
    foregroundMask = cv2.erode(foregroundMask, kernel, iterations=1)
    res = cv2.bitwise_and(image, image, mask=foregroundMask)
    return res

def preprocess(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (40, 40), 0)
    cv2.imshow('blur', blur)
    _, thres = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)
    return thres

def getFingerCount(thres, image):
    contours, _ = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    length = len(contours)
    maxArea = -1
    if length > 0:
        for i in range(length):  # find the biggest contour (according to area)
            temp = contours[i]
            area = cv2.contourArea(temp)
            if area > maxArea:
                maxArea = area
                ci = i

        res = contours[ci]
        hull = cv2.convexHull(res)
        drawing = np.zeros(image.shape, np.uint8)
        cv2.drawContours(drawing, [res], 0, (0, 255, 0), 2)
        cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 3)

        _,cnt = calculateFingers(res,drawing)
        print(cnt)
        return cnt


def calculateFingers(res,drawing):  # -> finished bool, cnt: finger count
    #  convexity defect
    hull = cv2.convexHull(res, returnPoints=False)
    if len(hull) > 3:
        defects = cv2.convexityDefects(res, hull)
        if type(defects) != type(None):  # avoid crashing.   (BUG not found)

            cnt = 0
            for i in range(defects.shape[0]):  # calculate the angle
                s, e, f, d = defects[i][0]
                start = tuple(res[s][0])
                end = tuple(res[e][0])
                far = tuple(res[f][0])
                a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # cosine theorem
                if angle <= math.pi / 2:  # angle less than 90 degree, treat as fingers
                    cnt += 1
                    cv2.circle(drawing, far, 8, [211, 84, 0], -1)
            return True, cnt
    return False, 0