import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imagen = cv.imread('imaxes/photo2.png')
print(type(imagen))
"""
Para leer una imagen se utiliz a imread.
OpenCV-python trabaja con numpy, las imágenes leídas son de tipo ndarray... 
se puede aplicar todo lo que sabes de numpy.
Una imagen va a estar compuesta de planos de colores del mismo tamaño. 
Todos van a tener alto, ancho y el color en componentes BGR (ojo no RGB)

Esta imagen tiene 780 px de alto y 1170 de ancho
"""

plt.imshow(imagen)
plt.title('Imagen 1')
plt.show()
print(imagen.shape)

"""
Una vez leida se puede acceder a cada pixel individual a partir de las 
coordenadas del punto.
"""
px = imagen[100, 100]
print(px)

"""
El contenido de cada punto es un array de 3 elementos en formato BGR (Blue, Green, Red).
Importante tenerlo en cuenta si trabajas con otras librerías.
"""

"""
IMÁGENES EN BLANCO Y NEGRO
Las imágenes en escala de grises solo deberían tener un único canal. 
Pero muchos programas gráficos las almacenan como con 3 canales, con el mismo contenido.
Se puede solucionar en openCV con cv.IMREAD_GRAYSCALE
"""
imagen_2 = cv.imread('imaxes/photo3.png', cv.IMREAD_GRAYSCALE)
print(imagen_2.shape)
px2 = imagen_2[100, 100]
print(px2)
plt.subplot(1, 2, 1)
plt.imshow(imagen_2)
plt.title('Imagen2')
plt.subplot(1, 2, 2)
plt.imshow(imagen_2, cmap='gray', vmin=0, vmax=255)
plt.title('Imagen2 en gris')
plt.show()

"""
REGIONES
Muchas veces en vez de trabajar con px, se va a trabajar con regiones.
Las imágenes son arrays de numpy.
"""
recorte = imagen_2[350:800, 250:400]
plt.imshow(recorte)
plt.title('Recorte de imagen_2')
plt.show()

"""
Se puede asignar valores como en numpy
imagen_3[0:100,0:100] = 0
"""
imagen_3 = imagen_2.copy()
imagen_3[350:800, 450:600] = recorte
plt.imshow(imagen_3)
plt.title('Copiando cachos')
plt.show()

"""
AÑADIR BORDES
Se pueden añadir bordes, al estilo de marco en la imagen.
El borde que se añade puede variar en muchos aspectos
"""
constant = cv.copyMakeBorder(imagen_2, 50, 50, 50, 50, cv.BORDER_CONSTANT, value=[255])
plt.imshow(constant, cmap='gray', vmin=0, vmax=255)
plt.title('Añadido borde')
plt.show()

"""
GRABAR IMÁGENES
Las imágenes se pueden grabar en el disco
"""
cv.imwrite('imaxes/resultado1.png', constant)

"""
TRANSFORMACIONES
Es muy normal tener que transformar los imágenes:
1. ESCALADO
Consiste en tener que cambiar el tamaño de las imágenes(más grande o más pequeña)
Se usa el método resize
"""
print(f"Tamaño original: {imagen.shape[0]} x {imagen.shape[1]}")
escalado1 = cv.resize(imagen, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
print(f"Tamaño escalado: {escalado1.shape[0]} x {escalado1.shape[1]}")
print(escalado1)
plt.imshow(escalado1)
plt.title("Imagen el doble de grande")
plt.show()
print(f"Tamaño original: {imagen.shape[0]} x {imagen.shape[1]}")
escalado2 = cv.resize(imagen, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
print(f"Tamaño escalado: {escalado2.shape[0]} x {escalado2.shape[1]}")
plt.imshow(escalado2)
plt.title("Imagen mitad de tamaño")
plt.show()

"""
2. DESPLAZAMIENTO
Para desplazar las imágenes se precisa un desplazamiento para x y para y(tx,ty).
Con estos valores se crea una matriz de transformación M
"""
rows, cols, colors = imagen.shape
tx = 100
ty = 50
M = np.float32([[1, 0, tx], [0, 1, ty]])
desplazada = cv.warpAffine(imagen, M, (cols, rows))
plt.imshow(desplazada)
plt.title("Imagen Desplazada")
plt.show()

"""
3. CAMBIO DE PERSPECTIVA
En ocasiones cuando se trabaja con fotos o documentos escaneados, 
las imágenes están torcidas
"""
sudoku = cv.imread("imaxes/sudoku.jpg", cv.IMREAD_GRAYSCALE)
plt.imshow(sudoku)
plt.title("Escaneo Torcido")
plt.show()

"""
La idea es cambiar la perspectiva de tal manera que el sudoku
aparezca frontal en la imagen. Para esto es necesario tener las
coordenadas de las cuatro esquinas donde en la imagen original se 
encuentran y las coordenadas de donde deben situarse las cuatro esquinas
en la imagen final.
"""
rows, cols = sudoku.shape
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])  # Posición de las esquinas actuales
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])  # Nueva posición de las esquinas

# Esto proporciona la mátriz de transformación
M = cv.getPerspectiveTransform(pts1, pts2)
print(f"Matriz de transformación: \n{M}")

sudoku_derecho = cv.warpPerspective(sudoku, M, (cols, rows))
plt.imshow(sudoku_derecho)
plt.title("Escaneo Enderezado")
plt.show()
"""
Como se puede observar queda mal las partes eliminadas.
Para arreglar esto hay que dar el tamaño correcto para 
que se centre en la imagen deseada.
"""
sudoku_derecho = cv.warpPerspective(sudoku, M, (300, 300))
plt.imshow(sudoku_derecho)
plt.title("Escaneo Enderezado y Recortado")
plt.show()

"""
Lo complicado es obtener las coordenadas originales bien ordenadas,
y obtener unas coordenadas de destino acordes.
Creamos la función order_points, que ordenará las coordenadas->
La primera será la de arriba izquerda, luego arriba a la derecha,
y el resto siguiendo el sentido de las agujas del reloj. Esto es
importante ya que cuando se obtienen contornos con OpenCV no siempre
va a aparecer en ese orden.
La función four_point_transform va a coger las coordenadas, ordenarlas,
obtener las coordenadas de destino para que queden formando un cuadrilátero
y aplicarla a la imagen.
"""

"""
Este código implementa una función llamada order_points(pts) que toma como entrada una matriz de puntos pts, donde cada 
fila representa las coordenadas (x, y) de un punto en un plano. 
La función tiene como objetivo ordenar estos puntos de 
manera que se pueda formar un cuadrilátero con las 
siguientes propiedades:

El primer punto en la lista será el punto superior izquierdo.
El segundo punto será el punto superior derecho.
El tercer punto será el punto inferior derecho.
El cuarto punto será el punto inferior izquierdo.
Para lograr esto, el código sigue estos pasos:

Inicializa una matriz rect de tamaño (4, 2) para almacenar las coordenadas ordenadas.
Calcula la suma de las coordenadas (x + y) de todos los puntos. El punto con la suma más pequeña será el punto superior 
izquierdo, y el punto con la suma más grande será el punto inferior derecho.
Calcula la diferencia entre las coordenadas x e y de cada punto. El punto con la diferencia más pequeña será el punto 
superior derecho, y el punto con la diferencia más grande será el punto inferior izquierdo.
Almacena los puntos ordenados en la matriz rect.
Devuelve la matriz rect con los puntos ordenados.
El código utiliza la librería NumPy para realizar operaciones matemáticas eficientes en matrices, como calcular sumas y 
diferencias.
"""


def order_points(pts):
    # Inicializa una lista de coordenadas que se ordenará de tal manera que la primera entrada en la lista
    # sea la esquina superior izquierda, la segunda entrada sea la esquina superior derecha,
    # la tercera sea la esquina inferior derecha y la cuarta sea la esquina inferior izquierda.
    rect = np.zeros((4, 2), dtype="float32")
    # El punto superior izquierdo tendrá la suma más pequeña,
    # mientras que el punto inferior derecho tendrá la suma más grande.
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    # Ahora, calcula la diferencia entre los puntos, el punto superior derecho tendrá la diferencia
    # más pequeña, mientras que el inferior izquierdo tendrá la
    # diferencia más grande.
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    # retornamos las coordenadas ordenadas
    return rect

"""
realiza una transformación de perspectiva en una imagen dada utilizando cuatro puntos de referencia especificados. 
Aquí está el desglose de cómo funciona:

Obtención de un orden consistente de los puntos:

Se llama a la función order_points(pts) para obtener un orden consistente de los puntos proporcionados 
en el argumento pts.
Se desempaquetan los puntos individualmente en las variables tl, tr, br y bl.
Cálculo de las dimensiones de la nueva imagen:

Se calcula la longitud de los lados de la nueva imagen (width_a y width_b) usando la distancia Euclidiana 
entre los puntos bottom-right y bottom-left, y entre los puntos top-right y top-left, respectivamente.
Se calcula la altura de los lados de la nueva imagen (height_a y height_b) usando la distancia Euclidiana 
entre los puntos top-right y bottom-right, y entre los puntos top-left y bottom-left, respectivamente.
Se determina la longitud máxima (max_width) y la altura máxima (max_height) de la nueva imagen 
utilizando los valores calculados.
Construcción de los puntos de destino:

Se define un conjunto de puntos de destino dst que especifica una "vista de pájaro" de la imagen. Estos puntos están 
ordenados de manera que el primer punto sea la esquina superior izquierda, el segundo sea la esquina superior derecha, 
el tercero sea la esquina inferior derecha y el cuarto sea la esquina inferior izquierda.
Cálculo de la matriz de transformación de perspectiva y aplicación:

Se calcula la matriz de transformación de perspectiva M utilizando la función cv.getPerspectiveTransform() de OpenCV, 
que toma los puntos de referencia originales (rect) y los puntos de destino (dst).
Se aplica la transformación de perspectiva a la imagen original utilizando la función cv.warpPerspective() de OpenCV, 
que toma la imagen original, la matriz de transformación M y las dimensiones de la nueva imagen (max_width y max_height)
Retorno de la imagen transformada:

Se retorna la imagen transformada.
"""


def four_point_transform(image, pts):
    # Obtener un orden consistente de los puntos y
    # desempacarlos individualmente.
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    # Calcula el ancho de la nueva imagen, que será la distancia máxima entre las coordenadas x del punto bottom-right
    # y bottom-left, o las coordenadas x del punto top-right y
    # top-left.
    width_a = np.sqrt((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2)
    width_b = np.sqrt((tr[0] - tl[0]) ** 2) + ((tr[1] - tr[1]) ** 2)
    max_width = max(int(width_a), int(width_b))
    # Calcula la altura de la nueva imagen, que será la distancia máxima
    # entre las coordenadas y del punto top-right y bottom-right,
    # o las coordenadas y del punto top-left y bottom-left.
    height_a = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    height_b = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    max_height = max(int(height_b), int(height_b))

    # Ahora que tenemos las dimensiones de la nueva imagen,
    # construyamos el conjunto de puntos de destino para obtener
    # una "vista de pájaro" (es decir, vista desde arriba)
    # de la imagen, especificando nuevamente los puntos en el
    # orden de arriba a la izquierda, arriba a la derecha,
    # abajo a la derecha y abajo a la izquierda.

    dst = np.array([
        [0, 0],
        [max_width - 1, 0],
        [max_width - 1, max_height - 1],
        [0, max_height - 1]], dtype="float32")

    # Calcula la matriz de transformación de perspectiva
    # y luego aplícala.
    M = cv.getPerspectiveTransform(rect, dst)
    warped = cv.warpPerspective(image, M, (max_width, max_height))
    # Retorna la imagen transformada
    return warped


# Aplicamos esto a la imagen de Sudoku
pts1 = np.float32([[368, 52], [28, 387], [389, 390], [56, 65]])  # Posición de esquinas actuales, levemente desordenadas
sudoku_derecho = four_point_transform(sudoku, pts1)
plt.imshow(sudoku_derecho)
plt.title('Escaneo enderezado y recortado')

"""
Las imágenes pueden ser filtradas para reducir el ruido o detección de 
características. La operación usada se conoce como convolución, donde una 
matriz se convoluciona con los píxeles de la imagen creando otra imagen
distinta.
"""
