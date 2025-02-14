import PySimpleGUI as sg


def create_window():
    sg.theme('DarkAmber')

    layout = [
        [sg.Text('Filtros de Visión por Computadora')],
        [sg.Checkbox('Blur', key='BLUR'),
         sg.Checkbox('Canny', key='CANNY'),
         sg.Checkbox('Grayscale', key='GRAY')],
        [sg.Button('Iniciar'), sg.Button('Detener'), sg.Button('Salir')]
    ]

    return sg.Window('Aplicación de Filtros', layout)