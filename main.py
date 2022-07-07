import cv2
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

def generate_id():
    numbers = '0123456789'
    letters = string.ascii_lowercase

    random = []
    for i in range(2):
        random.append(choice(numbers))
    for i in range(4):
        random.append(choice(letters))

    id = ''
    for i in range(6):
        symbol = choice(random)
        id += symbol
        random.remove(symbol)

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
    create_folders()
    clear_images()
    change_extensions()

    print("Started saving images:")

    i = 0
    while i < IMAGE_COUNT:
        id = generate_id()

        url = 'https://i.imgur.com/' + id + '.jpg'

        directory = Path(OUTPUT) / (str(i + 1) + '_' + str(id) + '.' + IMAGE_TYPE)

        try:
            save_image(url, directory)
                
            if (check_empty(directory) or check_exclude(directory)):
                directory.unlink()
            else:
                print("    Saved image #" + str(i + 1) + " (ID: " + id + ")")
                i += 1
        except:
            print("    Error saving image #" + str(i + 1) + " (ID: " + id + ")")
            print("    Generating new ID...")

    print("Finished saving images.")

main()