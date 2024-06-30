import ctypes
import sys
import os

if not ctypes.windll.shell32.IsUserAnAdmin():
    args = [sys.executable] + sys.argv
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(args), None, 1)
    sys.exit(0)

if os.path.exists("newinstall.bat"):
    os.system("newinstall.bat")
    os.system('start req.exe')

os.system('start Engine.exe')
