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
source venv/bin/activate  # En Windows: venv/Scripts/activate
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

## Aquí va a ir el informe

# Informe del Proyecto de Visión por Computadora

## Presentación y Explicación de Código

### Estructura del Proyecto

El proyecto está organizado en varios módulos, cada uno con una función específica:

1. **detectors.py**: Este módulo se encarga de aplicar los diferentes detectores disponibles.
2. **filters.py**: Este módulo se encarga de aplicar los filtros a la imagen capturada por la cámara.
3. **segmentations.py**: Este módulo realiza la segmentación de la imagen en función de los colores seleccionados.
4. **interface.py**: Este módulo define la interfaz gráfica de usuario (GUI) utilizando PySimpleGUI.
5. **main.py**: Este es el punto de entrada del programa, donde se integran todos los módulos y se controla el flujo de la aplicación.

### Explicación de Cada Módulo

#### 1. Módulo `detectors.py`

Este módulo implementa la clase `DetectorOpenCV`, que incluye métodos para detectar características en las imágenes:

- **`set_frame`**: Establece el frame actual y lo convierte a escala de grises.
- **`apply_detect_harris_corner`**: Aplica el detector de esquinas de Harris para identificar puntos de interés en la imagen.
- **`apply_detect_FAST`**: Utiliza el detector de características rápidas (FAST) para encontrar puntos clave en la imagen.
- **`apply_detect_SIFT`**: Aplica el algoritmo SIFT (Scale-Invariant Feature Transform) para detectar y describir características en la imagen.

**Decisiones de Diseño**: Elegí estos detectores debido a su eficacia en la identificación de características en imágenes, lo que es fundamental para aplicaciones de visión por computadora.

#### 2. Módulo `filters.py`

Este módulo implementa la clase `FilterOpenCV`, que proporciona métodos para aplicar diferentes filtros a la imagen:

- **`set_frame`**: Establece el frame actual y lo convierte a escala de grises.
- **`apply_blur`**: Aplica un filtro de desenfoque gaussiano a la imagen.
- **`apply_canny`**: Aplica el detector de bordes de Canny.
- **`apply_sobel`**: Aplica el filtro Sobel para detectar bordes en la imagen.
- **`apply_gray`**: Devuelve la imagen en escala de grises.

**Decisiones de Diseño**: escogí estos filtros para mejorar la calidad de la imagen y facilitar la detección de características y bordes.

#### 3. Módulo `segmentations.py`

Este módulo implementa la clase `Segmentation`, que se encarga de la segmentación de la imagen:

- **`set_frame`**: Establece el frame actual y lo convierte a los espacios de color HSV y LAB.
- **`set_color_range`**: Define los rangos de color para la segmentación.
- **`apply_thresholding`**: Aplica un umbral a la imagen.
- **`apply_color_segmentation`**: Realiza la segmentación de color en función del espacio de color seleccionado (HSV o LAB).
- **`apply_segmentation_border_detection`**: Aplica el detector de bordes de Canny.

**Decisiones de Diseño**: escogí los espacios de color HSV y LAB porque son más robustos para la segmentación de colores en comparación con el espacio de color RGB.

#### 4. Módulo `interface.py`

Este módulo define la interfaz gráfica de usuario utilizando PySimpleGUI. Permite al usuario seleccionar diferentes filtros, detectores y opciones de segmentación.

**Decisiones de Diseño**: Yo utilicé PySimpleGUI por su simplicidad y facilidad de uso, lo que permite crear interfaces gráficas de manera rápida y efectiva.

#### 5. Módulo `main.py`

Este es el punto de entrada del programa, aquí se inicializan los módulos y se controla el flujo de la aplicación, también, se captura el video de la cámara, se aplican los filtros y detectores seleccionados, y se muestra el resultado en una ventana.

### Argumentación de Decisiones

Las decisiones que eh tomado en la selección de algoritmos, la estructura de datos y una buena optimización de cada uno, me en la eficacia y la facilidad de implementación que se pueda ofrecer, también, los algoritmos utilizados se encuentran bien establecidos en la documentación de OpenCV, por ejemplo, los filtros gaussian blur o sobel, los detectores FAST o SIFT, las segmentaciones por umbral o por detección de borders y el diseño mediante el uso de PySimpleGUI.

### Posibles Mejoras y Optimizaciones

1. **Ajuste de Rangos de Color**: Implementar un método para calibrar automáticamente los rangos de color en función de la iluminación y el entorno. Esto podría incluir un selector de color en tiempo real.

2. **Optimización de Rendimiento**: Considerar el uso de técnicas de procesamiento en paralelo o en hilos para mejorar el rendimiento, especialmente al aplicar múltiples filtros y detectores.

3. **Interfaz de Usuario Mejorada**: Agregar más opciones en la interfaz para permitir al usuario ajustar parámetros como el tamaño del kernel para el desenfoque o los umbrales para el detector de Canny.

4. **Documentación y Comentarios**: Asegurarse de que el código esté bien documentado y que cada función tenga comentarios que expliquen su propósito y funcionamiento.

5. **Pruebas y Validación**: Implementar pruebas unitarias para cada módulo para garantizar que cada componente funcione correctamente y facilitar el mantenimiento del código.
