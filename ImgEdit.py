import cv2
import numpy as np

# white blank image
blank_image2 = 255 * np.ones(shape=[512, 1024, 3], dtype=np.uint8)
# font
font = cv2.FONT_HERSHEY_PLAIN

# org
org = (0, 200)

# fontScale
fontScale = 2

# Blue color in BGR
color = (0, 0, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.putText() method
image = cv2.putText(blank_image2, '检体', org, font,
                    fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow("White Blank", blank_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()