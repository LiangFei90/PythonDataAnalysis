# -*- coding: utf-8 -*-
#餐饮销量数据相关性分析+
from __future__ import print_function
import pandas as pd
catering_sale='C:\PythonDataAnalysisAndMining\Sources\chapter3\demo\data\catering_sale_all.xls'
data=pd.read_excel(catering_sale,index_col=u'日期')

print (data.corr())
print(data.corr()[u'百合酱蒸凤爪'])
print(data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺']))