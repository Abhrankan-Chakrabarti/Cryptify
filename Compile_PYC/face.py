import os
from sys import argv
a = str(argv[1])

def dialog_box(text):
    db = open('message.vbs', 'w')
    text = 'x = msgbox("'+text+'",4096,"Cryptify")'
    db.write (text)
    db.close()
    os.system('message.vbs')
    os.system('del /s message.vbs')

if not os.path.exists("face.png"):
    dialog_box("No faces added. Registering face from webcam...")
    os.system("python fr1.pyc ")
else:
    os.system("python fr2.pyc " + a)

