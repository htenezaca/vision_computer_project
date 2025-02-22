import cv2
import numpy as np

def apply_blur(frame):
    return cv2.GaussianBlur(frame, (15, 15), 0)

def apply_canny(frame):
    return cv2.Canny(frame, 100, 200)

def apply_gray(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def apply_threshold(frame, threshold_value):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
    return thresh
