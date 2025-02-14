import cv2
from filters import apply_blur, apply_canny, apply_gray
from interface import create_window
import PySimpleGUI as sg


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

            cv2.imshow('Video', frame)

    if cap is not None:
        cap.release()
    cv2.destroyAllWindows()
    window.close()


if __name__ == '__main__':
    main()