from os import system
import os
from zipfile import ZipFile
import cryptography.fernet as f
from sys import argv,exit
import re

def dialog_box(text):
    db = open('message.vbs', 'w')
    text = 'x = msgbox("'+text+'",4096,"Cryptify")'
    db.write (text)
    db.close()
    system('message.vbs')
    system('del /s message.vbs')

def encrypt_file(file_path,key):
    key = key_to_password(b'A-RyP_uywy6eDXrxsua7dPqKJHK6HO67zBK5lBtj5Hc=',key)
    with open(file_path, 'rb') as file:
        original = file.read()
    fernet = f.Fernet(key)
    encrypted = fernet.encrypt(original)
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    dialog_box("Lock successful!")

def decrypt_file(file_path, key):
    key = key_to_password(b'A-RyP_uywy6eDXrxsua7dPqKJHK6HO67zBK5lBtj5Hc=',key)
    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    fernet = f.Fernet(key)
    decrypted = fernet.decrypt(encrypted)
    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    dialog_box("Unlock successful!")

def key_to_password(key,password)->bytes:
    key_bytes = bytearray(key)
    password_bytes = password.encode()
    key_bytes[10:10+len(password_bytes)] = password_bytes
    new_key = bytes(key_bytes)
    return new_key

def lock_internet(key):
    with open('key', 'w') as f:
        f.write(key)
    encrypt_file('key',key)
    system ('netsh advfirewall firewall add rule name="Block Internet Access" dir=out action=block')
    dialog_box("Lock successful!")

def unlock_internet(key):
    decrypt_file('key',key)
    with open('key', 'r') as f:
        k = f.read()
    if key==k:
        system ('netsh advfirewall firewall delete rule name="Block Internet Access"')
        dialog_box("Unlock successful!")
        system ('del /s key')

def lock_drive(drive_letter):
    system(f'manage-bde -protectors -add {drive_letter}: -pw')
    system(f'manage-bde -lock -ForceDismount {drive_letter}:')
    system('cls')
    
def unlock_drive(drive_letter):
    system(f'manage-bde -unlock {drive_letter}: -password')
    system(f'manage-bde -off {drive_letter}:')
    system('cls')    

def encrypt_directory(path, key):
    base_name = os.path.basename(path)
    zip_name = os.path.join(os.path.dirname(path), base_name + ".zip")
    with ZipFile(zip_name, "w") as zip_obj:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, path)
                zip_obj.write(file_path, arcname=rel_path)
    os.system('rd /s /q '+path)
    encrypt_file(zip_name, key)
    os.rename(zip_name, os.path.join(os.path.dirname(path), base_name + ".zip"))
    dialog_box("Lock successful!")


def decrypt_directory(path, key):
    zip_file = os.path.basename(path)
    dir_name = os.path.splitext(zip_file)[0]
    dir_path = os.path.dirname(path)
    os.rename(path, os.path.join(dir_path, zip_file))
    try:
        decrypt_file(os.path.join(dir_path, zip_file), key)
        output_dir = os.path.join(dir_path, dir_name)
        os.makedirs(output_dir, exist_ok=True)
        with ZipFile(os.path.join(dir_path, zip_file), 'r') as zip_obj:
            zip_obj.extractall(output_dir)
        os.remove(os.path.join(dir_path, zip_file))
        dialog_box("Unlock successful!")
    except:
        os.rename(os.path.join(dir_path, zip_file), os.path.join(dir_path, path))
       

a = int(argv[1])
b = str(argv[2])

if '$' in b:
    dialog_box("File/Folder name cannot contain blank spaces.")
    exit()

c = str(argv[3])
c = re.sub(r'\W+', '', c)

if (a == 1):
    encrypt_file(b,str(c))
elif (a == 2):
    decrypt_file(b,str(c))
elif (a == 3):
    encrypt_directory(b,str(c))
elif (a == 4):
    decrypt_directory(b,str(c))
elif (a == 5):
    lock_drive(b)
elif (a == 6):
    unlock_drive(b)
elif (a == 7):
    lock_internet(str(c))
elif (a == 8):
    unlock_internet(str(c))
