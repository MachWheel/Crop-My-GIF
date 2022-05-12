@ECHO OFF
TITLE Crop-My-GIF Compiler
ECHO:
ECHO Crop-My-GIF Compiler
ECHO:
ECHO This batch script compiles Crop-My-GIF application
ECHO:
ECHO Make sure to proper configure the project virutalenv first.
ECHO:
ECHO You should run this script inside the project virtualenv to avoid problems.
ECHO:
ECHO The generated app will be in the ./dist folder
ECHO:
PAUSE
MKDIR dist
pyinstaller -w --onefile ..\main.py --icon app.ico --name Crop-My-GIF
ECHO:
ECHO DONE! PRESS ANY KEY TO OPEN THE OUTPUT FOLDER.
ECHO:
PAUSE
START dist
