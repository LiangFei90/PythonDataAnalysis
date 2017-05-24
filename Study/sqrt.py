#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:23:43 2017

@author: frank

题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？ 
程序分析：循环计算即可，判断成立即可输出。首先要判断是否为正整数。引入math模块算平方根。
"""
import math
import types

for i in range(10000):
    if (math.sqrt(i+100)-int(math.sqrt(i+100))==0) and (math.sqrt(i+268)-int(math.sqrt(i+268))==0):
        print i
        print ("%d %d"%(i+100 ,i+268))
        print ("%f %f"%(math.sqrt(i+100),math.sqrt(i+268)))

    