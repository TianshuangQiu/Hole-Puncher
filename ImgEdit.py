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


def get_img():
    my_path = os.path.dirname(__file__)
    fontpath = my_path + "/fonts/English.ttf"  # <== 这里是宋体路径
    img1 = np.zeros((height, width, 3), np.uint8)
    font = ImageFont.truetype(fontpath, 70)

    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((20, 25),  "你听懂了吗", stroke_height=1, font=font, fill=(b, g, r))
    img1 = np.array(img_pil)
    return img1


img = get_img()

count = 0
for x in range (0,height):
    for y in range (0,width):
        curr_val = img[x][y]
        rand = random.randint(0,100)
        if rand<20:
            img[x][y] = [255,255,255]
            count+=1
        if rand>80:
            img[x][y] = [0, 0, 0]
            count += 1

# Display
cv2.imwrite("res.png", img)
