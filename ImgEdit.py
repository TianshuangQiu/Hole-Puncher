import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import random
import os

# Make canvas and set the color
height = 100
width = 400
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

corpus = """以上
以下
以为
以便
以免
以前
以及
以后
以外
以後
以来
以至
以至于
以致
们
任
任何
任凭
任务
企图
伟大
似乎
似的
但
但是
何
何况
何处
何时
作为
你
你们
你的
使得
使用
例如
依
依照
依靠
促进
保持
俺
俺们
倘
倘使
倘或
倘然
倘若
假使
假如
假若
做到
像
允许
充分
先后
先後
先生
全部
全面
兮
共同
关于
其
其一
其中
其二
其他
其余
其它
其实
其次
具体
具体地说
具体说来
"""
words = []
buffer = []
string = ""
for c in corpus:
    if c is "\t" or c is "\n":
        if len(buffer) is not 0:
            words.append(string.join(buffer))
        buffer = []
        continue
    buffer.append(c)

for var in range (0,15):
    word = random.choice(words)
    img = put_text(word)
    num = 10
    draw_circle(img, num)
    img = (255 - img)
    print(word)
    filename ="pic/" + str(num) + word +".png"
    cv2.imwrite(filename, img)
    img = np.zeros((height, width, 3), np.uint8)

