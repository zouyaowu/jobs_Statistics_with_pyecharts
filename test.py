# -*- coding:utf-8 -*-


#二维阵列变换 行转化成列，列转化成行
lista=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
listb = []

#map实现 载入内存
print(list(map(list,zip(*lista))))
