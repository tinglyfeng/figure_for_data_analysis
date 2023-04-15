
#%%
# figure data
import random
import matplotlib.colors as mcolors
from matplotlib import pyplot as plt
groups = ["Group {}".format(i) for i in range(6)]
labels = ['Label {}'.format(i) for i in range(6)]
groups_len = len(groups)
xss = [[ 1 / groups_len * i  + random.random() / len(groups)  for _ in range(1000)] for i in range(groups_len)]
yss = [[random.random() for _ in range(1000)] for i in range(groups_len)]

# figure params
color_list = list(mcolors.TABLEAU_COLORS)
marker_size = 60
legend_font_size = 16
axis_label_size = 20
tick_label_size = 14

fig, ax = plt.subplots(figsize = (12,6))
handles = []
for i in range(groups_len):
    h = ax.scatter(xss[i], yss[i], c = color_list[i], marker = "o", s = marker_size, edgecolor='black')
    handles.append(h)
    
ax.spines["right"].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines["left"].set_visible(False)
ax.grid(color='gray', linestyle='-', linewidth=0.5, axis='y', alpha=1)
ax.legend(handles = handles, labels = labels, ncol = groups_len, bbox_to_anchor=(0.92, 1.15),fontsize = legend_font_size, columnspacing=0.5,handletextpad=0.01,markerscale=2)


ax.set_ylabel("yLabel",fontsize = axis_label_size)
ax.set_xlabel("xLabel",fontsize = axis_label_size)
ax.tick_params(axis='x', labelsize = tick_label_size)
ax.tick_params(axis='y', labelsize = tick_label_size)

fig.savefig('./figures/colorful_scatter.svg')