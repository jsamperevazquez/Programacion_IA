import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imagen = cv.imread('imaxes/photo2.png')
print(type(imagen))
"""
Para leer una imagen se utiliza imread.
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




