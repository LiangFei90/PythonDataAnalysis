#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 17:17:32 2017

@author: frank

题目：输入三个整数x,y,z，请把这三个数由小到大输出
"""

x=input('x=')
y=input('y=')
z=input('z=')

if x>=y:
    min=y
    if z<min:
        print (z,y,x)题目：用*号输出字母C的图案。 
    if min<z<x:
        print (y,z,x)
    elif z>x:
        print (y,x,z)
    
else:
    min=x
    if z<x:
        print(z,x,y)
    elif min<z<y:
        print(x,z,y)
    elif z>y:
        print(x,y,z)
    