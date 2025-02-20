import cv2
import numpy as np
from modulos.filters import FilterOpenCV
from modulos.detectors import DetectorOpenCV
from modulos.segmentations import Segmentation
from modulos.interface import create_window
import PySimpleGUI as sg

class VideoProcessor:
    def __init__(self):
        self.__window = create_window()
        self.__cap = None
        self.__filters = FilterOpenCV()
        self.__detectors = DetectorOpenCV()
        self.__segmentation = Segmentation()
        while True:
            event, values = self.__window.read(timeout=20)

            if event in (sg.WIN_CLOSED, 'Salir'):
                break

            if event == 'Iniciar' and self.__cap is None:
                self.__cap = cv2.VideoCapture(0)

            if event == 'Detener' and self.__cap is not None:
                self.__cap.release()
                self.__cap = None
                cv2.destroyAllWindows()

            if self.__cap is not None and self.__cap.isOpened():
                ret, frame = self.__cap.read()
                if not ret:
                    break
                
                self.__filters.set_frame(frame)
                self.__detectors.set_frame(frame)
                self.__segmentation.set_frame(frame)
                self.__segmentation.set_color_range()

                if values['BLUR']:
                    frame = self.__filters.apply_blur()

                if values['CANNY']:
                    frame = self.__filters.apply_canny()

                if values['SOBEL']:
                    frame = self.__filters.apply_sobel()

                if values['GRAY']:
                    frame = self.__filters.apply_gray()
                
                if values['HARRISCORNER']:
                    frame = self.__detectors.apply_detect_harris_corner()

                if values['FAST']:
                    frame = self.__detectors.apply_detect_FAST()
                    
                if values ['SIFT']:
                    frame = self.__detectors.apply_detect_SIFT()

                if values['THRESHOLDING']:
                    frame = self.__segmentation.apply_thresholding()

                if values ['COLORSEGM']:
                    color_space = values['COLOR_SPACE']
                    frame = self.__segmentation.apply_color_segmentation(color_space=color_space)

                if values ['BORDECTSEGM']:
                    frame = self.__segmentation.apply_segmentation_border_detection()
                                
                cv2.imshow('Video', frame)

        if self.__cap is not None:
            self.__cap.release()
        cv2.destroyAllWindows()
        self.__window.close()

if __name__ == '__main__':
 video_processor = VideoProcessor()