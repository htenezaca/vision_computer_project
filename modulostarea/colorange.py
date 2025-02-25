import cv2
import numpy as np

class ColorRange:
    def __init__(self):
        self.color_low_range = None
        self.color_high_range = None

    def set_color_ranges(self, LOW_H, LOW_S, LOW_V, HIGH_H, HIGH_S, HIGH_V):
        self.color_low_range = np.array([LOW_H, LOW_S, LOW_V], dtype=np.uint8)
        self.color_high_range = np.array([HIGH_H, HIGH_S, HIGH_V], dtype=np.uint8)