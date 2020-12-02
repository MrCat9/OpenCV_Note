# OpenCV_Note

文档  https://docs.opencv.org/4.1.0/d6/d00/tutorial_py_root.html

## 目录

#### 1_opencv按位操作bitwise
```
bitwise_and
bitwise_or
bitwise_xor
bitwise_not

按位操作-bitwise operations
https://www.jianshu.com/p/003e9451cdc4

图像基本运算(bitwise)及掩膜(mask)
https://blog.csdn.net/u011028345/article/details/77278467
```

#### 2_形态学变换
```
基本形态学变换：
腐蚀 erode （有0出0） （分割(isolate)独立的图像元素）
膨胀 dilate （有1出1） （连接(join)相邻的元素）

高级形态学变换：  morphologyEx函数
开运算 MORPH_OPEN （先腐蚀，再膨胀）（去除小白点）
闭运算 MORPH_CLOSE （先膨胀，再腐蚀）（去除小黑点）
梯度 MORPH_GRADIENT （膨胀图-腐蚀图）（提取物体边缘）
顶帽 MORPH_TOPHAT （原图像-开运算图）（突出原图像中比周围亮的区域）
黑帽 MORPH_BLACKHAT （闭运算图-原图像）（突出原图像中比周围暗的区域）
```

#### 3_基本形态学变换_腐蚀与膨胀
```python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # getStructuringElement 可以方便的生成一个矩阵（kernel）
im_erode = cv2.erode(src, kernel)  # 腐蚀

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
im_dilate = cv2.dilate(src, kernel)  # 膨胀
```
```
膨胀与腐蚀
https://www.cnblogs.com/ssyfj/p/9276999.html

getStructuringElement函数
https://blog.csdn.net/u014737138/article/details/80374666
```

#### 4_高级形态学变换_morphologyEx函数
```python
im_open = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)
```
```
opencv 形态学变换 morphologyEx函数
https://blog.csdn.net/keen_zuxwang/article/details/72768092
```

#### 5_验证码识别
```
Python3 识别验证码（opencv-python）
https://www.cnblogs.com/lizm166/p/9969647.html
降噪  高斯模糊
字符切割  findContours获取轮廓+boundingRect获取轮廓的x, y, w, h（x为轮廓最左点的x，y为最上点的y，w为最右点x-最左点x的差，h为最下点y-最上点y的差）

Python验证码识别
https://www.cnblogs.com/qqandfqr/p/7866650.html
二值化  cv2.adaptiveThreshold自适应阀值二值化
去除边框
线降噪  4邻域
点降噪  9邻域

python实现opencv学习二十四：识别验证码
https://blog.csdn.net/u011321546/article/details/79647179
降噪  getStructuringElement+morphologyEx

KNN 验证码识别
https://www.cnblogs.com/xuchunlin/p/9456593.html
https://blog.csdn.net/weixin_40267472/article/details/81384624
```

#### 6_在线RGB工具 https://www.fontke.com/tool/rgb/

#### [7_Python3识别判断图片主要颜色，提取指定颜色](https://github.com/MrCat9/OpenCV_Note/tree/master/color_identify)

https://blog.csdn.net/qq_41895190/article/details/82791426

```
HSV(hue,saturation,value)颜色空间
cv2.inRange(src, lowerb, upperb, dst=None)  # 根据范围选择，在范围内的点变为255（白色），不在范围内的变为0（黑色）
```

#### [8_三个图像包读图对比](https://github.com/MrCat9/OpenCV_Note/tree/master/img_read_compare.py)

```
cv2
skimage
PIL
```
