import cv2
import os
import requests
import string
from pathlib import Path
from random import choice
from PIL import Image

IMAGE_COUNT = 10
OUTPUT = 'images'
IMAGE_TYPE = 'jpg'

EXCLUDE = 'exclude'

def create_folder():
    if not Path(OUTPUT).exists():
        os.makedirs(OUTPUT)

def clear_images():
    for file in os.listdir(OUTPUT):
        os.remove(os.path.join(OUTPUT, file))

def change_extensions():
    for file in os.listdir(EXCLUDE):
        os.rename(os.path.join(EXCLUDE, file), os.path.join(EXCLUDE, Path(file).stem + '.' + IMAGE_TYPE))

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
        example = Image.open(os.path.join(EXCLUDE, file))
        if list(img.getdata()) == list(example.getdata()):
            return True

    return False

def main():
    create_folder()
    clear_images()
    change_extensions()

    print("Started saving images:")

    i = 0
    while i < IMAGE_COUNT:
        id = generate_id()

        image = 'https://i.imgur.com/' + id + '.jpg'

        directory = OUTPUT + '\image_' + str(i + 1) + '.' + IMAGE_TYPE
        save_image(image, directory)
            
        if (check_empty(directory) or check_exclude(directory)):
            os.remove(directory)
        else:
            print("    Saved image #" + str(i + 1))
            i+=1

    print("Finished saving images.")

main()