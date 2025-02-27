import cv2
import numpy as np
from circledetect import CircleDetector

class SegmentationOpenCV:
    def __init__(self):
        self.__frame = None
        self.__mask = None
        self.__color_segmentation = None
        self.__circle_detector = CircleDetector()  # Detector de círculos

    def set_frame(self, frame):
        self.__frame = frame
        self.__frame_hsv = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2HSV)

    def apply_color_segmentation(self):

        if self.__mask is None:
            return self.__frame

        self.__color_segmentation = cv2.bitwise_and(self.__frame, self.__frame, mask=self.__mask)
        return self.__color_segmentation
    
    def apply_border_detector(self):
        if self.__mask is None:
            print("Error: No se puede detectar bordes sin una segmentación previa.")
            return self.__frame

        edges = cv2.Canny(self.__mask, 50, 150)

        frame_with_edges = cv2.bitwise_and(self.__frame, self.__frame, mask=edges)

        return frame_with_edges

    def draw_detected_circles(self):
        """
        Aplica la detección de círculos en la imagen segmentada.
        """
        if self.__mask is None:
            print("Error: No se puede detectar círculos sin una segmentación previa.")
            return self.__frame

        return self.__circle_detector.draw_detected_circles(self.__frame, self.__mask)


    def set_color_ranges(self, LOW_H, LOW_S, LOW_V, HIGH_H, HIGH_S, HIGH_V):
        self.__color_low_range = np.array([LOW_H, LOW_S, LOW_V], dtype=np.uint8)
        self.__color_high_range = np.array([HIGH_H, HIGH_S, HIGH_V], dtype=np.uint8)

        self.__mask = cv2.inRange(self.__frame_hsv, self.__color_low_range, self.__color_high_range)


    def apply_kmeans_segmentation(self, k=3):

        if self.__frame is None:
            print("Error: No se ha recibido un frame válido.")
            return None

        Z = self.__frame.reshape((-1, 3))
        Z = np.float32(Z)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        _, labels, centers = cv2.kmeans(Z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        centers = np.uint8(centers)
        segmented_image = centers[labels.flatten()]
        self.__color_segmentation = segmented_image.reshape(self.__frame.shape)

        return self.__color_segmentation