from sys import argv
from os import system

a = int(argv[1])
if a <= 8:
    system('start UI.exe '+ str(a))
else:
    system('python face.pyc '+ str(a-8))
