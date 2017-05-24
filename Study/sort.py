#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:25:14 2017

@author: frank
"""

def buble_sort(l):
    print 'buble_sort:'
    for i in range(len(l)):
        for j in range(len(l)-1):
            if (l[j]>l[j+1]):
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
        print 'No.'+str(i)+' step is '
        print l
    print ''
    print l
    
def select_sort(l):
    print 'select_sort:'
    for i in range(len(l)):
        for j in range(i,len(l)):
            if l[i]>l[j]:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
        print 'No.'+str(i)+' step is '
        print l       
    print ''
    print l 

def insert_sort(l):
    print 'insert_sort:'   
    for i in range(len(l)):
        for n in range(i):#yi fen qu bu fen                
            j=i
            if l[i]<l[n]:
                temp=l[i]                   
                while j>n:
                    l[j]=l[j-1]
                    j=j-1                       
                l[n]=temp
        print 'No.'+str(i)+' step is '
        print l
        print ''
#            print 'No.'+str(j)+' step is '
#            print l
    print ''
    print l               
               
if __name__=='__main__':
    L=[9,8,4,1,7,3,2,0]
    #buble_sort(L)
    #select_sort(L)
    insert_sort(L)