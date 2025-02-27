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

        try:
            while True:
                event, values = self.__window.read(timeout=20)

                if event in (sg.WIN_CLOSED, 'Salir'):
                    break

                if event == 'Iniciar' and self.__cap is None:
                    self.__start_camera()

                if event == 'Detener' and self.__cap is not None:
                    self.__release_camera()

                if self.__cap is not None and self.__cap.isOpened():
                    ret, frame = self.__cap.read()
                    if not ret:
                        print("Error: No se pudo leer el frame.")
                        break

                    frame = self.__process_frame(frame, values)

                    cv2.imshow('Video', frame)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break  

        except Exception as e:
            print(f"Error inesperado: {e}")

        finally:
            self.__release_camera()
            self.__window.close()

    def __start_camera(self):
        """Inicia la captura de video desde la cámara."""
        self.__cap = cv2.VideoCapture(0)

        if not self.__cap.isOpened():
            print("Error: No se pudo acceder a la cámara.")
            self.__cap = None


    def __process_frame(self, frame, values):
        """Procesa el frame aplicando segmentación y detección según la GUI."""
        if frame is None or not isinstance(frame, np.ndarray):
            return None  # Si no hay frame, no hacer nada

        self.__segmentation.set_frame(frame)

        if values.get('SEGMHSV', False):
            low_hsv = (values.get('LOW_H', 0), values.get('LOW_S', 0), values.get('LOW_V', 0))
            high_hsv = (values.get('HIGH_H', 255), values.get('HIGH_S', 255), values.get('HIGH_V', 255))
            self.__segmentation.set_color_ranges(*low_hsv, *high_hsv)
            frame = self.__segmentation.apply_color_segmentation()

        if values.get('DRAWCIRC', False):
            frame = self.__segmentation.draw_detected_circles()

        if values.get('SEGMKMEANS', False):  
            frame = self.__segmentation.apply_kmeans_segmentation(k=5)

        if values.get('DECTCONT', False):
            frame = self.__segmentation.apply_border_detector()

        return frame



    def __release_camera(self):
        if self.__cap is not None:
            self.__cap.release()
            self.__cap = None
        cv2.destroyAllWindows()

if __name__ == '__main__':
    video_processor = VideoProcessor()
