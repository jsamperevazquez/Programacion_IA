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
plt.show()

"""
    FILTRADO DE IMÁGENES
Las imágenes pueden ser filtradas para reducir el ruido o detección de 
características. La operación usada se conoce como convolución, donde una 
matriz se convoluciona con los píxeles de la imagen creando otra imagen
distinta.
una convolución es sencillamente una multiplicación elemento elemento de 
un kernel y alguna parte de la imagen fuente para producir un nuevo pixel.
Esto se hace en todos los píxeles de la imagen creando una imagen distinta.
* En openCV tenemos una función filter2D que hace eso *
"""
kernel = np.ones((5, 5), np.float32) / 25
dst = cv.filter2D(sudoku_derecho, -1, kernel)
plt.subplot(121), plt.imshow(sudoku_derecho), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Media')
plt.xticks([]), plt.yticks([])
plt.show()

kernel_1 = np.array([[0., 0., 0.],
                     [1., 1., 1.],
                     [0., 0., 0.]], dtype=np.float32)
dst = cv.filter2D(sudoku_derecho, -1, kernel_1)
plt.subplot(121), plt.imshow(sudoku_derecho), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Filtrado')
plt.xticks([]), plt.yticks([])
plt.show()

"""
El siguiente filtro busca bordes
"""
kernel2 = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
])
dst = cv.filter2D(sudoku_derecho, -1, kernel2)
plt.subplot(121), plt.imshow(sudoku_derecho), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Filtrado')
plt.xticks([]), plt.yticks([])
plt.show()

"""
Existen algunos filtros ya predefinidos más sencillos de utilizar:
    * blur: suaviza la imagen
    * GaussianBlur: suaviza pero con kernel gaussiano
"""

blur = cv.blur(sudoku_derecho, (5, 5))
blur_gaussian = cv.GaussianBlur(sudoku_derecho, (5, 5), 0)
plt.subplot(131), plt.imshow(sudoku_derecho), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(blur_gaussian), plt.title('Blurred Gaussian')
plt.xticks([]), plt.yticks([])
plt.show()

"""
    UMBRAL DE IMÁGENES
Para realizar ciertas operaciones sobre imágenes, es preciso reducir el
número de colores de esta, muchas veces solo a blanco y negro.
Hay varios métodos, desde una simple comprobación de intensidad (valores mayores pasan 
a blanco y los menores a negro) hasta otros (Otsu o Gaussian) que tienen en cuenta otros 
factores.
"""
blur_median = cv.medianBlur(sudoku_derecho, 5)
blur = cv.GaussianBlur(sudoku_derecho, (5, 5), 0)
ret, th1 = cv.threshold(sudoku_derecho, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(blur_median, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(blur_median, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv.THRESH_BINARY, 11, 2)
# Otsu's thresholding
ret4, th4 = cv.threshold(sudoku_derecho, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
ret5, th5 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
titles = ['Original Image', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding', "Otsu's Thresholding",
          "Otsu's Thresholding imaxe filtrada"]

imagenes = [sudoku_derecho, th1, th2, th3, th4, th5]
for i in range(len(imagenes)):
    plt.subplot(2, 3, i + 1), plt.imshow(imagenes[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

"""
    EROSIÓN Y DILATACIÓN
Estas operaciones se aplican normalmente a imágenes binarias(blanco y negro).
La erosión consigue adelgazar las lineas, la dilatación las engorda.
"""
letra_j = cv.imread('imaxes/letter_j.png', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(letra_j, kernel, iterations=1)
erosion_2 = cv.erode(letra_j, kernel, iterations=2)

plt.subplot(131), plt.imshow(letra_j), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(erosion), plt.title('Erosionado')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(erosion_2), plt.title('Erosionado_2')
plt.xticks([]), plt.yticks([])
plt.show()

"""
Las lienas a erosionar es el blanco y fondo negro.
Muchas de las imágenes hay que invertirlas.
"""

th3 = cv.adaptiveThreshold(blur_median, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
sudoku_invertido = cv.bitwise_not(th3)
plt.subplot(121), plt.imshow(th3), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(sudoku_invertido), plt.title('Invertido')
plt.xticks([]), plt.yticks([])
plt.show()

kernel_1 = np.ones((3, 3), np.uint8)
erosion_1 = cv.erode(sudoku_invertido, kernel_1, iterations=1)
kernel_2 = np.ones((5, 5), np.uint8)
erosion_2 = cv.erode(sudoku_invertido, kernel_2, iterations=1)

plt.subplot(131), plt.imshow(sudoku_invertido), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(erosion_1), plt.title('Erosionado 3x3')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(erosion_2), plt.title('Erosionado 5x5')
plt.xticks([]), plt.yticks([])
plt.show()

"""
La dilatación es igual pero con la función dilate
"""
kernel = np.ones((5, 5), dtype=np.uint8)
dilatation = cv.dilate(letra_j, kernel, iterations=1)
plt.subplot(121), plt.imshow(letra_j), plt.title('Invertido')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dilatation), plt.title('Dilatado')
plt.xticks([]), plt.yticks([])
plt.show()

"""
También existen combinaciones de las dos operaciones para producir efectos 
en la imagen:
    * opening: erosión y luego dilatación -> Elimina ruidos de la imagen
    * closing: dilatación y luego erosión -> Elimina huecos dentro de estructuras cerradas
    * gradiente morfológico: diferencia entre dilatación y erosión -> Obtiene el borde exterior del elemento
"""
letra_j_puntos = cv.imread('imaxes/letter_j_puntos.png', 0)
letra_j_huecos = cv.imread('imaxes/letter_j_huecos.png', 0)

kernel_1 = np.ones((3, 3), dtype=np.uint8)
kernel2 = np.ones((5, 5), dtype=np.uint8)
opening_1 = cv.morphologyEx(letra_j_puntos, cv.MORPH_OPEN, kernel_1, kernel_1)
opening_2 = cv.morphologyEx(letra_j_huecos, cv.MORPH_OPEN, kernel2, kernel_2)

plt.subplot(131), plt.imshow(letra_j_puntos), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(opening_1), plt.title('Opening 3x3')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(opening_2), plt.title('Opening 5x5')
plt.xticks([]), plt.yticks([])
plt.show()

closing_1 = cv.morphologyEx(letra_j_huecos, cv.MORPH_CLOSE, kernel_1)
closing_2 = cv.morphologyEx(letra_j_huecos, cv.MORPH_CLOSE, kernel2)
plt.subplot(131), plt.imshow(letra_j_puntos), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(closing_1), plt.title('Closing 3x3')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(closing_2), plt.title('Closing 5x5')
plt.xticks([]), plt.yticks([])
plt.show()

gradient_1 = cv.morphologyEx(letra_j, cv.MORPH_GRADIENT, kernel_1)
gradient_2 = cv.morphologyEx(letra_j, cv.MORPH_GRADIENT, kernel_2)
plt.subplot(131), plt.imshow(letra_j), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(gradient_1), plt.title('Gradiente 3x3')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(gradient_2), plt.title('Gradiente 5x5')
plt.xticks([]), plt.yticks([])
plt.show()

kernel_1 = np.ones((3, 3), np.uint8)
opening_1 = cv.morphologyEx(sudoku_invertido, cv.MORPH_OPEN, kernel_1)
opening_2 = cv.morphologyEx(sudoku_invertido, cv.MORPH_OPEN, kernel_2)
plt.subplot(131), plt.imshow(sudoku_invertido), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(opening_1), plt.title('Opening 3x3')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(opening_2), plt.title('Opening 5x5')
plt.xticks([]), plt.yticks([])
plt.show()

"""
    DIBUJO
En ocasiones es útil dibujar en las imágenes. Algún tipo de búsqueda de un objeto, detección
de bordes y ver lo que detecta.
Se pueden dibujar formas simples de una manera sencilla:    
    * line
    * rectangle
    * circle
    * polylines
Todos ellos van a coger parámetros:
    * Una imagen a dibujar
    * Puntos de origen o radio
    * Tupla para representar el color
    * Grosor de una linea
"""
copia_j = sudoku.copy()
cv.line(copia_j, (50, 50), (100, 100), (0, 255, 0), 3)  # Sea en negro, imagen es en escala gris
for punto in pts1:
    p = punto.astype(int)
    cv.circle(copia_j, p, 10, (100, 100, 100), 3)
plt.imshow(copia_j)
plt.show()

"""
    DETECCIÓN DE CONTORNOS
Los contornos son curvas que unen puntos del mismo color o intensidad. Son útiles
para el análisis  de formas o detección de objetos.
Funcionan mejor con las imágenes binarias, por ello hay que transformarlas. Buscar 
contornos es buscar objetos blancos en fondos negros, por lo que en ocasiones habrá
que invertir la imagen.
La función que se usa es findContours, que recibe 3 parámetros:
    - La imagen
    - El método de extracción de contornos:
        * cv.RETR_TREE
        * cv2.RETR_LIST
    - Método de aproximación de contornos:
        * cv.CHAIN_APPROX_NONE
        * cv.CHAIN_APPROX_SIMPLE
        
cuadradoCirculo = cv.imread('imaxes/cuadrado-circulo.png',0): Carga la imagen "cuadrado-circulo.png"
en escala de grises (el segundo argumento 0 indica que la imagen debe cargarse en 
escala de grises).
cnts, hierarchy = cv.findContours(cuadradoCirculo, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE): 
Encuentra los contornos en la imagen cargada utilizando el algoritmo cv.RETR_LIST para recuperar todos
 los contornos sin establecer jerarquía entre ellos, y cv.CHAIN_APPROX_SIMPLE para aproximar los contornos.
cnts2, hierarchy2 = cv.findContours(cuadradoCirculo, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE): 
Encuentra los contornos nuevamente, pero esta vez utilizando el algoritmo cv.RETR_TREE para recuperar
 todos los contornos y construir una jerarquía de contornos anidados.
display(hierarchy2): Muestra la jerarquía de contornos obtenida en el paso anterior.
display(f"Numero contornos {len(cnts)}"): Muestra el número de contornos encontrados 
en la imagen.
conContornos = cv.cvtColor(cuadradoCirculo,cv.COLOR_GRAY2RGB): Convierte la imagen en escala
de grises a RGB para poder dibujar los contornos en color.
cv.drawContours(conContornos, cnts, -1, (0, 255, 0), 2): Dibuja todos los contornos encontrados
en la imagen convertida a RGB (conContornos). 
El color de los contornos se establece en verde (0, 255, 0), con un grosor de línea de 2 píxeles.
plt.subplot(121),plt.imshow(cuadradoCirculo,cmap = 'gray'): Establece el primer subplot 
para mostrar la imagen original en escala de grises.
plt.subplot(122),plt.imshow(conContornos,cmap = 'gray'): Establece el segundo subplot
para mostrar la imagen con los contornos dibujados en color.
plt.show(): Muestra las imágenes con los contornos dibujados en dos subplots.
En resumen, este código carga una imagen, encuentra sus contornos, dibuja los contornos 
en una versión en color de la imagen y muestra tanto la imagen original 
como la imagen con los contornos dibujados.
También muestra la jerarquía de contornos si se utiliza el modo RETR_TREE.
"""
cuadrado_circulo = cv.imread('imaxes/cuadrado-circulo.png', 0)
cnts, hierarchy = cv.findContours(cuadrado_circulo, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cnts_2, hierarchy_2 = cv.findContours(cuadrado_circulo, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(hierarchy_2)
print(f"Número de contornos {len(cnts)}")
con_contornos = cv.cvtColor(cuadrado_circulo, cv.COLOR_GRAY2BGR)

cv.drawContours(con_contornos, cnts, -1, (0, 255, 0), 2)
plt.subplot(121), plt.imshow(cuadrado_circulo, cmap='gray')
plt.title('Imaxe Orixinal'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(con_contornos, cmap='gray')
plt.title('Bordes'), plt.xticks([]), plt.yticks([])
plt.show()

"""
De cada contorno se puede obtener información:

    - moments
    - contourArea: area
    - arcLength: perimetro
    - approxPolyDP: aproxima el contorno con un polígono más simple
    - convexHull: es un perímetro más simple que contiene a todos los puntos do contorno.
                  Similar ao anterior.
    - boundingRect: obtiene un rectángulo que contiene a todos los puntos del contorno
    - minEnclosingCircle: como o anterior, pero cun círculo.
for contorno in cnts:: Itera sobre cada contorno encontrado en la imagen.
M = cv.moments(contorno): Calcula los momentos del contorno actual.
area = cv.contourArea(contorno): Calcula el área del contorno actual.
print( M ): Imprime los momentos calculados del contorno.
print(f"Area: {area}"): Imprime el área del contorno.
perimeter = cv.arcLength(contorno,True): Calcula el perímetro del contorno.
approx = cv.approxPolyDP(contorno,0.01*perimeter,True): Aproxima el contorno actual con un polígono 
con menos vértices.
circularity = 4*np.pi*(area/(perimeter*perimeter)): Calcula la circularidad 
del contorno utilizando la fórmula que definimos anteriormente.
if circularity > 0.8:: Compara la circularidad calculada con un umbral de 0.8.
print(f"O contorno con {len(contorno)} vertices parece un circulo"): Si la circularidad 
es mayor que 0.8, imprime un mensaje indicando que el contorno parece ser un círculo, 
junto con el número de vértices del contorno.
else:: Si la circularidad no es mayor que 0.8, se ejecuta este bloque de código.
print(f"O contorno con {len(contorno)} vertices NON parece un circulo"): Imprime un mensaje 
indicando que el contorno no parece ser un círculo, 
junto con el número de vértices del contorno.
En resumen, este código analiza cada contorno encontrado en la imagen y 
determina si parece ser un círculo basándose en su circularidad, 
imprimiendo mensajes en consecuencia.
"""
for contorno in cnts:
    M = cv.moments(contorno)
    area = cv.contourArea(contorno)
    print(M)
    print(f"Area: {area}")
    perimeter = cv.arcLength(contorno, True)
    approx = cv.approxPolyDP(contorno, 0.01 * perimeter, True)
    circularity = 4 * np.pi * (area / (perimeter * perimeter))
    if circularity > 0.8:
        print(f"O contorno con {len(contorno)} vertices parece un circulo")
    else:
        print(f"O contorno con {len(contorno)} vertices NON parece un circulo")
