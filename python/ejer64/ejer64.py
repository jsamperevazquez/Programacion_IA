from matplotlib import pyplot as plt
from python.ejer63 import ejer63
import pickle
import dlib
import cv2 as cv
import numpy as np


class Identifier:
    BD: ejer63.BD
    PREDICTOR: str
    FACE_REC_MODEL: str
    DETECTOR: dlib

    def __init__(self) -> None:
        self.PREDICTOR = "shape_predictor_5_face_landmarks.dat"
        self.FACE_REC_MODEL = "dlib_face_recognition_resnet_model_v1.dat"
        self.DETECTOR = dlib.get_frontal_face_detector()
        self.BD = ejer63.BD()
        self.SP = dlib.shape_predictor(self.PREDICTOR)
        self.FACE_REC = dlib.face_recognition_model_v1(self.FACE_REC_MODEL)

    def identify_users(self, img: str) -> None:
        tolerance = 0.6
        known_face_encodings = []
        face_names = []

        # Recuperamos los usuarios de la base de datos
        self.BD.open_database()
        users = self.BD.select_all_users()

        img_to_evaluate = cv.imread(img)
        img_eval_color = cv.cvtColor(img_to_evaluate, cv.COLOR_BGR2RGB)
        dets = self.DETECTOR(img_to_evaluate, 1)
        for u in users:
            # Convertimos la cadena de bytes de nuevo en vector numpy para meterlo en lista
            known_face_encodings.append((pickle.loads(u[2]), u[1]))

        for face in dets:
            shape = self.SP(img_eval_color, face)
            face_descriptor = np.array(self.FACE_REC.compute_face_descriptor(img_eval_color, shape))
            matches = [(np.linalg.norm(face_descriptor - match[0]), match[1]) for match in known_face_encodings if
                       np.linalg.norm(face_descriptor - match[0]) <= tolerance]
            print(matches) if len(matches) > 0 else None
            if len(matches) == 0:
                face_names.append(((face.top(), face.right(), face.bottom(), face.left()), "Ignoto"))
            else:
                sort_faces = sorted(matches, key=lambda x: x[0])
                face_names.append(((face.top(), face.right(), face.bottom(), face.left()), sort_faces[0][1]))
        marked_image = img_eval_color.copy()
        for (top, right, bottom, left), name in face_names:
            # Se amplía las ubicaciones de las caras, ya que el marco que detectamos se escaló a 1/4 de tamaño
            color = (0, 255, 0)
            if name == "Ignoto":
                color = (0, 0, 255)
            cv.rectangle(marked_image, (left, top), (right, bottom), color, 3)
            cv.rectangle(marked_image, (left, bottom + 30), (right, bottom), color, cv.FILLED)
            font = cv.FONT_HERSHEY_TRIPLEX
            cv.putText(marked_image, name, (
                left + 6, bottom + 20), font, 0.75, (255, 0, 0), 2)

        plt.imshow(marked_image)
        plt.title('Caras Encontradas')
        plt.show()


if __name__ == '__main__':
    iden = Identifier()
    iden.identify_users("imaxes/ironmaiden.jpg")
    iden.identify_users("imaxes/papaMateo.jpg")
