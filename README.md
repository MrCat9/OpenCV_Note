# OpenCV_Note

## 目录

1_opencv按位操作bitwise
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

2_形态学变换
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

3_基本形态学变换_腐蚀与膨胀
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

4_高级形态学变换_morphologyEx函数
```python
im_open = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)
```
```
opencv 形态学变换 morphologyEx函数
https://blog.csdn.net/keen_zuxwang/article/details/72768092
```
