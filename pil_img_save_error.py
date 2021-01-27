# -*- coding: utf-8 -*-


import os
from PIL import Image


# img_path = os.path.join('data/png_img.jpg')  # 实际为png图片，文件名编辑错误
img_path = os.path.join('data/jpg_img.jpg')
img_format = img_path.split('.')[-1]  # jpg
result_img_path = img_path[:-(len(img_format) + 1)] + '__result.' + img_format  # 拼接结果图路径

result_img = Image.open(img_path)

channel_num = len(result_img.split())  # 返回图片的通道数
print('channel_num', channel_num)

result_img.save(result_img_path)

# png图片无法保存为.jpg文件
# jpg图片可以保存为.png文件
