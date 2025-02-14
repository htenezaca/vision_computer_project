import cv2
import numpy as np

def detect_harris_corners(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    frame[dst > 0.01 * dst.max()] = [0, 0, 255]
    return frame