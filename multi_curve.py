import numpy as np
from matplotlib import pyplot as plt

# figure data
y_data1 = np.sort(np.random.choice(100,9))
y_data2 = np.sort(np.random.choice(100,9))[::-1]
y_data3 = np.sort(np.random.choice(10,9))
y_data4 = np.sort(np.random.choice(10,9))[::-1]

x_data = [i for i in range(0,256 + 32, 32)]



# figure params
color1 = "darkviolet"
color2 = "coral"
line1 = '-'
line2 = '--'
marker = 'o'
x_label_fontsize = 32
y_label_fontsize = 28
tick_label_size = 22
legend_labelsize = 23
markersize = 12
linewidth = 4

# figure making
fig, ax = plt.subplots(figsize=(18,8))
fig.subplots_adjust(right=0.75)
tw = ax.twinx()
p1, = ax.plot(x_data, y_data1,color1, linestyle = line1, label="Type 1 ", marker = marker, markersize = markersize, linewidth = linewidth)
p2, = ax.plot(x_data, y_data2, color1, linestyle = line2, label="Type 2", marker = marker, markersize = markersize, linewidth = linewidth)
p3, = tw.plot(x_data, y_data3,color2, linestyle = line1,label="Type 3", marker = marker, markersize = markersize, linewidth = linewidth)
p4, = tw.plot(x_data, y_data4,color2,linestyle = line2, label="Type 4", marker = marker, markersize = markersize, linewidth = linewidth)

ax.set_xlabel("xLabel",fontsize= x_label_fontsize)
ax.set_ylabel("yLabel 1", fontsize = y_label_fontsize)
tw.set_ylabel("yLabel 2", fontsize = y_label_fontsize)
ax.yaxis.label.set_color(p1.get_color())
tw.yaxis.label.set_color(p3.get_color())
tkw = dict(size=6, width=1.5, labelsize = tick_label_size)
ax.tick_params(axis='y', colors=p1.get_color(), **tkw)
tw.tick_params(axis='y', colors=p3.get_color(), **tkw)
ax.tick_params(axis='x', **tkw)
ax.legend(handles=[p1,p2, p3, p4], loc='upper center', ncol = 4,
          bbox_to_anchor = (0.5,1.176),fontsize = legend_labelsize)
ax.grid(which='major', axis='both',linestyle='--')
plt.tight_layout()
plt.savefig('./figures/multi_curve.svg')





