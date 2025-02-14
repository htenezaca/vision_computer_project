# Proyecto Final de Visión por Computadora

## Descripción
Esta aplicación permite aplicar filtros de procesamiento de imágenes en tiempo real usando OpenCV y una interfaz gráfica construida con 
PySimpleGUI.

## Estructura del Proyecto
```
vision_app/
├── main.py               # Código principal para correr la app
├── filters
|───gaussianBlur.py            # Funciones de filtros de imagen
├── detectors.py          # Funciones para detección de puntos de interés
├── interface.py          # Código para la interfaz gráfica (GUI)
├── resources/            # Carpeta para videos o imágenes de prueba
├── requirements.txt      # Dependencias del proyecto
├── .gitignore            # Archivos y carpetas a ignorar por Git
└── README.md             # Instrucciones y objetivos del proyecto
```

## Instalación
1. Clonar el repositorio.
2. Crear y activar un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```
3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso
Ejecutar la aplicación con:
```bash
python main.py
```

Selecciona los filtros que quieres aplicar y observa los resultados en tiempo real.

## Extensiones
- Agrega tus propios filtros en `filters.py`.
- Implementa detección de puntos de interés en `detectors.py`.
- Personaliza la interfaz en `interface.py`.


