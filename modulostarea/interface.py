import PySimpleGUI as sg

def create_interface():
    sg.theme('LightBrown3')

    layout = [
        [sg.Text('Segmentación y Detección')],
        [
        sg.Checkbox('Segmentación de Color HSV', key='SEGMHSV'),
        sg.Checkbox('Segmentación K-means', key='SEGMKMEANS'),
        sg.Checkbox('Detección de Contornos', key='DECTCONT'),
        sg.Checkbox('Dibujar Círculos', key='DRAWCIRC')],
        [sg.Text('Rango Bajo (H, S, V):')],
        [sg.Text('H'), sg.Slider(range=(0, 255), orientation='h', size=(20, 15), default_value=0, key='LOW_H')],
        [sg.Text('S'), sg.Slider(range=(0, 255), orientation='h', size=(20, 15), default_value=0, key='LOW_S')],
        [sg.Text('V'), sg.Slider(range=(0, 255), orientation='h', size=(20, 15), default_value=0, key='LOW_V')],
        [sg.Text('Rango Alto (H, S, V):')],
        [sg.Text('H'), sg.Slider(range=(0, 255), orientation='h', size=(20, 15), default_value=179, key='HIGH_H')],
        [sg.Text('S'), sg.Slider(range=(0, 255), orientation='h', size=(20, 15), default_value=255, key='HIGH_S')],
        [sg.Text('V'), sg.Slider(range=(0, 255), orientation='h', size=(20, 15), default_value=255, key='HIGH_V')],

        [sg.Combo(['HSV'], default_value='HSV', key='COLOR_SPACE', readonly=True)],
        [sg.Button('Iniciar'), sg.Button('Detener'), sg.Button('Salir')]

    ]
    
    return sg.Window('Aplicación de Filtros y Detectores de Bordes', layout) 


