"""
Sistema de identificación de entrada.
Utilizando lo aprendido con la detección de rostros, se trata de crear un pequeño sistema de control de acceso a un
recinto deportivo. El sistema debe detectar cuando aparece una cara en la cámara e intentar identificarla.
Si el rostro es conocido indicará la hora a la que ingresa el usuario y almacenará la hora de entrada.
Una vez que ya no se detecta el rostro se da un pequeño tiempo, y si ese mismo rostro vuelve a aparecer,
se considerará que el usuario ha abandonado el local y se indicará el tiempo que permaneció dentro.

Si no se conoce el rostro dará una alerta.

Las caras deben cargarse desde algún sistema tipo DB, por lo que primero debes cargar los datos necesarios para el
reconocimiento facial en esa tienda.

El código CV para capturar imágenes de la cámara sería algo como esto:
import cv2

video_capture = cv2.VideoCapture(0)


while True:
    # Captura un frame
    ret, frame = video_capture.read()

    # para procesar o frame con outras ferramentas seguramente habería que convertilo a RGB
    # (Lembra que opencv traballa con BGR)

    # Amosa a imaxe resultante
    cv2.imshow('Video', frame)

    # Pulsa 'q' para saír!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a cámara
video_capture.release()
cv2.destroyAllWindows()

"""
import numpy as np
import cv2
import dlib
import time

predictor_path = "shape_predictor_5_face_landmarks.dat"
face_rec_model_path = "dlib_face_recognition_resnet_model_v1.dat"

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)
face_rec = dlib.face_recognition_model_v1(face_rec_model_path)

video_capture = cv2.VideoCapture(0)

while True:
    # Captura un frame
    ret, frame = video_capture.read()
    dets = detector(frame, 1)
    # para procesar o frame con outras ferramentas seguramente habería que convertilo a RGB
    # (Lembra que opencv traballa con BGR)
    for d in dets:
        x, y, w, h = d.left(), d.top(), d.width(), d.height()
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # Amosa a imaxe resultante
    cv2.imshow('Video', frame)

    # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Pulsa 'q' para salir!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # if len(dets) == 1:

        # print("Number of faces detected: {}".format(len(dets)))
        # time.sleep(5)
        # break

# Libera a cámara
# video_capture.release()
# cv2.destroyAllWindows()
