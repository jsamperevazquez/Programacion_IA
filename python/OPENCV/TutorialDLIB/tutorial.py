import cv2 as cv
import matplotlib.pyplot as plt
import dlib
import numpy as np

img = cv.imread('imaxes/angel.jpg')
img_color = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img_color), plt.title('Original')
plt.show()

predictor = "shape_predictor_5_face_landmarks.dat"
face_rec_model = "dlib_face_recognition_resnet_model_v1.dat"

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor)
face_rec = dlib.face_recognition_model_v1(face_rec_model)

known_face_encodings = []
known_face_names = []

dets = detector(img_color, 1)
print("Found {} face(s)".format(len(dets)))
positions = dets[0]
print(positions)
shape = sp(img, positions)

face_descriptors = np.array(face_rec.compute_face_descriptor(img, shape))
print(face_descriptors)

known_face_encodings.append((face_descriptors, 'Angel'))

face_names = []
dets = detector(img_color, 1)
tolerance = 0.6
for face in dets:
    shape = sp(img, face)
    face_descriptors = np.array(face_rec.compute_face_descriptor(img_color, shape))
    print(np.linalg.norm(face_descriptors - known_face_encodings[0][0]))
    # Vemos si la cara coincide con las caras conocidas
    matches = [(np.linalg.norm(face_descriptors - match[0]), match[1]) for match in known_face_encodings if
               np.linalg.norm(face_descriptors - match[0]) <= tolerance]
    print(matches)
    if len(matches) == 0:
        face_names.append(((face.top(), face.right(), face.bottom(), face.left()), "Desconocido"))
    else:
        sorted_faces = sorted(matches, key=lambda x: x[0])
        face_names.append(((face.top(), face.right(), face.bottom(), face.left()), sorted_faces[0][1]))

# Marcamos rectángulos en las caras detectadas
marked_img = img_color.copy()
for (top, right, bottom, left), name in face_names:
    # Se amplía las ubicaciones de las caras, ya que el marco que detectamos se escaló a 1/4 de tamaño
    color = (0, 255, 0) if not name == "Desconocido" else (0, 0, 255)
    # Dibujamos rectángulo alrededor de la cara
    cv.rectangle(marked_img, (left, top), (right, bottom), color, 2)

    # Escribimos el nombre en una etiqueta
    cv.rectangle(marked_img, (left, bottom + 100), (right, bottom), color, cv.FILLED)
    font = cv.FONT_HERSHEY_TRIPLEX
    cv.putText(marked_img, name, (left + 200, bottom + 60), font, 3.0, (0, 0, 0), 1)

plt.imshow(marked_img)
plt.title("Caras encontradas")
plt.show()

img_bruce = cv.imread("imaxes/bruce.jpeg")
img_bruce_color = cv.cvtColor(img_bruce, cv.COLOR_BGR2RGB)

dets = detector(img_bruce, 1)
print("Number of faces detected: {}".format(len(dets)))
positions2 = dets[0]
print(positions2)
shape = sp(img_bruce, positions2)

face_descriptor = np.array(face_rec.compute_face_descriptor(img_bruce, shape))
print(face_descriptor)

known_face_encodings.append((face_descriptor, "Bruce Dickinson"))
plt.imshow(img_bruce_color), plt.title("Bruce Dickinson")
plt.show()

img_iron_maiden = cv.imread("imaxes/ironmaiden.jpg")
img_iron_maiden_color = cv.cvtColor(img_iron_maiden, cv.COLOR_BGR2RGB)

dets = detector(img_iron_maiden, 1)
for face in dets:

    shape = sp(img_iron_maiden_color, face)
    face_descriptor = np.array(face_rec.compute_face_descriptor(img_iron_maiden_color, shape))
    print(np.linalg.norm(face_descriptor - known_face_encodings[0][0]))
    # See if the face is a match for the known face(s)
    matches = [(np.linalg.norm(face_descriptor - match[0]), match[1]) for match in known_face_encodings if
               np.linalg.norm(face_descriptor - match[0]) <= tolerance]
    print(matches)
    if len(matches) == 0:
        face_names.append(((face.top(), face.right(), face.bottom(), face.left()), "Desconocido"))
    else:
        sort_faces = sorted(matches, key=lambda x: x[0])
        face_names.append(((face.top(), face.right(), face.bottom(), face.left()), sort_faces[0][1]))
marked_image = img_iron_maiden_color.copy()
for (top, right, bottom, left), name in face_names:
    # Se amplía las ubicaciones de las caras, ya que el marco que detectamos se escaló a 1/4 de tamaño

    color = (0, 255, 0)
    if name == "Desconocido":
        color = (0, 0, 255)
    cv.rectangle(marked_image, (left, top), (right, bottom), color, 2)

    cv.rectangle(marked_image, (left, bottom + 20), (right, bottom), color, cv.FILLED)
    font = cv.FONT_HERSHEY_DUPLEX
    cv.putText(marked_image, name, (left + 6, bottom + 15), font, 0.5, (255, 255, 255), 1)

plt.imshow(marked_image)
plt.title('Caras Encontradas')
plt.show()
