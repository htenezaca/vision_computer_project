import PySimpleGUI as sg

def create_window():
    sg.theme('DarkAmber')

    layout = [
        [sg.Text('Filtros de Visión por Computadora')],
        [sg.Checkbox('Blur', key='BLUR'),
         sg.Checkbox('Canny', key='CANNY'),
         sg.Checkbox('Grayscale', key='GRAY'),
         sg.Checkbox('Thresholding', key='THRESHOLD')],
        [sg.Text('Umbral:'), sg.Slider(range=(0, 255), orientation='h', size=(20, 15), default_value=127, key='THRESH_VALUE')],
        [sg.Button('Iniciar'), sg.Button('Detener'), sg.Button('Salir')]
    ]

    return sg.Window('Aplicación de Filtros', layout)
