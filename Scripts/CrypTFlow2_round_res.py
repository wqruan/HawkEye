import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 数据
categories = ['DenseNet-121', 'ResNet-50',   'MobilleNet-V3', 'ShuffleNet-V2']
values1 = [10317, 7155, 12131, 6827]
values2 = [10278, 7148, 2232, 1745]
values3 = [1340, 582, 2252, 608]
values4 = [1313, 575, 2125, 599]
values5 = [720, 438, 612, 270]
values6 = [720, 414, 612, 246]
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
width = 0.15
from pylab import mpl
# 绘制柱状图

fig, ax = plt.subplots(figsize=(6 * 2.2, 4)) 
rects1 = ax.bar(x - 2.5*width, values1, width, color='#8ECFC9', label='CrypTFlow2-Conv2d', hatch='/')

rects2 = ax.bar(x - 1.5*width, values2, width,color='#FFBE7A', label='HawkEye-Conv2d', hatch='\\')
rects3 = ax.bar(x- 0.5*width, values3, width, color='#FA7F6F',label='CrypTFlow2-Other-Liner', hatch='-')
rects4 = ax.bar(x + 0.5* width, values4, width,color='#82B0D2', label='HawkEye-Other-Liner', hatch='.')
rects5 = ax.bar(x + 1.5*width, values5, width,color='#F6CAE5', label='CrypTFlow2-Non-Liner', hatch='|')
rects6 = ax.bar(x + 2.5*width, values6, width,color='#E7DAD2', label='HawkEye-Non-Liner', hatch='x')
plt.bar_label(rects1, label_type='edge', fontproperties=font1)
plt.bar_label(rects2, label_type='edge', fontproperties=font1)
plt.bar_label(rects3, label_type='edge', fontproperties=font1)
plt.bar_label(rects4, label_type='edge', fontproperties=font1)
plt.bar_label(rects5, label_type='edge', fontproperties=font1)
plt.bar_label(rects6, label_type='edge', fontproperties=font1)
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
plt.savefig('round_crypTFlow.pdf')


