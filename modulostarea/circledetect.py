import cv2
import numpy as np


class CircleDetector:
    def __init__(self):
        self.__circle_detect = None



    def detect_circles(self, mask):
        circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)
        
        if circles is not None:
            circles = np.uint16(np.around(circles)) 
            circles_unlimited = [(circle[0], circle[1], circle[2]) for circle in circles[0]]  
            self.__circle_detect = circles_unlimited
            return self.__circle_detect
        
        return [], self.__circle_detect
    
    
    

        
    