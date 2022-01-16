import imp
from PIL import Image
import json
import os
from settings import *

colors = json.load(open('colors.json'))
color_to_hex = lambda x: '#{:02x}{:02x}{:02x}{:02x}'.format(*x)

img = Image.open(TEMPLATES_PATH + 'faces/face1.png')

# print(colors["faces"][0])

for x in range(X_SIZE):
    for y in range(Y_SIZE):
        if img.getpixel((x, y)) == (255, 255, 255, 255):
            img.putpixel((x, y), (0, 255, 0, 255))

img.show()

        

