import os

os.system("pyinstaller main.spec")
try:
    os.system("move .\\dist\\main.exe .\\dist\\FreeDoc-Windows.exe")
except:
    os.system("mv .\\dist\\main.exe .\\dist\\FreeDoc-Linux")
