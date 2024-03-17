import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

imagen = cv.imread('imaxes/Escaneo-cargador.jpg')
plt.imshow(imagen)
plt.title("Cuadrados, triángulos o círculos")
plt.show()