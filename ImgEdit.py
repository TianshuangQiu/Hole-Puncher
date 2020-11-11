import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import random
import os

# Make canvas and set the color
height = 100
width = 1000
img = np.zeros((height, width, 3), np.uint8)
b, g, r, a = 255, 255, 255, 0

# Use cv2.FONT_HERSHEY_XXX to write English.

def put_text(text):
    my_path = os.path.dirname(__file__)
    fontpath = my_path + "/fonts/English.ttf"  # <== 这里是宋体路径
    img1 = np.zeros((height, width, 3), np.uint8)
    font = ImageFont.truetype(fontpath, 70)

    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((30, 10), text, stroke_height=1, font=font, fill=(b, g, r))
    img1 = np.array(img_pil)
    return img1

def draw_circle(input):
    tmp = input
    for x in range (0,10):
        w = random.randint(0,width)
        h = random.randint(0,height)
        print(h,w)
        tmp = cv2.circle(img, (w,h), 30, (255, 255, 255), -1)

    return tmp



def scatter():
    count = 0
    for x in range (0,height):
        for y in range (0,width):
            curr_val = img[x][y]
            rand = random.randint(0,100)
            if rand>20:
                img[x][y] = [0, 0, 0]

img = put_text("hello, this is a test sentence")
#img = draw_circle(img)
scatter()
cv2.imwrite("res.png", img)
