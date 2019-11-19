import face_recognition
import joblib

def match(id):
    known_encoding = joblib.load("models/" + id + ".pkl")
    unknown_image = face_recognition.load_image_file("uploads/tmp.jpg")
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    results = face_recognition.compare_faces([known_encoding], unknown_encoding)
    print(results)
    return results[0]

def encode(id):
    known_image = face_recognition.load_image_file("tmp/tmp.jpg")
    known_encoding = face_recognition.face_encodings(known_image)[0]
    joblib.dump(known_encoding, "models/" + id + ".pkl")
    return True



