import string
import time
import math
import json
import cv2
import requests
import random
from pathlib import Path
from PIL import Image

json_file = 'properties.json'

def init():
    load_json()
    create_folders()
    clear_images()
    change_extensions()

def load_json():
    content = json.load(open(json_file))
    global IMAGE_COUNT, IMAGE_TYPE, METHOD, OUTPUT, EXCLUDE
    IMAGE_COUNT = content['image_count']
    IMAGE_TYPE = content['image_type']
    METHOD = content['method']
    OUTPUT = content['output']
    EXCLUDE = content['exclude']

def create_folders():
    Path(OUTPUT).mkdir(exist_ok=True)
    Path(EXCLUDE).mkdir(exist_ok=True)

def clear_images():
    for file in list(Path(OUTPUT).iterdir()):
        file.unlink()

def change_extensions():
    name = ''
    for i in range(2):
        j = 0
        for file in list(Path(EXCLUDE).iterdir()):
            if file.suffix == '.txt':
                continue
            if i == 1:
                name = 'exclude_'
            file.rename(Path(EXCLUDE) / (name + str(j) + '.' + IMAGE_TYPE))
            j += 1

def generate_id(method):
    id = ''

    characters = '0123456789' + string.ascii_lowercase
    
    id = ''.join(random.sample(characters, 6))

    return id

def save_image(url, image):
    with open(str(image), 'wb') as f:
        res = requests.get(url)
        f.write(res.content)

def check_empty(image):
    img = cv2.imread(str(image))

    return img is None

def check_exclude(image):
    img = Image.open(str(image))

    for file in list(Path(EXCLUDE).iterdir()):
        if file.suffix == '.txt':
            continue
        example = Image.open(file)
        if list(img.getdata()) == list(example.getdata()):
            return True

    return False

def main():
    init()

    print("Started saving images:")
    start_time = time.time()

    i = 0
    while i < IMAGE_COUNT:
        id = generate_id(METHOD)

        url = 'https://i.imgur.com/' + id + '.jpg'

        directory = Path(OUTPUT) / (str(i + 1) + '_' + str(id) + '.' + IMAGE_TYPE)

        try:
            save_image(url, directory)
                
            if (check_empty(directory) or check_exclude(directory)):
                directory.unlink()
            else:
                print(f"    Saved image #{i + 1} (ID: {id})")
                i += 1
        except:
            print(f"    Error saving image #{i + 1} (ID: {id})")
            print("    Generating new ID...")
            directory.unlink()

    print("Finished saving images.")
    end_time = time.time()

    time_passed = end_time - start_time
    print(f"Time: {math.floor(time_passed / 60):02}:{round(time_passed % 60):02}")

main()