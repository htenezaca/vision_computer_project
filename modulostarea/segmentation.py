import cv2
import numpy as np
from colorange import ColorRange


class SegmentationOpenCV:
    def __init__(self):
        self.__frame = None
        self.__frame_hsv = None
        self.__mask = None
        self.__color_segmentation = None
        self.__detect_border = None
        self.__colorange = ColorRange()
        self.__circle_detect = []
    def set_frame(self, frame):
        self.__frame = frame
        self.__frame_hsv = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2HSV)

    def set_color_ranges(self, LOW_H, LOW_S, LOW_V, HIGH_H, HIGH_S, HIGH_V):
        self.__colorange.set_color_ranges(LOW_H, LOW_S, LOW_V, HIGH_H, HIGH_S, HIGH_V)
        
    def apply_color_segmentation(self, color_space='HSV'):
        if color_space == 'HSV':
            mask = cv2.inRange(self.__frame_hsv, self.__colorange.color_low_range, self.__colorange.color_high_range)
            self.__mask = mask 
            self.__color_segmentation = cv2.bitwise_and(self.__frame, self.__frame, mask=mask)
            return self.__color_segmentation
        return self.__color_segmentation
    
    def apply_border_detector(self):
        contours, _ = cv2.findContours(self.__mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.__detect_border = cv2.drawContours(self.__color_segmentation, contours, -1, (0, 255, 0), 2)
        return self.__detect_border
    
    def detect_circles(self):
        circles = cv2.HoughCircles(self.__mask, cv2.HOUGH_GRADIENT, dp=1, minDist=10, param1=20, param2=20, minRadius=0, maxRadius=0)
        
        if circles is not None:
            circles = np.uint8(np.around(circles)) 
            circles_unlimited = [(circle[0], circle[1], circle[2]) for circle in circles[0]]  
            self.__circle_detect = circles_unlimited
            return self.__circle_detect
        return []

    def draw_detected_circles(self):
        detected_circles = self.detect_circles() 
        
        if detected_circles:
            for circle in detected_circles:
                cv2.circle(self.__color_segmentation, (circle[0], circle[1]), circle[2], (0, 0, 255), 2)  
                cv2.circle(self.__color_segmentation, (circle[0], circle[1]), 5, (0, 0, 255), -1) 
                
            return self.__color_segmentation      
        
    def apply_kmeans_segmentation(self, k=5):
        Z = self.__frame.reshape((-1, 5))
        Z = np.float32(Z)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        _, labels, centers = cv2.kmeans(Z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        centers = np.uint8(centers)
        segmented_image = centers[labels.flatten()]
        self.__color_segmentation = segmented_image.reshape(self.__frame.shape)

        return self.__color_segmentation