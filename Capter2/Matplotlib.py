# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

x = np.linspace(-10,10,2000)
y = np.sin(x)+1
z = np.cos(x**2)+1

myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simhei.ttf')

plt.rcParams['font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
plt.figure(figsize = (8,4))
plt.plot(x,y,label = '$\sin x+1$',color='red',linewidth=2)
plt.plot(x,z,'b--',label = '$cos x^2+1$')
plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title(u'例子',fontproperties=myfont)
plt.ylim(0,2.2)
plt.legend()
plt.show()
