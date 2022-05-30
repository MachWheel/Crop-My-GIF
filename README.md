<p align="center"><img src="/docs/source/_static/logo.png?raw=true" alt="Crop My GIF Logo"></p>
<h1 align="center">Crop My GIF</h1>
<p align="center"><i>A practical way to crop large GIF animation files.</i></p>

<p align="center"><img src="/docs/source/_static/demo_v12.gif?raw=true" alt="Crop My GIF DEMO"></p>

# Documentation
### [crop-my-gif.readthedocs.io](http://crop-my-gif.readthedocs.io/)

# How to use it
  1. Choose a GIF file 
  2. Click the image to select the crop start/end positions
  3. Check if the output size is correct
      - *Press "Clear Selection" if you want to select again*
  4. Check if you want to preserve the input GIF fps
      - *"Preserve FPS" will take longer to export*
  5. Press "Crop My GIF" to export it
  6. Done!

# How to install it
Just download the zip at *Releases*, extract and run the .exe file. No installation needed.

# Is it "portable"?
**Yes!** In other words, you need just **Crop-My-GIF.exe** to run this app. 
To uninstall, just delete it.

# Cloning the repository:

First, open the command-line and check your Python version. This app was made using **Python 3.10.3**:

    py --version


Now, install virtualenv if you don't have it:
    
    py -m pip install virtualenv


Clone the repository and change the directory to it:
    
    git clone https://github.com/MachWheel/Crop-My-GIF.git
    cd Crop-My-GIF


Create a virtualenv for the project, then activate it:
    
    py -m venv venv
    .\venv\Scripts\activate


Install project dependencies:
    
    py -m pip install -r requirements.txt


Done. Now you can run the app typing:

    py main.py


# How to compile it:

### First: [clone the repository and properly configure its virtualenv (see above)](#cloning-the-repository)
### Second: change to the directory and activate virtualenv if it is not already activated.

    cd Crop-My-GIF
    .\venv\Scripts\activate

## Easy way:

### Inside Crop-My-GIF virtualenv, change the directory to compile and run the script:

    cd compile
    .\compile.bat
    
![COMPILE](https://s8.gifyu.com/images/compile-crop-my-gif.gif)

  - **The folder containing the generated .exe file will be opened automatically**

## Manual way:

Inside Easy-Gifer virtualenv, change the directory to compile folder and run pyinstaller:

    cd compile
    pyinstaller -w --onefile ..\main.py --icon app.ico --name Crop-My-GIF --splash splashfile.jpg
    
  - **The generated .exe file will be in .\compile\dist folder.**

## requirements.txt

    imageio==2.18.0
    imageio-ffmpeg==0.4.7
    moviepy==1.0.3
    Pillow==9.1.0
    pyinstaller==5.0.1
    pyinstaller-hooks-contrib==2022.4
    PySimpleGUI==4.59.0
    pywin32-ctypes==0.2.0
    screeninfo==0.8
    
