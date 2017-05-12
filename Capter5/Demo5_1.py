# -*- coding: utf-8 -*-
import pandas as pd

filename='C:\PythonDataAnalysisAndMining\Sources\chapter5\demo\data\\bankloan.xls'
data=pd.read_excel(filename)
x=data.iloc[:,:8].as_matrix()#取1~8列
                #as_matrix()  Convert the frame to its Numpy-array representation.
y=data.iloc[:,8].as_matrix()#取第九列

print x
print y
