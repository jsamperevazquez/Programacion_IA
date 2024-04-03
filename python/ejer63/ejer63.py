import pickle
import sqlite3
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import dlib
import os


class BD:
    conn: sqlite3.Connection
    cursor: sqlite3.Cursor

    def open_database(self):
        database_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "bd/datosDLIB.db"))
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()

    def close_database(self):
        self.conn.close()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users_vectors (
                id INTEGER PRIMARY KEY AUTOINCREMENT , user_name VARCHAR(100), vector TEXT)''')

    def insert_image_name(self, name: str, vector_str: pickle):
        self.cursor.execute("INSERT INTO users_vectors (user_name, vector) VALUES (?, ?)", (name, vector_str))
        self.conn.commit()

    def select_all_users(self):
        self.cursor.execute("SELECT * FROM users_vectors")
        users = self.cursor.fetchall()
        return users


class UserDlib:
    img_uri: str
    user_name: str
    PREDICTOR: str
    FACE_REC_MODEL: str
    BD: BD

    def __init__(self, img_uri: str, user_name: str) -> None:
        self.img_uri = img_uri
        self.user_name = user_name
        self.PREDICTOR = "shape_predictor_5_face_landmarks.dat"
        self.FACE_REC_MODEL = "dlib_face_recognition_resnet_model_v1.dat"
        self.DETECTOR = dlib.get_frontal_face_detector()
        self.SP = dlib.shape_predictor(self.PREDICTOR)
        self.FACE_REC = dlib.face_recognition_model_v1(self.FACE_REC_MODEL)
        self.BD = BD()
        self.known_face_encodings = []
        self.known_face_names = []

    def register_new_user(self, image: str, name: str):
        # Abro conexión a BD y creo tabla
        self.BD.open_database()
        self.BD.create_table()

        # Cargo imágenes
        user_image = cv.imread(image)
        user_image_color = cv.cvtColor(user_image, cv.COLOR_BGR2RGB)

        # Introduzco imagen de usuario en el detector de DLIB
        dets = self.DETECTOR(user_image, 1)
        print("Number of faces detected: {}".format(len(dets)))
        positions = dets[0]
        print(positions)

        # Usamos el predictor facial para puntos clave de la imagen
        shape = self.SP(user_image, positions)
        face_descriptor = np.array(self.FACE_REC.compute_face_descriptor(user_image, shape))
        print(face_descriptor)

        self.known_face_encodings.append((face_descriptor, name))

        # Convertimos el vector face_descriptor en una cadena de bytes para insertar en la BD
        vector_str = pickle.dumps(face_descriptor)

        # Recuperamos los usuarios de la BD
        users = self.BD.select_all_users()

        vector_found = False
        for u in users:
            # Convertimos la cadena de bytes de nuevo en vector numpy
            db_vector = pickle.loads(u[2])

            if np.array_equal(face_descriptor, db_vector):
                vector_found = True
                print(f"El usuario con id {u[0]} y nombre {u[1]} ya está en la base de datos")
                break

        if not vector_found:
            self.BD.insert_image_name(name, vector_str)

        self.BD.close_database()
        plt.imshow(user_image_color), plt.title(name)
        plt.show()


if __name__ == '__main__':
    user = UserDlib("imaxes/mateo.jpg", "Mateo")
    user2 = UserDlib("imaxes/angel.jpg", "Angel")
    user.register_new_user(user.img_uri, user.user_name)
    user2.register_new_user(user2.img_uri, user2.user_name)
