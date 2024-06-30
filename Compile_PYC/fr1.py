import cv2
import face_recognition
import time
from os import system

def dialog_box(text):
    db = open('message.vbs', 'w')
    text = 'x = msgbox("'+text+'",4096,"Cryptify")'
    db.write (text)
    db.close()
    system('message.vbs')
    system('del /s message.vbs')

cap = cv2.VideoCapture(0)

capture_time = 10  
delay = 0.5 

start_time = time.time()
count = 0

while (time.time() - start_time) < capture_time and count < 20:
    ret, frame = cap.read()

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)

    if len(face_locations) > 0:
        cv2.imwrite("face.png", frame)
        dialog_box("Face added successfully! Please restart the app!")
        break

    count += 1
    time.sleep(delay)

cap.release()
cv2.destroyAllWindows()