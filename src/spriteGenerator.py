from ast import Str
from typing import Iterable
from PIL import Image, ImageColor
from json import load as json_load
from settings import *

color_to_hex = lambda x: '#{:02X}{:02X}{:02X}{:02X}'.format(*x)
color_to_dec = lambda x: ImageColor.getcolor(x, "RGBA")

colors = json_load(open('colors.json'))


class SpriteGenerator:
    def __init__(self, bg: int, templates: Iterable, colors: Iterable):
        self.img = SpriteGenerator.mix_template(bg, *templates)
        self.img = SpriteGenerator.apply_colors(self.img, *colors)


    @classmethod
    def generate_by_id(id: str):
        pass


    @staticmethod
    def override_layer(layer1: Image, layer2: Image) -> Image:
        for x in range(X_SIZE):
            for y in range(Y_SIZE):
                if layer2.getpixel((x, y)) != (0, 0, 0, 0):
                    layer1.putpixel((x, y), layer2.getpixel((x, y)))

        return layer1


    @staticmethod
    def mix_template(bg, face, hair, eyes):
        img = Image.open(TEMPLATES_PATH + 'bgs/bg{}.png'.format(bg))
        face = Image.open(TEMPLATES_PATH + 'faces/face{}.png'.format(face))
        hair = Image.open(TEMPLATES_PATH + 'hair/hair{}.png'.format(hair))
        eyes = Image.open(TEMPLATES_PATH + 'eyes/eyes{}.png'.format(eyes))
        img = SpriteGenerator.override_layer(img, face)
        img = SpriteGenerator.override_layer(img, eyes)
        img = SpriteGenerator.override_layer(img, hair)

        return img


    @staticmethod
    def apply_colors(img, face, hair, eyes):
        for x in range(X_SIZE):
            for y in range(Y_SIZE):
                color = color_to_hex(img.getpixel((x, y)))
                if color == '#000000FF':
                    img.putpixel((x, y), (0, 0, 0, 255))

                elif color in colors["faces"]:
                    img.putpixel((x, y), color_to_dec(colors["faces"][color][face]))

                elif color in colors["hair"]:
                    img.putpixel((x, y), color_to_dec(colors["hair"][color][hair]))

                elif color in colors["eyes"]:
                    img.putpixel((x, y), color_to_dec(colors["eyes"][color][eyes]))
                
                elif color != '#FFFFFFFF':
                    img.putpixel((x, y), color_to_dec(color))

        return img
