from typing import Iterable
from PIL import Image, ImageColor
from json import load as json_load
from settings import *

color_to_hex = lambda x: '#{:02X}{:02X}{:02X}{:02X}'.format(*x)
color_to_dec = lambda x: ImageColor.getcolor(x, "RGBA")

colors = json_load(open('colors.json'))


class SpriteGenerator:
    def __init__(self, templates: Iterable, colors: Iterable):
        self.img = SpriteGenerator.mix_template(*templates)
        self.img = SpriteGenerator.apply_colors(self.img, *colors)


    @staticmethod
    def override_layer(layer1: Image, layer2: Image) -> Image:
        for x in range(X_SIZE):
            for y in range(Y_SIZE):
                if layer2.getpixel((x, y)) != (0, 0, 0, 0):
                    layer1.putpixel((x, y), layer2.getpixel((x, y)))
                    
        return layer1


    @staticmethod
    def mix_template(face, hair):
        face = Image.open(TEMPLATES_PATH + 'faces/face{}.png'.format(face))
        hair = Image.open(TEMPLATES_PATH + 'hair/hair{}.png'.format(hair))
        return SpriteGenerator.override_layer(face, hair)


    @staticmethod
    def apply_colors(img, face, hair):
        for x in range(X_SIZE):
            for y in range(Y_SIZE):
                color = color_to_hex(img.getpixel((x, y)))
                if color in colors["faces"]:
                    img.putpixel((x, y), color_to_dec(colors["faces"][color][face]))

                elif color in colors["hair"]:
                    img.putpixel((x, y), color_to_dec(colors["hair"][color][hair]))

        return img
