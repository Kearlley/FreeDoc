import os

os.system("pyinstaller -F .\\main.py")
try:
    os.system("move .\\dist\\main.exe .\\dist\\FreeDoc-Windows.exe")
except:
    os.system("mv .\\dist\\main.exe .\\dist\\FreeDoc-Linux")
