import cv2
import os
import requests
import string
from random import choice
from PIL import Image

image_count = 10
output = 'images'
image_type = 'jpg'

example = Image.open('other\\no_exist.png')

def clear_images():
    for file in os.listdir(output):
        os.remove(os.path.join(output, file))

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

def check_not_exist(image):
    img = Image.open(image)

    return list(img.getdata()) == list(example.getdata())

clear_images()
print("Started saving images:")

i = 0
while i < image_count:
    id = generate_id()

    image = 'https://i.imgur.com/' + id + '.jpg'

    directory = output + '\image_' + str(i + 1) + '.' + image_type
    save_image(image, directory)
        
    if (check_empty(directory) or check_not_exist(directory)):
        os.remove(directory)
    else:
        print("    Saved image #" + str(i + 1))
        i+=1

print("Finished saving images.")