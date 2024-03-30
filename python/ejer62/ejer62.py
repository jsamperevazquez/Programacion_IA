import cv2 as cv
import matplotlib.pyplot as plt

# Cargo archivos y colores
image = cv.imread('imaxes/ironmaiden.jpg')
image_color = cv.cvtColor(image, cv.COLOR_BGRA2RGB)
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Muestro imagen original
plt.imshow(image_color)
plt.title('Original')
plt.show()


# Función para detectar y difuminar cada cara
def blurr_faces(img):
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
        face_zone = destiny[y:y + h, x:x + w]  # Zona de la imagen a difuminar
        blurred_face = cv.blur(face_zone, (
            25, 25))
        destiny[y:y + h, x:x + w] = blurred_face
        cv.rectangle(destiny, (x, y), (x + w, y + h), (255, 0, 0), 5)
    plt.imshow(destiny)
    plt.title('Caras detectadas')
    plt.show()


blurr_faces(image_color)
