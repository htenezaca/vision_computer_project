import cv2
import numpy as np

class CircleDetector:
    def __init__(self):
        self.__circle_detect = []

    def detect_circles(self, segmented_mask, dp=1.2, minDist=30, param1=50, param2=40, minRadius=10, maxRadius=100):
        """
        Detecta círculos en la imagen segmentada por color HSV usando la Transformada de Hough.

        :param segmented_mask: Imagen binaria segmentada por color HSV.
        :param dp: Resolución inversa de la acumuladora HoughCircles.
        :param minDist: Distancia mínima entre los círculos detectados.
        :param param1: Primer umbral para el detector de bordes Canny.
        :param param2: Segundo umbral para la detección de círculos.
        :param minRadius: Radio mínimo de los círculos a detectar.
        :param maxRadius: Radio máximo de los círculos a detectar.
        :return: Lista de círculos detectados en formato (x, y, radio).
        """

        # Asegurar que la imagen está en escala de grises
        if len(segmented_mask.shape) == 3:
            segmented_mask = cv2.cvtColor(segmented_mask, cv2.COLOR_BGR2GRAY)

        # Aplicar morfología para eliminar ruido
        kernel = np.ones((5, 5), np.uint8)
        segmented_mask = cv2.morphologyEx(segmented_mask, cv2.MORPH_CLOSE, kernel)  # Cierra huecos pequeños
        segmented_mask = cv2.morphologyEx(segmented_mask, cv2.MORPH_OPEN, kernel)   # Reduce ruido

        # 2Suavizar la imagen para mejorar la detección
        blurred = cv2.GaussianBlur(segmented_mask, (9, 9), 2)

        # Aplicar la Transformada de Hough para detectar círculos
        circles = cv2.HoughCircles(
            blurred,
            cv2.HOUGH_GRADIENT,
            dp=dp,
            minDist=minDist,
            param1=param1,
            param2=param2,
            minRadius=minRadius,
            maxRadius=maxRadius
        )

        if circles is not None:
            circles = np.uint16(np.around(circles))
            self.__circle_detect = self.__filtrar_circulos(circles[0])

        return self.__circle_detect

    def __filtrar_circulos(self, circles, umbral_distancia=20):
        """
        Filtra círculos duplicados basados en su posición y radio.

        :param circles: Lista de círculos detectados por HoughCircles.
        :param umbral_distancia: Distancia mínima para considerar círculos como duplicados.
        :return: Lista filtrada de círculos únicos.
        """
        circulos_filtrados = []

        for c in circles:
            x, y, r = c
            agregar = True

            for cf in circulos_filtrados:
                x_cf, y_cf, r_cf = cf
                distancia = np.sqrt((x - x_cf) ** 2 + (y - y_cf) ** 2)
                if distancia < umbral_distancia and abs(r - r_cf) < umbral_distancia:
                    agregar = False
                    break

            if agregar:
                circulos_filtrados.append((x, y, r))

        return circulos_filtrados

    def draw_detected_circles(self, frame, segmented_mask):
        """
        Dibuja los círculos detectados sobre la imagen segmentada.

        :param frame: Imagen original en color.
        :param segmented_mask: Imagen segmentada en la que se detectaron los círculos.
        :return: Imagen con los círculos dibujados.
        """

        detected_circles = self.detect_circles(segmented_mask)

        if detected_circles:
            output = frame.copy()  # Para no modificar la imagen original
            for x, y, r in detected_circles:
                cv2.circle(output, (x, y), r, (0, 0, 255), 2)  # Dibujar borde del círculo
                cv2.circle(output, (x, y), 3, (255, 0, 0), -1)  # Dibujar centro del círculo

            return output

        return frame 
