from src.spriteGenerator import SpriteGenerator
import random

# c - color
# SpriteGenerator(bg, (f, h, e), (fc, hc, ec))

def generate_random(amount):
    for _ in range(amount):
        bg = random.randint(0, 3)

        f = random.randint(0, 1)
        h = random.randint(0, 6)
        e = random.randint(0, 5)

        fc = random.randint(0, 3)
        hc = random.randint(0, 3)
        ec = random.randint(0, 2)
        sprite = SpriteGenerator(bg, (f, h, e), (fc, hc, ec))
        sprite.img.save('out/{}{}{}{}{}{}{}.png'.format(bg, f, h, e, fc, hc, ec))


# SpriteGenerator(3, (0, 5, 5), (0, 1, 1)).img.save('my_sprite.png')

if __name__ == '__main__':
    generate_random(10)


