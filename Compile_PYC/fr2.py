import cv2
import face_recognition
import numpy as np
import time
from sys import argv
from os import system

def dialog_box(text):
    db = open('message.vbs', 'w')
    text = 'x = msgbox("'+text+'",4096,"Cryptify")'
    db.write (text)
    db.close()
    system('message.vbs')
    system('del /s message.vbs')

a = int(argv[1])

cap = cv2.VideoCapture(0)

capture_time = 10
delay = 0.5

start_time = time.time()
count = 0
found = False

known_image = face_recognition.load_image_file("face.png")
known_face_locations = face_recognition.face_locations(known_image)
known_face_encodings = face_recognition.face_encodings(known_image, known_face_locations)

# Capture 20 photos with a delay of 0.5 seconds per photo
while (time.time() - start_time) < capture_time and count < 20:
    ret, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)

    if len(face_locations) > 0:
        found = True
        x_face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        x_face_encodings = np.array(x_face_encodings)
        Matches = face_recognition.compare_faces(known_face_encodings, x_face_encodings)
        if True in Matches:
            dialog_box("Face matched!")
            system('start UI2.exe '+ str(a))
        else:
            dialog_box("Face doesn't match!")
        break

    count += 1
    time.sleep(delay)


cap.release()
cv2.destroyAllWindows()

