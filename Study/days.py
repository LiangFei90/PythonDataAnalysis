#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:51:00 2017

@author: frank

题目：输入某年某月某日，判断这一天是这一年的第几天？
"""
def yearLearn(y):
    y=int(y)
    if y%400==0 or(y%4==0 and y%100!=0):
        return 1
    else:
        return 0

inp=input('please input like "2001-01-01":\n')
print inp
L=inp.split('-')
flag=yearLearn(L[0])
dir1={"1":31,"2":60,"3":91,"4":121,"5":152,"6":182,"7":213,"8":244,"9":274,"10":305,"11":335}
dir2={"1":31,"2":59,"3":90,"4":120,"5":151,"6":181,"7":212,"8":243,"9":273,"10":304,"11":334}
if flag==1:
    days=dir1[str(int(L[1])-1)]+int(L[2])
    print days
if flag==0:
    days=dir2[str(int(L[1])-1)]+int(L[2])
    print days
    
    
