import face_recognition
import pickle

def match(id):
    known_encoding = pickle.load(open("models/" + id + ".pkl", "rb"))
    unknown_image = face_recognition.load_image_file("uploads/tmp.jpg")
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    results = face_recognition.compare_faces([known_encoding], unknown_encoding)
    print(results)
    return results[0]


