# Cloning the repository

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
