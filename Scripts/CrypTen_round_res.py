import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# 数据
categories = ['Matmul', 'Gelu',   'Softmax']
values1 = [346,144,1632]
values2 = [346, 156, 1740]
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

# X轴的位置
x = np.arange(len(categories))
colors = plt.cm.tab10(np.linspace(0, 1, 10))
from matplotlib.font_manager import FontProperties

# 确认Times New Roman字体是否可用
font = FontProperties()
# font.set_family('serif')
font.set_name('Times New Roman')
font.set_size(13)
# 宽度
font1 = FontProperties()
font1.set_family('serif')
font1.set_name('Times New Roman')
font1.set_size(11)
width = 0.33
from pylab import mpl
# 绘制柱状图

fig, ax = plt.subplots() 
rects1 = ax.bar(x - 0.5*width, values1, width, color='#8ECFC9', label='CrypTen', hatch='/')
rects2 = ax.bar(x + 0.5*width, values2, width,color='#FFBE7A', label='HawkEye', hatch='\\')

plt.bar_label(rects1, label_type='edge', fontproperties=font1)
plt.bar_label(rects2, label_type='edge', fontproperties=font1)

from matplotlib.font_manager import FontManager


# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
ax.set_xlabel('Model',fontsize = 18, fontproperties='Times New Roman')
ax.set_ylabel('Round Number',fontsize = 18, fontproperties='Times New Roman')
ax.set_xticks(x)
ax.set_xticklabels(categories, fontproperties=font)
plt.yscale('log')
# 添加图例
ax.tick_params(axis='y',  labelsize= 15)
ax.tick_params(axis='x',  labelsize= 15)

ax.legend(prop = {'size':11, 'family': 'Times New Roman'})
plt.tight_layout()

# 显示图形
plt.show()
plt.savefig('round_crypTen.pdf')


