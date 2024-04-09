import chromadb, dlib, cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('imaxes/angel.jpg')
image_color = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_color), plt.title('Imagen 1')
plt.show()

# Creamos una Base de datos persistente (si no queremos persistencia chromadb.Client())
chroma_client = chromadb.PersistentClient(path='chromiumDB')

# Creamos una colección (equivalente a tabla bd_relacional)
collection = chroma_client.get_or_create_collection(name="faces", metadata={"hnsw:space": "cosine"})
num_faces = collection.count()
print(f"Número de caras previas: {num_faces}")

predictor_path = 'shape_predictor_5_face_landmarks.dat'
face_rec_model_path = 'dlib_face_recognition_resnet_model_v1.dat'

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)
face_rec = dlib.face_recognition_model_v1(face_rec_model_path)

dets = detector(image_color, 1)
print(f"Número de caras detectadas: {len(dets)}")
positions = dets[0]
print(positions)
shape = sp(image_color, positions)

face_descriptor = np.array(face_rec.compute_face_descriptor(image_color, shape))
print(face_descriptor)

# Añadimos las caras a las colecciones
collection.add(
    embeddings=[list(face_descriptor)],
    metadatas=[{"nombre": "Angel"}],
    ids=["id1"]
)
num_faces = collection.count()
print(f"Numero de caras: {num_faces}")

face_names = []

dets = detector(image_color, 1)
tolerance = 0.1
for face in dets:
    shape = sp(image_color, face)
    face_descriptor = np.array(face_rec.compute_face_descriptor(image_color, shape))
    results = collection.query(query_embeddings=[list(face_descriptor)],
                               n_results=5)
    print(results)
    found_faces = [position for position, distance in enumerate(results['distances'][0])
                   if distance < tolerance]
    num_faces = len(found_faces)
    print(f"Número de concordancias: {num_faces}")
    if num_faces > 0:
        print(results['metadatas'])
        face_names.append(((face.top(), face.right(), face.bottom(), face.left()),
                           results['metadatas'][0][0]['nombre']))

# Marcamos las caras y escribimos etiquetas nombre
marked_image = image_color.copy()
for (top, right, bottom, left), name in face_names:
    color = (0, 255, 0) if not name == "Ignoto" else (0, 0, 255)
    cv2.rectangle(marked_image, (left, top), (right, bottom), color, 2)
    cv2.rectangle(marked_image, (left, bottom + 55), (right, bottom), color, cv2.FILLED)
    font = cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(marked_image, name, (left + 20, bottom + 35), font, 1.5, (0, 0, 0), 2)
plt.imshow(marked_image)
plt.title("Caras encontradas")
plt.show()

id = 2
images_Scanner = (("imaxes/steve.jpeg", "Steve"), ("imaxes/bruce.jpeg", "Bruce"))
for image_file, name in images_Scanner:
    image_steve = cv2.imread(image_file)
    img_steve_color = cv2.cvtColor(image_steve, cv2.COLOR_BGR2RGB)

    dets = detector(img_steve_color, 1)
    print(f"Número de caras detectadas: {len(dets)}")
    positions = dets[0]
    shape = sp(image_steve, positions)

    face_descriptor = np.array(face_rec.compute_face_descriptor(image_steve, shape))

    collection.add(
        embeddings=[list(face_descriptor)],
        metadatas=[{"nombre": name}],
        ids=[f"id{id}"]
    )
    id += 1
num_faces = collection.count()

iron_maiden = cv2.imread("imaxes/ironmaiden.jpg")
iron_maiden_color = cv2.cvtColor(iron_maiden, cv2.COLOR_BGR2RGB)

face_names = []
dets = detector(iron_maiden_color, 1)
tolerance = 0.1
for det in dets:
    shape = sp(iron_maiden_color, det)
    face_descriptor = np.array(face_rec.compute_face_descriptor(iron_maiden_color, shape))
    results = collection.query(query_embeddings=[list(face_descriptor)],
                               n_results=1)
    found_faces = [position for position, distance in enumerate(results['distances'][0])
                   if distance < tolerance]
    num_faces = len(found_faces)
    face_names.append(
        ((det.top(), det.right(), det.bottom(), det.left()), "Ignoto")) if num_faces == 0 else face_names.append(
        ((det.top(), det.right(), det.bottom(), det.left()), results['metadatas'][0][0]['nombre']))
    marked_image = iron_maiden_color.copy()
    for (top, right, bottom, left), name in face_names:
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        color = (0, 255, 0)
        if name == "Ignoto":
            color = (0, 0, 255)
        # Draw a box around the face
        cv2.rectangle(marked_image, (left, top), (right, bottom), color, 2)

        # Draw a label with a name below the face
        cv2.rectangle(marked_image, (left, bottom + 35), (right, bottom), color, cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(marked_image, name, (left + 8, bottom + 20), font, 0.7, (0, 0, 0), 2)

plt.imshow(marked_image)
plt.title('Caras encontradas')
plt.show()


# Optimizamos el bloque anterior con face_descriptor(lista de vectores a buscar) para evitar exceso consultas:
face_names = []

dets = detector(iron_maiden_color, 1)
tolerance = 0.1  # distancia máxima que permitimos entre o vector almacenado e o actual
face_descriptors = [list(face_rec.compute_face_descriptor(iron_maiden_color, sp(iron_maiden_color, d))) for d in dets]
results = collection.query(query_embeddings=face_descriptors,
                           n_results=1
                           )
found_faces = [position for position, distances in enumerate(results['distances']) for distance in distances if
               distance < tolerance]
for pos_face, d in enumerate(dets):
    name = results['metadatas'][pos_face][0]['nombre'] if pos_face in found_faces else "Ignoto"
    face_names.append(((d.top(), d.right(), d.bottom(), d.left()), name))

marker_image = iron_maiden_color.copy()
for (top, right, bottom, left), name in face_names:
    # Scale back up face locations since the frame we detected in was scaled to 1/4 size

    color = (0, 255, 0)
    if name == "Ignoto":
        color = (0, 0, 255)
    # Draw a box around the face
    cv2.rectangle(marker_image, (left, top), (right, bottom), color, 2)

    # Draw a label with a name below the face
    cv2.rectangle(marker_image, (left, bottom + 35), (right, bottom), color, cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(marker_image, name, (left + 8, bottom + 20), font, 0.7, (0, 0, 0), 2)

plt.imshow(marker_image)
plt.title('Caras encontradas')
plt.show()
