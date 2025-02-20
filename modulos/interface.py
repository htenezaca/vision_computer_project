import PySimpleGUI as sg


def create_window():
    sg.theme('DarkAmber')

    layout = [
        [sg.Text('Filtros de Visión por Computadora')],
        [
         sg.Checkbox('Blur Filter', key='BLUR'),
         sg.Checkbox('Canny Filter', key='CANNY'),
         sg.Checkbox('Sobel Filter', key='SOBEL'), 
         sg.Checkbox('Grayscale', key='GRAY')],

        [sg.Text('Detectores de Visión por Computadora')],
        [
         sg.Checkbox('HarrisCorner Detector', key='HARRISCORNER'),
         sg.Checkbox('FAST Detector', key='FAST'),
         sg.Checkbox('SIFT Detector', key='SIFT')],
        
        [sg.Text('Segmentadores de Vision por Computadora')],
        [
         sg.Checkbox('Thresholding', key='THRESHOLDING'),
         sg.Checkbox('Color Segmentation', key='COLORSEGM'),
         sg.Checkbox('Border Detector Segmentation', key='BORDECTSEGM')],

        [sg.Text('Selecciona el espacio de color:')],
        [sg.Combo(['HSV', 'LAB'], default_value='HSV', key='COLOR_SPACE')],

        [sg.Button('Iniciar'), sg.Button('Detener'), sg.Button('Salir')]

    ]

    return sg.Window('Aplicación de Filtros y Detectores de Bordes', layout)