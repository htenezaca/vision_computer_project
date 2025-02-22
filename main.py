import cv2
import PySimpleGUI as sg
from filters import apply_blur, apply_canny, apply_gray, apply_threshold
from interface import create_window

def main():
    window = create_window()
    cap = None

    while True:
        event, values = window.read(timeout=20)

        if event in (sg.WIN_CLOSED, 'Salir'):
            break

        if event == 'Iniciar' and cap is None:
            cap = cv2.VideoCapture(0)

        if event == 'Detener' and cap is not None:
            cap.release()
            cap = None
            cv2.destroyAllWindows()

        if cap is not None and cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            if values['BLUR']:
                frame = apply_blur(frame)

            if values['CANNY']:
                frame = apply_canny(frame)

            if values['GRAY']:
                frame = apply_gray(frame)
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

            if values['THRESHOLD']:
                threshold_value = int(values['THRESH_VALUE'])  # Capturar el valor del slider
                frame = apply_threshold(frame, threshold_value)
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)  # Convertir a BGR para que OpenCV pueda mostrarlo

            cv2.imshow('Video', frame)

    if cap is not None:
        cap.release()
    cv2.destroyAllWindows()
    window.close()

if __name__ == '__main__':
    main()
