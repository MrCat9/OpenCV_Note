# -*- coding: utf-8 -*-
# 摘自 https://blog.csdn.net/qq_41895190/article/details/82791426


import cv2
from color_identify import colorList


# filename = 'data/id_12.png'
filename = 'data/id_1.jpg'
output_dir = 'output'


# 处理图片
def get_color(im):
    print('go in get_color')

    cv2.imshow('im', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 增强对比度
    # im = cv2.convertScaleAbs(im, alpha=1.5, beta=0)
    # cv2.imshow('im', im)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv', hsv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    maxsum = -100
    color = None
    color_dict = colorList.getColorList()
    for d in color_dict:
        mask = cv2.inRange(hsv, color_dict[d][0], color_dict[d][1])
        cv2.imwrite(output_dir + '/' + d + '.jpg', mask)
        binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
        binary = cv2.dilate(binary, None, iterations=2)
        # img, cnts, hiera = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts, hiera = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        sum = 0
        for c in cnts:
            sum += cv2.contourArea(c)
        if sum > maxsum:
            maxsum = sum
            color = d

    return color


if __name__ == '__main__':
    im = cv2.imread(filename)
    print(get_color(im))
