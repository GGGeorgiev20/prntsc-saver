from tkinter import N
import cv2
import os
import requests
import string
from pathlib import Path
from random import choice
from PIL import Image

IMAGE_COUNT = 10
IMAGE_TYPE = 'jpg'

OUTPUT = 'images'
EXCLUDE = 'exclude'

def create_folders():
    if not Path(OUTPUT).exists():
        os.makedirs(OUTPUT)
    if not Path(EXCLUDE).exists():
        os.makedirs(EXCLUDE)

def clear_images():
    for file in os.listdir(OUTPUT):
        os.remove(os.path.join(OUTPUT, file))

def change_extensions():
    name = ''
    for i in range(2):
        j = 0
        for file in list(Path(EXCLUDE).iterdir()):
            if file.suffix == '.txt':
                continue
            if i == 1:
                name = 'exclude_'
            os.rename(file, os.path.join(EXCLUDE, name + str(j) + '.' + IMAGE_TYPE))
            j += 1

def generate_id():
    numbers = '0123456789'
    letters = string.ascii_lowercase
    
    random_numbers = ''.join(choice(numbers) for i in range(2))
    random_letters = ''.join(choice(letters) for i in range(4))

    return random_numbers + random_letters

def check_empty(image):
    img = cv2.imread(image)

    return img is None

def save_image(image, directory):
    with open(directory, 'wb') as f:
        res = requests.get(image)
        f.write(res.content)

def check_exclude(image):
    img = Image.open(image)

    for file in os.listdir(EXCLUDE):
        if Path(file).suffix == '.txt':
            continue
        example = Image.open(os.path.join(EXCLUDE, file))
        if list(img.getdata()) == list(example.getdata()):
            return True

    return False

def main():
    create_folders()
    clear_images()
    change_extensions()

    print("Started saving images:")

    i = 0
    while i < IMAGE_COUNT:
        id = generate_id()

        image = 'https://i.imgur.com/' + id + '.jpg'

        directory = OUTPUT + '\image_' + str(i + 1) + '.' + IMAGE_TYPE
        try:
            save_image(image, directory)
                
            if (check_empty(directory) or check_exclude(directory)):
                os.remove(directory)
            else:
                print("    Saved image #" + str(i + 1) + " (ID: " + id + ")")
                i += 1
        except:
            print("    Error saving image #" + str(i + 1) + " (ID: " + id + ")")
            print("    Trying again...")

    print("Finished saving images.")

main()