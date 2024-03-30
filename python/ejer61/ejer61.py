import matplotlib.pyplot as plt
import cv2 as cv

# Cargo archivos y colores
image = cv.imread('imaxes/ironmaiden.jpg')
image_color = cv.cvtColor(image, cv.COLOR_BGRA2RGB)
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Muestro resultados
plt.imshow(image_color)
plt.title('Imagen Original')
plt.show()
plt.imshow(image_gray)
plt.title('Imagen en gris')
plt.show()


# Creo función con clasificador de cascada para clasificar rostros
def search_faces(img):
    face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

    faces = face_cascade.detectMultiScale(
        img,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(50, 50),
    )
    print("Caras = ", len(faces))
    destiny = img.copy()
    for (x, y, w, h) in faces:
        cv.rectangle(destiny, (x, y), (x + w, y + h), (255, 0, 0), 5)
    plt.imshow(destiny)
    plt.title('Caras detectadas')
    plt.show()


search_faces(image_color)
