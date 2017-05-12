# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
catering_sale='C:\PythonDataAnalysisAndMining\Sources\chapter3\demo\data\catering_sale.xls'
data=pd.read_excel(catering_sale,index_col=u'日期')
plt.rcParams['font.sans-serif']=['SimHei']
plt.figure()
p=data.boxplot()
x=p['fliers'][0].get_xdata()
y=p['fliers'][0].get_ydata()
y.sort()
print x
print y
for i in range(len(x)):
    if i>0:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
                    #y[i]是显示的标识，xy是此点所在位置，xytext是标识所在的位置
                                                                            
    else:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))
plt.show()