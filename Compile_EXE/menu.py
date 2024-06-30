import tkinter as tk
from sys import argv
from os import system

def lock_or_unlock(n):
    n = int(n)
    def lock():
        root.destroy()
        system ('start branch.exe ' + str(n * 2 - 1))

    def unlock():
        root.destroy()
        system ('start branch.exe ' + str(n * 2))

    root = tk.Tk()

    lock_button = tk.Button(root, text="Lock", command=lock)
    lock_button.pack()

    unlock_button = tk.Button(root, text="Unlock", command=unlock)
    unlock_button.pack()

    root.mainloop()

lock_or_unlock(argv[1])
