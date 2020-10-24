import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time
import os

## Make canvas and set the color
img = np.zeros((200,1000,3),np.uint8)
b,g,r,a = 255,255,255,0

## Use cv2.FONT_HERSHEY_XXX to write English.
text = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime())
cv2.putText(img,  "This is a statement", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (b,g,r))


## Use simsum.ttc to write Chinese.
def get_img(name):
    my_path = os.path.dirname(__file__)
    fontpath = my_path + "/fonts/English.ttf" # <== 这里是宋体路径
    img1 = np.zeros((500, 700, 3), np.uint8)
    font = ImageFont.truetype(fontpath, 50)

    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((50, 80),  "这是一句话", font = font, fill = (b, g, r))
    img1 = np.array(img_pil)
    return img1


img = get_img("f")
img = cv2.circle(img, (120, 50), 20, (255, 255, 255), -1)
img = cv2.circle(img, (350, 20), 50, (255, 255, 255), -1)
img = cv2.circle(img, (100, 90), 30, (255, 255, 255), -1)

## Display
cv2.imwrite("res.png", img)
