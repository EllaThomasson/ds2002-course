#!/Users/ellathomasson/anaconda3/bin/python


import os

FAV_COLOR = input('What is your favorite color? ')
NAME = input('What is your name? ')
CAREER = input('What career path are you persuing? ' )

os.environ["FAV_COLOR"] = FAV_COLOR
ZIP_ENV1 = os.getenv("FAV_COLOR")
print(ZIP_ENV1)

os.environ["NAME"] = NAME
ZIP_ENV2 = os.getenv("NAME")
print(ZIP_ENV2)

os.environ["CAREER"] = CAREER
ZIP_ENV3 = os.getenv("CAREER")
print(ZIP_ENV3)

