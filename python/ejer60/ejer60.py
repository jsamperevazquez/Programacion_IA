import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# Cargo imagen a analizar
imagen = cv.imread('imaxes/Escaneo-cargador.jpg')
plt.imshow(imagen, cmap='gray', vmin=0, vmax=255)
plt.title("Cuadrados, triángulos o círculos")
plt.show()

# Recorto imagen para seleccionar puntos
recorte = imagen[210:1500, 100:900]
plt.imshow(recorte)
plt.title('Un recorte de imagen')
plt.show()

# Reduzco tamaño de la imagen
escalado = cv.resize(recorte, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
plt.imshow(escalado)
plt.title('Imagen mitad de tamaño')
plt.show()

# Grabo imagen
cv.imwrite('imaxes/Escaneo-cargador_recorte.jpg', escalado)

# Paso la imagen a escala grises
img_gray = cv.imread('imaxes/Escaneo-cargador_recorte.jpg', cv.IMREAD_GRAYSCALE)
plt.subplot(121), plt.imshow(recorte), plt.title('Recorte Original')
plt.subplot(122), plt.imshow(img_gray, cmap='gray'), plt.title('Recorte en gris')
plt.show()

# Filtramos imagen
img_suavizada = cv.bilateralFilter(img_gray, 9, 75, 75)
plt.imshow(img_suavizada)
plt.title('Filtrado Gaussiano')
plt.show()

# Reducimos número de colores de imagen
adaptative_Gaussian = cv.adaptiveThreshold(img_suavizada, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                           cv.THRESH_BINARY, 11, 2)
invertida = cv.bitwise_not(adaptative_Gaussian)
plt.imshow(invertida)
plt.title('Adaptative Gaussian (invertida)')
plt.show()


# Opening and closing
kernel1 = np.ones((1, 1), np.uint8)
kernel2 = np.ones((3, 3), np.uint8)
opening1 = cv.morphologyEx(invertida, cv.MORPH_OPEN, kernel1)
closing1 = cv.morphologyEx(opening1, cv.MORPH_CLOSE, kernel2)
plt.subplot(131), plt.imshow(adaptative_Gaussian), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(opening1), plt.title('Opening 1x1')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(closing1), plt.title('Closing 3x3')
plt.xticks([]), plt.yticks([])
plt.show()

# Detección de contornos
cnts, hierarchy = cv.findContours(closing1, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
con_contornos = cv.cvtColor(closing1, cv.COLOR_GRAY2BGR)
cv.drawContours(con_contornos, cnts, -1, (0, 255, 0), 2)
# Creo un rectángulo alrededor de los círculos
cv.rectangle(con_contornos, (260, 50), (380, 190), (255, 255, 255), 2)
cv.rectangle(con_contornos, (30, 530), (150, 640), (255, 255, 255), 2)
cv.rectangle(con_contornos, (240, 270), (360, 400), (255, 255, 255), 2)

plt.imshow(con_contornos, cmap='gray')
plt.show()

circulo = 0
triangulo = 0
cuadrado = 0
for contorno in cnts:
    area = cv.contourArea(contorno)
    num_vertices = len(cv.approxPolyDP(contorno, 0.04 * cv.arcLength(contorno, True), True))
    perimeter = cv.arcLength(contorno, True)
    if perimeter <= 310 or area <= 500:
        pass
    else:
        circularity = 4 * np.pi * (area / (perimeter * perimeter))
        if circularity > 0.8:
            circulo += 1
        elif num_vertices == 3:
            triangulo += 1
        elif num_vertices == 4:
            cuadrado += 1
print(f"Círculos: {circulo}, Cuadrados: {cuadrado}")
