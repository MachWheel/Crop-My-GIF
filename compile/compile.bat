@ECHO OFF
:: This batch file compiles Crop-My-GIF application
:: The generated app is in the ./dist folder
:: First make sure to "pip install -r requirements.txt"
TITLE Crop-My-GIF-v1 Compiler
ECHO:
ECHO Crop-My-GIF-v1 Compiler
ECHO:
ECHO PRESS ANY KEY TO START COMPILING
ECHO:
PAUSE
MKDIR dist
pyinstaller -w --onefile ..\main.py --icon app.ico --name Crop-My-GIF-v1
ECHO:
ECHO DONE! PRESS ANY KEY TO OPEN THE OUTPUT FOLDER.
ECHO:
PAUSE
START dist
