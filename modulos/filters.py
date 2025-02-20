import cv2


class FilterOpenCV:
    def __init__(self):
        self.__frame = None
        self.__gray_frame = None

    def set_frame(self, frame):
        self.__frame = frame
        self.__gray_frame = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2GRAY) 

    def apply_blur(self, ksize=(15,15)):
        return cv2.GaussianBlur(self.__frame, ksize, 0)

    def apply_canny(self):
        return cv2.Canny(self.__frame, 100, 200)
    
    def apply_sobel (self, ksize=(15,15)):
        sobel_filter_x = cv2.Sobel(self.__gray_frame, cv2.CV_64F, 1, 0, ksize)
        sobel_filter_y = cv2.Sobel(self.__gray_frame, cv2.CV_64F, 0, 1, ksize)
        return cv2.magnitude(sobel_filter_x, sobel_filter_y)

    def apply_gray(self):
        return self.__gray_frame 
