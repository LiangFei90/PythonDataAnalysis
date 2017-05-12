import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#x=[1,2,3,4,5,6,7]
#y=[5,7,2,9,3,0,5]
#
#plt.ylim=(0,10)
#plt.plot(x,y)
#plt.show()
inputfile='C:\Users\LiangFei\Desktop\PythonDataAnalysis\Capter6\mising_data_processed.xls'
data=pd.read_excel(inputfile,header=None)

for i in range(len(data)):
    y=data[i]
    x=list(range(len(data[i])))
    plt.plot(x,y)
    plt.show()