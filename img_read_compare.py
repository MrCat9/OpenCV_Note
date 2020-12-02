# -*- coding: utf-8 -*-
# 三个图像包读图对比


import cv2
from skimage import io
from PIL import Image
import matplotlib.pyplot as plt


img_path = 'data/test_data/tt06.png'

# cv2
img1 = cv2.imread(img_path)  # BGR
cv2.imshow('img1', img1)

# skimage
img2 = io.imread(img_path)  # RGB
plt.figure()
ax = plt.subplot(111)
ax.imshow(img2)
plt.show()

# PIL
img3 = Image.open(img_path)
img3.show()

# array转PIL
img31 = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
img31.show()
img32 = Image.fromarray(img2)
img32.show()


cv2.waitKey(0)
cv2.destroyAllWindows()

