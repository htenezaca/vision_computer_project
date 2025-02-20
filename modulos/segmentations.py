import cv2
import numpy as np


class Segmentation:
    def __init__(self):
        self.__frame = None
        self.__frame_HSV = None
        self.__frame_LAB = None
        self.__thresholding_frame = None
        self.__color_high_range = None
        self.__color_low_range = None

    def set_frame(self, frame):
        self.__frame = frame
        if self.__frame is not None:
            self.__frame_HSV = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2HSV)
            self.__frame_LAB = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2LAB)

    def set_color_range(self):
        self.__color_low_range = np.array([20, 20, 70], dtype=np.uint8)
        self.__color_high_range = np.array([20, 255, 255], dtype=np.uint8)
        
    def apply_thresholding(self, thresh=100, maxvalue=255):
        _ , self.__thresholding_frame = cv2.threshold(self.__frame, thresh, maxvalue, cv2.THRESH_BINARY) 
        return self.__thresholding_frame
    
    def apply_color_segmentation(self, color_space=('HSV', 'LAB')):
        if color_space == 'HSV':
            mask = cv2.inRange(self.__frame_HSV, self.__color_low_range, self.__color_high_range)
            return cv2.bitwise_and(self.__frame, self.__frame, mask=mask)  
        elif color_space == 'LAB':
            mask= cv2.inRange(self.__frame_LAB, self.__color_low_range, self.__color_high_range)
            return cv2.bitwise_and(self.__frame, self.__frame, mask=mask)

    def apply_segmentation_border_detection(self):
        return cv2.Canny(self.__frame, 100, 200)





