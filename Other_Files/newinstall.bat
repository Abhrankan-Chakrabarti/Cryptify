@echo off

@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
C:\ProgramData\chocolatey\bin\choco.exe install python --version=3.9.0 -y
pip install opencv-python
pip install dlib-19.22.99-cp39-cp39-win_amd64.whl
pip install face_recognition

del "%~f0"
