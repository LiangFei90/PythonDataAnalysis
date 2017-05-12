# -*- coding: utf-8 -*-
# 菜品盈利数据 怕累托图
from __future__ import print_function
import pandas as pd
import matplotlib.pyplot as plt

dish_profit='C:\PythonDataAnalysisAndMining\Sources\chapter3\demo\data\catering_dish_profit.xls'
data=pd.read_excel(dish_profit,index_col=u'菜品名')
data=data[u'盈利'].copy()
data.sort(ascending=False)
plt.rcParams['font.sans-serif']=['SimHei']
plt.figure()#建立图像
data.plot(kind='bar')#柱状图
plt.ylabel(u'盈利（元）')
p=1.0*data.cumsum()/data.sum()
p.plot(color='r',secondary_y=True,style='-o',linewidth=2)
plt.annotate(format(p[6],'.4%'),xy=(6,p[6]),xytext=(6*0.9,p[6]*0.9),arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
plt.ylabel(u'盈利(比例)')
plt.show()
