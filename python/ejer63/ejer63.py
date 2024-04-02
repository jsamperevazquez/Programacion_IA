import pickle
import sqlite3
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import dlib


class UserDlib:
    img_uri: str
    user_name: str
    PREDICTOR: str
    FACE_REC_MODEL: str

    def __init__(self, img_uri: str, user_name: str) -> None:
        self.img_uri = img_uri
        self.user_name = user_name
        self.conn = sqlite3.connect('datosDLIB.db')
        self.PREDICTOR = "shape_predictor_5_face_landmarks.dat"
        self.FACE_REC_MODEL = "dlib_face_recognition_resnet_model_v1.dat"
        self.DETECTOR = dlib.get_frontal_face_detector()
        self.SP = dlib.shape_predictor(self.PREDICTOR)
        self.FACE_REC = dlib.face_recognition_model_v1(self.FACE_REC_MODEL)
        self.known_face_encodings = []
        self.known_face_names = []

    def create_table_image_name(self, image: str, name: str):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users_vectors (
                id INTEGER PRIMARY KEY AUTOINCREMENT , user_name VARCHAR(100), vector TEXT)''')
        user_image = cv.imread(image)
        user_image_color = cv.cvtColor(user_image, cv.COLOR_BGR2RGB)

        dets = self.DETECTOR(user_image, 1)
        print("Number of faces detected: {}".format(len(dets)))
        positions = dets[0]
        print(positions)
        shape = self.SP(user_image, positions)
        face_descriptor = np.array(self.FACE_REC.compute_face_descriptor(user_image, shape))
        print(face_descriptor)

        self.known_face_encodings.append((face_descriptor, name))
        vector_str = pickle.dumps(face_descriptor)
        cursor.execute("SELECT * FROM users_vectors")
        users = cursor.fetchall()

        vector_found = False
        for user in users:
            db_vector = pickle.loads(user[2])
            if np.array_equal(face_descriptor, db_vector):
                vector_found = True
                print(f"El usuario con id {user[0]} y nombre {user[1]} ya está en la base de datos")
                break

        if not vector_found:
            cursor.execute("INSERT INTO users_vectors (user_name, vector) VALUES (?, ?)", (name, vector_str))
            self.conn.commit()

        cursor.close()
        plt.imshow(user_image_color), plt.title(name)
        plt.show()


if __name__ == '__main__':
    user = UserDlib("imaxes/mateo.jpg", "Mateo")
    user2 = UserDlib("imaxes/angel.jpg", "Angel")
    user.create_table_image_name(user.img_uri, user.user_name)
    user2.create_table_image_name(user2.img_uri, user2.user_name)
