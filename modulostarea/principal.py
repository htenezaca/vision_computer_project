import cv2
import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg
from segmentation import SegmentationOpenCV
from colorange import ColorRange
from interface import create_interface


class VideoProcessor:
    def __init__(self):
        self.__window = create_interface()
        self.__cap = None
        self.__segmentation = SegmentationOpenCV()
        self.__colorange = ColorRange()
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
                self.__segmentation.set_frame(frame)           
                
                if values['SEGMHSV']:
                    color_space = 'HSV'
                    low_hsv = (values['LOW_H'], values['LOW_S'], values['LOW_V'])
                    high_hsv = (values['HIGH_H'], values['HIGH_S'], values['HIGH_V'])
                    self.__segmentation.set_color_ranges(*low_hsv, *high_hsv)
                    frame = self.__segmentation.apply_color_segmentation(color_space=color_space)
  
                if values['DECTCONT']:
                    frame = self.__segmentation.apply_border_detector()

                if values['DRAWCIRC']:
                    frame = self.__segmentation.draw_detected_circles()

                cv2.imshow('Video', frame)


        if self.__cap is not None:
            self.__cap.release()
        cv2.destroyAllWindows()
        self.__window.close()

if __name__ == '__main__':
 video_processor = VideoProcessor()