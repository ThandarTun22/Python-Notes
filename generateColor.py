

import random
from sty import fg

def generatorRGB():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return red, green, blue

def generatorColour(red, green, blue):
    return fg(red, green, blue)

red, green, blue = generatorRGB()
color = generatorColour(red, green, blue)
# print(red, green, blue)
print(color, "I'm randaomly changing colors")