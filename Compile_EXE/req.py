from os import system

def dialog_box(text):
    db = open('message.vbs', 'w')
    text = 'x = msgbox("'+text+'",4096,"Cryptify")'
    db.write (text)
    db.close()
    system('message.vbs')
    system('del /s message.vbs')

dialog_box("Cryptify only works on Python 3.9. Please uninstall any other version of python, if present.")
system(r'"powershell.exe  "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('+"'"+'https://community.chocolatey.org/install.ps1'+"'"'))"')
system("C:\ProgramData\chocolatey\bin\choco.exe install python --version=3.9.0 -y")
system("pip install opencv-python")
system("pip install dlib-19.22.99-cp39-cp39-win_amd64.whl")
system("pip install face_recognition")
dialog_box("Requirements installed! If anything doesn't work, restart the app and re-install requirements from Help section of Cryptify.")