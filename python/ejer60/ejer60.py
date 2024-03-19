import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# Cargo imagen a analizar
imagen = cv.imread('imaxes/Escaneo-cargador.jpg', cv.IMREAD_GRAYSCALE)
plt.imshow(imagen, cmap='gray', vmin=0, vmax=255)
plt.title("Cuadrados, triángulos o círculos")
plt.show()

# Recorto imagen para seleccionar puntos
recorte = imagen[210:1500, 100:900]
plt.imshow(recorte)
plt.title('Un recorte de imagen')
plt.show()

# Grabo imagen
cv.imwrite('imaxes/Escaneo-cargador_recorte.jpg', recorte)

# Filtramos imagen
blur = cv.GaussianBlur(recorte, (5, 5), 0)
plt.imshow(blur)
plt.title('Blurred Gaussian')
plt.show()

# Reducimos número de colores de imagen
adaptative_Gaussian = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                           cv.THRESH_BINARY, 11, 2)
plt.imshow(adaptative_Gaussian, cmap='gray')
plt.title('Adaptative Gaussian')
plt.show()

# Detección de contornos
cnts, hierarchy = cv.findContours(adaptative_Gaussian, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
con_contornos = cv.cvtColor(adaptative_Gaussian, cv.COLOR_GRAY2BGR)
cv.drawContours(con_contornos, cnts, -1, (0, 255, 0), 2)
plt.imshow(con_contornos, cmap='gray')
plt.show()

circulo = 0
triangulo = 0
cuadrado = 0
for contorno in cnts:
    M = cv.moments(contorno)
    area = cv.contourArea(contorno)
    print(M)
    print(f"Area: {area}")
    num_vertices = len(cv.approxPolyDP(contorno, 0.01 * cv.arcLength(contorno, True), True))
    perimeter = cv.arcLength(contorno, True)
    approx = cv.approxPolyDP(contorno, 0.01 * perimeter, True)
    circularity = 4 * np.pi * (area / (perimeter * perimeter))
    if circularity > 0.8:
        circulo += 1
    elif num_vertices == 3:
        triangulo += 1
    else:
        cuadrado += 1
print(f"Circulos: {circulo},"
      f"Cuadrados: {cuadrado},"
      f"Triangulos: {triangulo}")

