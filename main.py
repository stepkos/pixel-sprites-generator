from src.spriteGenerator import SpriteGenerator
import random
# background face, hair    face_color, hair_color


for _ in range(10):
    bg = random.randint(0, 3)

    f = random.randint(0, 1)
    h = random.randint(0, 4)
    e = random.randint(0, 2)

    fc = random.randint(0, 3)
    hc = random.randint(0, 3)
    ec = random.randint(0, 2)
    sprite = SpriteGenerator(bg, (f, h, e), (fc, hc, ec))
    sprite.img.save('out/{}{}{}{}{}{}{}.png'.format(bg, f, h, e, fc, hc, ec))



