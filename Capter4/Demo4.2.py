# -*- coding: utf-8 -*-
#数据规范化
import pandas as pd
import numpy as np

datafile='C:\PythonDataAnalysisAndMining\Sources\chapter4\demo\data\\normalization_data.xls'
data=pd.read_excel(datafile,header=None)
dataM_N=(data-data.min())/(data.max()-data.min())
dataM_M=(data-data.mean())/data.std()
dataF=(data/10**np.ceil(np.log10(data.abs().max())))

print data
print dataM_N
print dataM_M
print dataF