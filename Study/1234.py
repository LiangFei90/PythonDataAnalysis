#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 22:40:06 2017
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？ 

@author: frank
"""

def fu(l):
    n=0
    for i in l:
        for j in l:
            for m in l:
                if i!=j and j!=m and i!=m: 
                    n=n+1
                    s=i*100+j*10+m
                    print ('No.'+str(n)+' is %d'%s)
    print 'total number is '+str(n)
    
if __name__=='__main__':
    L=[1,2,3,4]
    fu(L)