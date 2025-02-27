import cv2
import numpy as np


class DetectorOpenCV:
    def __init__(self):
        self.__frame = None
        self.__gray_frame = None
        

    def set_frame(self, frame):
        self.__frame = frame 
        self.__gray_frame = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2GRAY)
        return self.__gray_frame
    
    def apply_detect_harris_corner(self, x):
        gray = np.float32(self.__gray_frame)
        dst = cv2.cornerHarris(gray, x, 3, 0.04)
        self.__frame[dst > 0.01 * dst.max()] = [0, 0, 255]
        return self.__frame
    
    def apply_detect_FAST(self):
        fast = cv2.FastFeatureDetector.create()
        keypoints = fast.detect(self.__gray_frame, None)
        self.__frame = cv2.drawKeypoints(self.__frame, keypoints, None, color=(255, 0, 0))
        return self.__frame

    def apply_detect_SIFT(self):
        sift =  cv2.SIFT.create()
        keypoints, descriptors = sift.detectAndCompute(self.__gray_frame, None)
        self.__frame = cv2.drawKeypoints(self.__frame, keypoints, None, color=(0, 255, 0))
        return self.__frame

        
    
        

