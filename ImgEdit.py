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
    fontpath = my_path + "/fonts/Chinese.ttf"  # <== 这里是宋体路径
    img1 = np.zeros((height, width, 3), np.uint8)
    font = ImageFont.truetype(fontpath, 70)

    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((10, 10), text, stroke_height=1, font=font, fill=(b, g, r))
    img1 = np.array(img_pil)
    return img1

def draw_circle(input, n):
    tmp = input
    for x in range (0,n):
        w = random.randint(0,width)
        h = random.randint(0,height)
        print(h,w)
        tmp = cv2.circle(img, (w,h), random.randint(10,30), (255, 255, 255), -1)

    return tmp

def scatter(threshold):
    for x in range (0,height):
        for y in range (0,width):
            rand = random.randint(0,100)
            if rand>threshold:
                img[x][y] = [0, 0, 0]

corpus =[]
with open ("Corpus_CN", "r") as myfile:
    corpus=myfile.readlines()
words = []

string = ""
for c in corpus:
    buffer = []
    if "\t" in c:
        buffer = c.split("\t")
        for item in buffer:
            words.append(item)
        continue
    words.append(c)
"""
for var in range (1,2):
    word = random.choice(words)
    img = put_text(word)
    num = var
    #draw_circle(img, num)
    scatter(num)
    img = (255 - img)
    print(word)
    filename ="pics_scatter/" + str(num) + word +".png"
    cv2.imwrite(filename, img)
    img = np.zeros((height, width, 3), np.uint8)
"""
phrase = "樱桃向下一格"
num = 3
img = put_text(phrase)
scatter(num)
img = (255 - img)
print(phrase)
filename ="phrases_scatter/" + str(num) + phrase +".png"
cv2.imwrite(filename, img)
